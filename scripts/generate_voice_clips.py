#!/usr/bin/env python3
"""
generate_voice_clips.py — Generates local neural speech clips for the Shadow of Mars campaign
using the local openedai-speech Docker container (port 8001).

Usage:
    python3 scripts/generate_voice_clips.py [--session 4|5] [--clip-id ID] [--dry-run]
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error


def generate_clip(endpoint: str, model: str, voice: str, text: str, output_path: str, dry_run: bool = False) -> bool:
    print(f" -> Generating [{voice}]: {output_path} ({len(text)} chars)...")
    if dry_run:
        print("    [DRY RUN] Skipped API call.")
        return True

    payload = json.dumps({
        "model": model,
        "input": text,
        "voice": voice
    }).encode("utf-8")

    req = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.status != 200:
                print(f"    [ERROR] HTTP {response.status}: {response.read().decode('utf-8')}", file=sys.stderr)
                return False
            data = response.read()
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(data)
            print(f"    [OK] Saved {len(data):,} bytes.")
            return True
    except urllib.error.URLError as e:
        print(f"    [FAIL] Could not connect to {endpoint}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Generate NPC and narrative audio clips via openedai-speech.")
    parser.add_argument("--manifest", default="audio/voice_manifest.json", help="Path to voice manifest JSON")
    parser.add_argument("--output-dir", default="audio/clips", help="Target directory for generated mp3 files")
    parser.add_argument("--session", type=int, choices=[4, 5], help="Filter by session number (4 or 5)")
    parser.add_argument("--clip-id", help="Generate only a specific clip ID")
    parser.add_argument("--endpoint", help="Override speech endpoint URL")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without making network requests")
    parser.add_argument("--force", action="store_true", help="Regenerate even if output file already exists")

    args = parser.parse_args()

    if not os.path.exists(args.manifest):
        print(f"Error: manifest '{args.manifest}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(args.manifest, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    endpoint = args.endpoint or manifest.get("endpoint", "http://localhost:8001/v1/audio/speech")
    default_model = manifest.get("default_model", "tts-1")
    clips = manifest.get("clips", [])

    filtered_clips = []
    for c in clips:
        if args.session and c.get("session") != args.session:
            continue
        if args.clip_id and c.get("id") != args.clip_id:
            continue
        filtered_clips.append(c)

    if not filtered_clips:
        print("No matching clips found in manifest.")
        return

    print(f"=== Shadow of Mars Voice Generator ===")
    print(f"Endpoint: {endpoint}")
    print(f"Clips to process: {len(filtered_clips)}")
    print(f"Output directory: {args.output_dir}\n")

    os.makedirs(args.output_dir, exist_ok=True)

    success_count = 0
    fail_count = 0

    for clip in filtered_clips:
        clip_id = clip["id"]
        out_path = os.path.join(args.output_dir, f"{clip_id}.mp3")

        if os.path.exists(out_path) and not args.force and not args.dry_run:
            print(f" -> Skipping [{clip_id}]: {out_path} already exists (use --force to overwrite).")
            success_count += 1
            continue

        model = clip.get("model", default_model)
        voice = clip.get("voice", "onyx")
        text = clip["text"]

        ok = generate_clip(endpoint, model, voice, text, out_path, dry_run=args.dry_run)
        if ok:
            success_count += 1
        else:
            fail_count += 1

    print(f"\nCompleted: {success_count} succeeded, {fail_count} failed.")
    if fail_count > 0 and not args.dry_run:
        sys.exit(1)


if __name__ == "__main__":
    main()
