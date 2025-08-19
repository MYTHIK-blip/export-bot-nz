"""
export_bot.py

Master controller for the Export Bot NZ system.
Manages the full pipeline: config ingestion → data fetch → conversion → vaulting → logging.
Designed for offline-first operation with minimal dependencies and full format flexibility.
"""

import os
import sys
import yaml
import time
import logging
from utils.log import setup_logger
from configparser import ConfigParser
from scripts.fetch_sources import fetch_all_sources
from scripts.convert_data import convert_all_data
from utils.format_utils import ensure_dirs

# ────────────────────────────────────────────────────────────────────────────────
# 💡 Setup
# ────────────────────────────────────────────────────────────────────────────────

CONFIG_PATH = "config/sources.yaml"
TAGS_PATH = "config/tags.yaml"
DATA_DIR = "data/raw"
PROCESSED_DIR = "data/processed"
EXPORT_DIR = "data/exports"
VAULT_DIR = "vaults"

logger = setup_logger("ExportBot")

# ────────────────────────────────────────────────────────────────────────────────
# 🚀 Main Pipeline
# ────────────────────────────────────────────────────────────────────────────────

def run_export_pipeline():
    logger.info("💼 Export Bot NZ initialized...")

    # 1. Ensure folders exist
    ensure_dirs([DATA_DIR, PROCESSED_DIR, EXPORT_DIR, VAULT_DIR])

    # 2. Load config
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = yaml.safe_load(f)
        logger.info("✅ Source config loaded.")
    except Exception as e:
        logger.error(f"⚠️ Failed to load config: {e}")
        sys.exit(1)

    # 3. Fetch data
    logger.info("📡 Starting data fetch...")
    fetch_all_sources(config, output_dir=DATA_DIR)

    # 4. Convert/Process data
    logger.info("🧪 Converting and formatting data...")
    convert_all_data(input_dir=DATA_DIR, output_dir=PROCESSED_DIR)

    # 5. Package/Export
    logger.info("📦 Exporting final datasets...")
    from scripts.schedule import export_vaults
    export_vaults(source_dir=PROCESSED_DIR, export_dir=VAULT_DIR)

    logger.info("🏁 Pipeline completed successfully.")


if __name__ == "__main__":
    start = time.time()
    run_export_pipeline()
    logger.info(f"⏱ Total runtime: {round(time.time() - start, 2)} seconds.")
