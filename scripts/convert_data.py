# scripts/convert_data.py

import os
import json
import sqlite3
from utils.format_utils import tag_and_format
from utils.log import logger
from pathlib import Path
from datetime import datetime

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
EXPORT_DIRS = {
    "jsonl": Path("vaults/jsonl"),
    "markdown": Path("vaults/markdown"),
    "pdf": Path("vaults/pdf"),
    "sqlite": Path("vaults/sqlite"),
}

def load_raw_data():
    logger.info("Loading raw data...")
    for file in RAW_DIR.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            yield json.load(f)

def process_data(entry):
    # Placeholder for advanced NLP or tagging pipeline
    return tag_and_format(entry)

def export_to_jsonl(processed_data, filename):
    out_path = EXPORT_DIRS["jsonl"] / f"{filename}.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for item in processed_data:
            f.write(json.dumps(item) + "\n")
    logger.info(f"Exported JSONL: {out_path}")

def export_to_markdown(processed_data, filename):
    out_path = EXPORT_DIRS["markdown"] / f"{filename}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        for item in processed_data:
            f.write(f"### {item['title']}\n{item['body']}\n\n---\n")
    logger.info(f"Exported Markdown: {out_path}")

def export_to_sqlite(processed_data, filename):
    db_path = EXPORT_DIRS["sqlite"] / f"{filename}.db"
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS exports (id TEXT, title TEXT, body TEXT, tags TEXT)''')
    for item in processed_data:
        c.execute("INSERT INTO exports VALUES (?, ?, ?, ?)",
                  (item['id'], item['title'], item['body'], ','.join(item['tags'])))
    conn.commit()
    conn.close()
    logger.info(f"Exported SQLite DB: {db_path}")

def run_conversion():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"converted_{timestamp}"
    all_processed = []

    for entry in load_raw_data():
        processed = process_data(entry)
        all_processed.append(processed)

    export_to_jsonl(all_processed, filename)
    export_to_markdown(all_processed, filename)
    export_to_sqlite(all_processed, filename)
    # Future-proof: PDF or custom format modules can be added later

if __name__ == "__main__":
    run_conversion()
