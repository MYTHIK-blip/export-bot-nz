"""
fetch_sources.py

Handles ingestion of raw datasets from the URLs defined in sources.yaml.
Supports multiple content types: .csv, .tsv, .json, .xml, .rss, .txt, .html
Built to allow retries, offline fallback, and source health telemetry.
"""

import os
import requests
import time
import logging
from urllib.parse import urlparse
from utils.log import setup_logger
from utils.format_utils import slugify

logger = setup_logger("Fetcher")

def fetch_source(name, url, output_dir, max_retries=3):
    parsed = urlparse(url)
    filename = f"{slugify(name)}_{int(time.time())}.raw"
    filepath = os.path.join(output_dir, filename)

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(filepath, "wb") as f:
                f.write(response.content)
            logger.info(f"✅ [{name}] fetched and saved to: {filepath}")
            return filepath
        except Exception as e:
            logger.warning(f"⚠️ Attempt {attempt+1} failed for {url}: {e}")
            time.sleep(2)

    logger.error(f"❌ Failed to fetch {name} after {max_retries} attempts.")
    return None


def fetch_all_sources(config, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for source in config.get("sources", []):
        name = source.get("name")
        url = source.get("url")

        if name and url:
            fetch_source(name, url, output_dir)
        else:
            logger.warning(f"⚠️ Invalid config entry: {source}")
