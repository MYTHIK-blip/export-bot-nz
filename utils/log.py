# utils/log.py

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("data/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "export_bot.log"

logger = logging.getLogger("ExportBot")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_format = logging.Formatter("[%(levelname)s] %(message)s")
console_handler.setFormatter(console_format)

# File handler (rotates at 1MB, keeps 3 backups)
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
file_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(file_format)

# Attach handlers if not already present
if not logger.hasHandlers():
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
