#!/usr/bin/env python3
"""
Campaign RAG Chunking & Qdrant Ingestion Script (Story 12.1)

Indexes campaign knowledge files (CAMPAIGN_LOG.md, knowledge.qmd,
vindolanda_guide.qmd, npcs/*.json, chapter4.qmd, chapter5.qmd)
into Qdrant (http://localhost:6333) collection 'shadow-of-mars'.
Embeds with nomic-embed-text via LiteLLM or native Ollama.
"""

import argparse
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
DEFAULT_LITELLM_URL = os.environ.get("LITELLM_URL", "http://localhost:4000/v1/embeddings")
DEFAULT_LITELLM_KEY = os.environ.get("LITELLM_MASTER_KEY", "sk-localstack-5WU8JxXMD2zvhogkbVaY")
DEFAULT_OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/embeddings")
COLLECTION_NAME = "shadow-of-mars"
VECTOR_SIZE = 768


_USE_LITELLM = None


def check_litellm_embeddings():
    global _USE_LITELLM
    if _USE_LITELLM is not None:
        return _USE_LITELLM
    try:
        req_data = json.dumps({"model": "nomic-embed-text", "input": "health"}).encode("utf-8")
        req = urllib.request.Request(
            DEFAULT_LITELLM_URL,
            data=req_data,
            headers={
                "Authorization": f"Bearer {DEFAULT_LITELLM_KEY}",
                "Content-Type": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=1.5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "data" in data and len(data["data"]) > 0:
                _USE_LITELLM = True
                print("  [Embeddings] Connected to LiteLLM.")
                return True
    except Exception:
        pass
    _USE_LITELLM = False
    print("  [Embeddings] Using high-speed native Ollama (http://localhost:11434).")
    return False


def get_embedding(text: str, model: str = "nomic-embed-text") -> list:
    """Generate embedding vector using LiteLLM with fallback to native Ollama."""
    if check_litellm_embeddings():
        try:
            req_data = json.dumps({"model": model, "input": text}).encode("utf-8")
            req = urllib.request.Request(
                DEFAULT_LITELLM_URL,
                data=req_data,
                headers={
                    "Authorization": f"Bearer {DEFAULT_LITELLM_KEY}",
                    "Content-Type": "application/json",
                },
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data["data"][0]["embedding"]
        except Exception:
            pass

    # Native Ollama
    req_data = json.dumps({"model": model, "prompt": text}).encode("utf-8")
    req = urllib.request.Request(
        DEFAULT_OLLAMA_URL,
        data=req_data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data["embedding"]


def chunk_markdown(file_path: Path, max_chars: int = 1500) -> list:
    """Chunk markdown document by headers and paragraphs."""
    content = file_path.read_text(encoding="utf-8")
    rel_path = str(file_path.relative_to(BASE_DIR))
    chunks = []

    # Split into sections based on # or ## or ###
    lines = content.split("\n")
    current_heading = file_path.stem.replace("_", " ").title()
    current_lines = []

    def flush_chunk(lines_to_flush, heading):
        text = "\n".join(lines_to_flush).strip()
        if not text or len(text) < 40:
            return
        # If text is too long, split by double newlines
        if len(text) > max_chars:
            paras = text.split("\n\n")
            sub_buf = []
            sub_len = 0
            for p in paras:
                if sub_len + len(p) > max_chars and sub_buf:
                    chunk_text = f"[{heading}]\n" + "\n\n".join(sub_buf).strip()
                    chunks.append({
                        "source": rel_path,
                        "heading": heading,
                        "text": chunk_text
                    })
                    sub_buf = [p]
                    sub_len = len(p)
                else:
                    sub_buf.append(p)
                    sub_len += len(p)
            if sub_buf:
                chunk_text = f"[{heading}]\n" + "\n\n".join(sub_buf).strip()
                chunks.append({
                    "source": rel_path,
                    "heading": heading,
                    "text": chunk_text
                })
        else:
            chunks.append({
                "source": rel_path,
                "heading": heading,
                "text": f"[{heading}]\n{text}"
            })

    for line in lines:
        header_match = re.match(r"^(#{1,4})\s+(.+)$", line)
        if header_match:
            flush_chunk(current_lines, current_heading)
            current_lines = []
            current_heading = header_match.group(2).strip()
        else:
            current_lines.append(line)

    flush_chunk(current_lines, current_heading)
    return chunks


def chunk_npc(file_path: Path) -> dict:
    """Format NPC json file into a structured semantic chunk."""
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
    except Exception:
        return None

    name = data.get("name") or file_path.stem.replace("_", " ").title()
    cr = data.get("cr", "unknown")
    alignment = data.get("alignment", "unknown")
    ac = data.get("ac", "unknown")
    hp = data.get("hp", "unknown")
    speed = data.get("speed", "unknown")

    text_parts = [
        f"NPC Profile: {name}",
        f"Challenge Rating: {cr} | Alignment: {alignment} | AC: {ac} | HP: {hp} | Speed: {speed}"
    ]

    if "description" in data and data["description"]:
        text_parts.append(f"Description: {data['description']}")

    # Ability scores
    if "ability_scores" in data and isinstance(data["ability_scores"], dict):
        scores = ", ".join(f"{k}: {v}" for k, v in data["ability_scores"].items())
        text_parts.append(f"Ability Scores: {scores}")

    # Traits
    if "traits" in data and data["traits"]:
        traits = data["traits"]
        if isinstance(traits, list):
            text_parts.append("Special Traits:\n" + "\n".join(f"- {t}" for t in traits))
        elif isinstance(traits, str):
            text_parts.append(f"Special Traits: {traits}")

    # Actions / Attacks
    if "attacks" in data and data["attacks"]:
        text_parts.append("Attacks / Actions:")
        for atk in data["attacks"]:
            label = atk.get("label", "Attack")
            note = atk.get("note", "")
            raw_cmd = atk.get("raw_cmd", "")
            desc = note or raw_cmd or f"Bonus: {atk.get('atk', '')}, Damage: {atk.get('dice', '')}"
            text_parts.append(f"- {label}: {desc}")

    # Notes / Secrets / Lore
    if "notes" in data and data["notes"]:
        text_parts.append(f"Notes & Tactics: {data['notes']}")
    if "gm_notes" in data and data["gm_notes"]:
        text_parts.append(f"GM Lore & Secrets: {data['gm_notes']}")
    if "secret" in data and data["secret"]:
        text_parts.append(f"Secret: {data['secret']}")

    rel_path = str(file_path.relative_to(BASE_DIR))
    return {
        "source": rel_path,
        "heading": f"NPC: {name}",
        "npc_name": name,
        "cr": str(cr),
        "text": "\n".join(text_parts)
    }


def ensure_qdrant_collection(qdrant_url: str, collection_name: str, recreate: bool = False):
    """Ensure collection exists in Qdrant with correct vector size."""
    col_url = f"{qdrant_url}/collections/{collection_name}"
    
    if recreate:
        try:
            req = urllib.request.Request(col_url, method="DELETE")
            urllib.request.urlopen(req, timeout=5)
            print(f"Deleted existing collection '{collection_name}' for clean rebuild.")
        except Exception:
            pass

    # Check if exists
    try:
        req = urllib.request.Request(col_url)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("result", {}).get("status") in ("green", "yellow", "ok"):
                print(f"Collection '{collection_name}' already exists.")
                return
    except urllib.error.HTTPError as e:
        if e.code != 404:
            pass
    except Exception:
        pass

    # Create collection
    create_payload = json.dumps({
        "vectors": {
            "size": VECTOR_SIZE,
            "distance": "Cosine"
        }
    }).encode("utf-8")
    req = urllib.request.Request(
        col_url,
        data=create_payload,
        headers={"Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print(f"Created Qdrant collection '{collection_name}': {res}")


def upsert_points(qdrant_url: str, collection_name: str, points: list):
    """Upload a batch of points to Qdrant."""
    url = f"{qdrant_url}/collections/{collection_name}/points"
    req_data = json.dumps({"points": points}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={"Content-Type": "application/json"},
        method="PUT"
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        return res


def search_qdrant(qdrant_url: str, collection_name: str, query_text: str, top_k: int = 3):
    """Query Qdrant collection using semantic vector search."""
    vec = get_embedding(query_text)
    url = f"{qdrant_url}/collections/{collection_name}/points/search"
    req_data = json.dumps({
        "vector": vec,
        "limit": top_k,
        "with_payload": True
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        return res.get("result", [])


def run_ingestion(recreate: bool = False):
    print("=== Starting Campaign RAG Ingestion into Qdrant ===")
    ensure_qdrant_collection(DEFAULT_QDRANT_URL, COLLECTION_NAME, recreate=recreate)

    # 1. Collect all chunks
    all_chunks = []

    # Key campaign markdown files
    md_files = [
        BASE_DIR / "knowledge.qmd",
        BASE_DIR / "vindolanda_guide.qmd",
        BASE_DIR / "CAMPAIGN_LOG.md",
        BASE_DIR / "corruption.qmd",
        BASE_DIR / "roman_tactics.qmd",
        BASE_DIR / "chapter4.qmd",
        BASE_DIR / "chapter5.qmd",
    ]

    for p in md_files:
        if p.exists():
            chunks = chunk_markdown(p)
            print(f"Extracted {len(chunks)} chunks from {p.name}")
            all_chunks.extend(chunks)

    # NPC JSON files
    npc_files = sorted((BASE_DIR / "npcs").glob("*.json"))
    npc_count = 0
    for np in npc_files:
        chunk = chunk_npc(np)
        if chunk:
            all_chunks.append(chunk)
            npc_count += 1
    print(f"Extracted {npc_count} structured profiles from npcs/*.json")
    print(f"Total chunks to embed and index: {len(all_chunks)}")

    # 2. Embed and upsert in batches
    batch_size = 25
    points_batch = []
    total_indexed = 0

    t_start = time.time()
    for idx, c in enumerate(all_chunks):
        vec = get_embedding(c["text"])
        point = {
            "id": idx + 1,
            "vector": vec,
            "payload": {
                "source": c["source"],
                "heading": c["heading"],
                "text": c["text"],
                "char_count": len(c["text"])
            }
        }
        if "npc_name" in c:
            point["payload"]["npc_name"] = c["npc_name"]
            point["payload"]["cr"] = c["cr"]

        points_batch.append(point)

        if len(points_batch) >= batch_size or idx == len(all_chunks) - 1:
            upsert_points(DEFAULT_QDRANT_URL, COLLECTION_NAME, points_batch)
            total_indexed += len(points_batch)
            print(f"  Indexed {total_indexed}/{len(all_chunks)} chunks ({int(total_indexed/len(all_chunks)*100)}%)...")
            points_batch = []

    elapsed = round(time.time() - t_start, 2)
    print(f"=== Successfully indexed {total_indexed} chunks in {elapsed}s! ===")

    # 3. Verification query
    test_query = "Who forged the chains of Mars?"
    print(f"\n--- Running Verification Semantic Query: '{test_query}' ---")
    results = search_qdrant(DEFAULT_QDRANT_URL, COLLECTION_NAME, test_query, top_k=3)
    for rank, res in enumerate(results, 1):
        score = round(res.get("score", 0), 4)
        payload = res.get("payload", {})
        source = payload.get("source", "unknown")
        heading = payload.get("heading", "")
        text_preview = payload.get("text", "").replace("\n", " ")[:200]
        print(f"#{rank} [Score: {score}] Source: {source} ({heading})")
        print(f"   Excerpt: {text_preview}...\n")


def main():
    parser = argparse.ArgumentParser(description="Campaign RAG Qdrant Ingestion")
    parser.add_argument("--recreate", action="store_true", help="Recreate Qdrant collection from scratch")
    parser.add_argument("--query", type=str, help="Run semantic search query against index")
    parser.add_argument("--top-k", type=int, default=3, help="Number of results for query")
    args = parser.parse_args()

    if args.query:
        results = search_qdrant(DEFAULT_QDRANT_URL, COLLECTION_NAME, args.query, top_k=args.top_k)
        print(f"Search results for: '{args.query}' (top {len(results)}):")
        for i, r in enumerate(results, 1):
            score = round(r.get("score", 0), 4)
            p = r.get("payload", {})
            print(f"\n[{i}] Score: {score} | {p.get('source')} | {p.get('heading')}")
            print(p.get("text", "")[:400] + "...")
        return

    run_ingestion(recreate=args.recreate or True)


if __name__ == "__main__":
    main()
