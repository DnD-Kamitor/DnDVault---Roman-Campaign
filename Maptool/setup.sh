#!/usr/bin/env bash
# MapTool standalone setup for Shadow of Mars campaign
# Run once from inside the Maptool/ folder: bash setup.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_DIR="$SCRIPT_DIR/app"
DATA_DIR="$SCRIPT_DIR/data"

MT_DEB="$SCRIPT_DIR/maptool_1.18.6-amd64.deb"
TT_DEB="$SCRIPT_DIR/tokentool_2.3.0_amd64.deb"
MT_ROOT="$APP_DIR/maptool/opt/maptool"
TT_ROOT="$APP_DIR/tokentool/opt/tokentool"
MT_CFG="$MT_ROOT/lib/app/MapTool.cfg"

log()  { printf '\033[0;32m[setup]\033[0m %s\n' "$*"; }
skip() { printf '\033[0;33m[skip] \033[0m %s\n' "$*"; }
warn() { printf '\033[0;31m[warn] \033[0m %s\n' "$*"; }

# ─── 1. Extract applications ──────────────────────────────────────────────────

log "=== 1. Extract applications from .deb ==="

[ -f "$MT_DEB" ] || { echo "ERROR: $MT_DEB not found."; exit 1; }

if [ -d "$MT_ROOT" ]; then
    skip "MapTool already extracted."
else
    log "Extracting MapTool 1.18.6 (this takes a moment)..."
    mkdir -p "$APP_DIR/maptool"
    dpkg-deb -x "$MT_DEB" "$APP_DIR/maptool"
    log "MapTool extracted."
fi

if [ -f "$TT_DEB" ]; then
    if [ -d "$TT_ROOT" ]; then
        skip "TokenTool already extracted."
    else
        log "Extracting TokenTool 2.3.0..."
        mkdir -p "$APP_DIR/tokentool"
        dpkg-deb -x "$TT_DEB" "$APP_DIR/tokentool"
        log "TokenTool extracted."
    fi
else
    warn "$TT_DEB not found; skipping TokenTool."
fi

# ─── 2. Patch MapTool.cfg for local data directory ────────────────────────────

log "=== 2. Configure local data directory ==="

[ -f "$MT_CFG" ] || { echo "ERROR: $MT_CFG not found after extraction."; exit 1; }

if grep -qF "MAPTOOL_DATADIR=$DATA_DIR" "$MT_CFG"; then
    skip "MapTool.cfg already points to local data/."
else
    sed -i "s|java-options=-DMAPTOOL_DATADIR=.*|java-options=-DMAPTOOL_DATADIR=$DATA_DIR|" "$MT_CFG"
    log "Patched MapTool.cfg: MAPTOOL_DATADIR -> $DATA_DIR"
fi

# ─── 3. Create directory structure ────────────────────────────────────────────

log "=== 3. Create directory structure ==="

mkdir -p \
    "$DATA_DIR" \
    "$SCRIPT_DIR/campaigns/5e" \
    "$SCRIPT_DIR/campaigns/roman" \
    "$SCRIPT_DIR/addons/MTLib" \
    "$SCRIPT_DIR/addons/builtin-source" \
    "$SCRIPT_DIR/maps/roman" \
    "$SCRIPT_DIR/maps/wilderness"

log "Directories ready."

# ─── 4. Organize existing campaign files ──────────────────────────────────────

log "=== 4. Organize campaigns ==="

