# utils/format_utils.py

import re
from uuid import uuid4
from datetime import datetime

def generate_id():
    return str(uuid4())

def simple_clean(text: str) -> str:
    # Remove HTML tags and redundant whitespace
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()

def tag_entry(entry: dict) -> list:
    tags = []
    text = f"{entry.get('title', '')} {entry.get('body', '')}".lower()
    if "contract" in text: tags.append("contract")
    if "geospatial" in text: tags.append("geospatial")
    if "tender" in text: tags.append("tender")
    if "water" in text: tags.append("water")
    if "infrastructure" in text: tags.append("infrastructure")
    return tags

def tag_and_format(raw_entry: dict) -> dict:
    return {
        "id": generate_id(),
        "title": simple_clean(raw_entry.get("title", "Untitled")),
        "body": simple_clean(raw_entry.get("body", "")),
        "tags": tag_entry(raw_entry),
        "timestamp": datetime.utcnow().isoformat()
    }
