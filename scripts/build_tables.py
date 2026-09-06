"""
build_tables.py — generates Quarto-include markdown tables from data/ CSVs.
Run automatically via _quarto.yml pre-render hook, or manually: python scripts/build_tables.py
Output files land in _generated/ and are gitignored.
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
OUT_DIR  = BASE_DIR / "_generated"
OUT_DIR.mkdir(exist_ok=True)


def read_csv(filename: str) -> list[dict]:
    with open(DATA_DIR / filename, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pipe_table(rows: list[dict], cols: list[str], headers: list[str]) -> str:
    """Return a Quarto-compatible pipe table string."""
    sep = "|" + "|".join(["---"] * len(headers)) + "|"
    header_row = "| " + " | ".join(headers) + " |"
    data_rows = [
        "| " + " | ".join(str(row.get(c, "") or "").replace("|", "/") for c in cols) + " |"
        for row in rows
    ]
    return "\n".join([header_row, sep] + data_rows) + "\n"


def write(filename: str, content: str) -> None:
    path = OUT_DIR / filename
    path.write_text(content, encoding="utf-8")
    print(f"  wrote {path.relative_to(BASE_DIR)}")


# ── Equipment tables ──────────────────────────────────────────────────────────

equip = read_csv("equipment.csv")

MELEE_COLS    = ["name_latin", "name_english", "damage", "damage_type", "weight_lb", "cost_d", "properties", "culture", "availability"]
MELEE_HEADS   = ["*Latin*", "English", "Damage", "Type", "Wt (lb)", "Cost (d)", "Properties", "Culture", "Avail."]

RANGED_COLS   = ["name_latin", "name_english", "damage", "damage_type", "range", "weight_lb", "cost_d", "culture", "availability"]
RANGED_HEADS  = ["*Latin*", "English", "Damage", "Type", "Range", "Wt (lb)", "Cost (d)", "Culture", "Avail."]

AMMO_COLS     = ["name_latin", "name_english", "damage", "damage_type", "range", "weight_lb", "cost_d", "availability"]
AMMO_HEADS    = ["*Latin*", "English", "Damage", "Type", "Range", "Wt (lb)", "Cost (d)", "Avail."]

ARMOR_COLS    = ["name_latin", "name_english", "type", "ac", "weight_lb", "cost_d", "culture", "availability"]
ARMOR_HEADS   = ["*Latin*", "English", "Class", "AC", "Wt (lb)", "Cost (d)", "Culture", "Avail."]

SHIELD_COLS   = ["name_latin", "name_english", "ac", "weight_lb", "cost_d", "culture", "availability"]
SHIELD_HEADS  = ["*Latin*", "English", "AC", "Wt (lb)", "Cost (d)", "Culture", "Avail."]

HELMET_COLS   = ["name_latin", "name_english", "ac", "weight_lb", "cost_d", "culture", "availability"]
HELMET_HEADS  = ["*Latin*", "English", "AC bonus", "Wt (lb)", "Cost (d)", "Culture", "Avail."]

GEAR_COLS     = ["name_latin", "name_english", "slot", "weight_lb", "cost_d", "culture", "availability"]
GEAR_HEADS    = ["*Latin*", "English", "Slot", "Wt (lb)", "Cost (d)", "Culture", "Avail."]

melee      = [r for r in equip if r["category"] == "melee"]
thrown     = [r for r in equip if r["category"] == "thrown"]
ranged     = [r for r in equip if r["category"] == "ranged"]
siege      = [r for r in equip if r["category"] == "siege"]
ammo       = [r for r in equip if r["category"] == "ammo"]
armor      = [r for r in equip if r["category"] == "body_armor"]
shields    = [r for r in equip if r["category"] == "shield"]
helmets    = [r for r in equip if r["category"] == "helmet"]
gear       = [r for r in equip if r["category"] == "gear" and r.get("slot") != "helmet"]
commission = [r for r in equip if r["availability"] == "commission"]
vicus      = [r for r in equip if r["availability"] == "vicus"]
aelius     = [r for r in equip if r["availability"] == "aelius"]

MARKET_COLS  = ["name_latin", "name_english", "cost_d", "special"]
MARKET_HEADS = ["*Latin*", "English", "Cost (d)", "Mechanics"]

write("ref_weapons_melee.md",   pipe_table(melee,           MELEE_COLS,   MELEE_HEADS))
write("ref_weapons_thrown.md",  pipe_table(thrown,          RANGED_COLS,  RANGED_HEADS))
write("ref_weapons_ranged.md",  pipe_table(ranged + siege,  RANGED_COLS,  RANGED_HEADS))
write("ref_ammo.md",            pipe_table(ammo,            AMMO_COLS,    AMMO_HEADS))
write("ref_armor.md",           pipe_table(armor,           ARMOR_COLS,   ARMOR_HEADS))
write("ref_shields.md",         pipe_table(shields,         SHIELD_COLS,  SHIELD_HEADS))
write("ref_helmets.md",         pipe_table(helmets,         HELMET_COLS,  HELMET_HEADS))
write("ref_gear.md",            pipe_table(gear,            GEAR_COLS,    GEAR_HEADS))
write("ref_commission.md",      pipe_table(commission,      MARKET_COLS,  MARKET_HEADS))
write("ref_vicus.md",           pipe_table(vicus,           MARKET_COLS,  MARKET_HEADS))
write("ref_aelius.md",          pipe_table(aelius,          MARKET_COLS,  MARKET_HEADS))

print(f"Done — {len(list(OUT_DIR.glob('*.md')))} files in _generated/")