for f in "$SCRIPT_DIR"/*.cmpgn; do
    [ -f "$f" ] || continue
    name="$(basename "$f")"
    dest="$SCRIPT_DIR/campaigns/5e/$name"
    if [ ! -f "$dest" ]; then
        mv "$f" "$dest"
        log "Moved: $name -> campaigns/5e/"
    else
        skip "$name already in campaigns/5e/"
    fi
done

# ─── 5. Download addons and frameworks from GitHub ────────────────────────────

log "=== 5. Download addons from GitHub ==="

gh_release() {
    local repo="$1" pattern="$2" dest="$3"
    mkdir -p "$dest"
    local url="https://api.github.com/repos/$repo/releases/latest"
    local json
    json="$(curl -fsSL --retry 3 --connect-timeout 15 "$url" 2>/dev/null)" || {
        warn "Cannot reach GitHub for $repo — skipping."
        return 0
    }
    python3 - "$json" "$pattern" "$dest" <<'PY'
import json, os, re, sys, urllib.request
raw, pattern, dest = sys.argv[1:4]
try:
    data = json.loads(raw)
except Exception:
    print("  ERROR: invalid JSON response")
    sys.exit(0)
tag = data.get("tag_name", "unknown")
rx = re.compile(pattern, re.IGNORECASE)
matched = [a for a in data.get("assets", []) if rx.search(a["name"])]
if not matched:
    print(f"  [{tag}] no assets match {pattern!r}")
    sys.exit(0)
for a in matched:
    name, url = a["name"], a["browser_download_url"]
    out = os.path.join(dest, name)
    if os.path.exists(out) and os.path.getsize(out) > 0:
        print(f"  [{tag}] skip (exists): {name}")
        continue
    print(f"  [{tag}] downloading: {name} ...", flush=True)
    req = urllib.request.Request(url, headers={"User-Agent": "maptool-setup/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r, open(out, "wb") as f:
            f.write(r.read())
        print(f"  [{tag}] saved: {out}")
    except Exception as e:
        print(f"  [{tag}] FAILED: {e}")
PY
}

gh_zip() {
    local repo="$1" dest="$2" branch="${3:-main}"
    mkdir -p "$dest"
    local name; name="$(echo "$repo" | tr '/' '-')-${branch}.zip"
    local out="$dest/$name"
    [ -f "$out" ] && { skip "$name"; return 0; }
    log "Downloading source zip: $repo ($branch)"
    curl -fsSL --retry 3 --connect-timeout 15 \
        "https://github.com/$repo/archive/refs/heads/${branch}.zip" \
        -o "$out" 2>/dev/null || warn "Could not download $repo — skipping."
}

# Melek's Simple 5e — clean, readable 5e framework; best starting point
log "Checking: melek/Simple5e"
gh_release "melek/Simple5e" '\.(cmpgn|zip)$' "$SCRIPT_DIR/campaigns/5e"

# Automated 5e by Pmofmalasia — richer dice/automation (heavier)
log "Checking: Pmofmalasia/Automated-5e"
gh_release "Pmofmalasia/Automated-5e" '\.(cmpgn|zip)$' "$SCRIPT_DIR/campaigns/5e"

# Lib_DateTime — .mtlib add-on for calendar/time tracking macros
log "Checking: ColdAnkles/Lib_DateTime"
gh_release "ColdAnkles/Lib_DateTime" '\.(mtlib|zip)$' "$SCRIPT_DIR/addons/MTLib"

# RPTools built-in addons source — reference macros bundled with MapTool itself
log "Checking: RPTools/maptool-builtin-addons"
gh_zip "RPTools/maptool-builtin-addons" "$SCRIPT_DIR/addons/builtin-source"

# ─── 6. Launcher scripts ──────────────────────────────────────────────────────

log "=== 6. Create launcher scripts ==="

cat > "$SCRIPT_DIR/maptool.sh" <<'LAUNCH'
#!/usr/bin/env bash
# Launch MapTool — all data stays in ./data/ (standalone)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BINARY="$SCRIPT_DIR/app/maptool/opt/maptool/bin/MapTool"

if [ ! -x "$BINARY" ]; then
    echo "ERROR: MapTool binary not found. Run: bash setup.sh"
    exit 1
fi

exec "$BINARY" "$@"
LAUNCH
chmod +x "$SCRIPT_DIR/maptool.sh"
log "Created: maptool.sh"

if [ -d "$TT_ROOT" ]; then
    cat > "$SCRIPT_DIR/tokentool.sh" <<'LAUNCH'
#!/usr/bin/env bash
# Launch TokenTool — token portrait creator
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BINARY="$SCRIPT_DIR/app/tokentool/opt/tokentool/bin/TokenTool"

if [ ! -x "$BINARY" ]; then
    echo "ERROR: TokenTool binary not found. Run: bash setup.sh"
    exit 1
fi

exec "$BINARY" "$@"
LAUNCH
    chmod +x "$SCRIPT_DIR/tokentool.sh"
    log "Created: tokentool.sh"
fi

# ─── 7. Gitignore for large binaries ──────────────────────────────────────────

log "=== 7. .gitignore ==="

GIFILE="$SCRIPT_DIR/.gitignore"
if [ ! -f "$GIFILE" ]; then
    cat > "$GIFILE" <<'GI'
# Extracted application binaries — recreated by setup.sh
app/

# MapTool runtime data (preferences, cache, autosaves, imported resources)
data/

# Original .deb installers (large; re-download if needed)
*.deb

# Zip archives (token pack, source zips)
dnd5eTokens.zip
addons/builtin-source/
GI
    log "Created: .gitignore"
else
    skip ".gitignore already exists."
fi

# ─── Done ─────────────────────────────────────────────────────────────────────

echo
echo "╔══════════════════════════════════════════════════════╗"
echo "║    MapTool standalone setup complete                 ║"
echo "╚══════════════════════════════════════════════════════╝"
echo
echo "  Launch MapTool:    ./maptool.sh"
echo "  Launch TokenTool:  ./tokentool.sh"
echo
echo "  MapTool data dir:  $DATA_DIR"
echo "    Stores: preferences, autosaves, imported resources"
echo
echo "──── After first launch, do these once in MapTool ──────"
echo
echo "  Add token images to the Resource Library:"
echo "    File > Add Resource to Library > Local Directory"
echo "    Folder: $SCRIPT_DIR/dnd5eTokens"
echo
echo "  Load .rptok library tokens (drag onto a GM Layer map):"
echo "    $SCRIPT_DIR/addons/Lib_MonsterMaker/"
echo "    $SCRIPT_DIR/addons/Lib_SpellLibrary/"
echo
echo "  Import .mtlib add-on libraries:"
echo "    File > Import Add-On Library"
echo "    Folder: $SCRIPT_DIR/addons/MTLib/"
echo
echo "  Open a campaign:"
echo "    File > Open Campaign"
echo "    Folder: $SCRIPT_DIR/campaigns/5e/"
echo "    Recommended start: Meleks.Simple.5e.v2.3.0.cmpgn"
echo
echo "──── Memory tip ────────────────────────────────────────"
echo "  For heavy campaigns, raise the heap in:"
echo "  $MT_CFG"
echo "  Add: java-options=-Xmx4g"
echo
