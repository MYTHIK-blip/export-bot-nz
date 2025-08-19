# scripts/schedule.py

import time
import argparse
import subprocess
from utils.log import logger

DEFAULT_INTERVAL = 3600  # 1 hour

def run_export():
    logger.info("Triggering export pipeline...")
    subprocess.call(["python", "scripts/export_bot.py"])
    subprocess.call(["python", "scripts/convert_data.py"])

def schedule_loop(interval):
    logger.info(f"Starting schedule loop: every {interval} seconds.")
    while True:
        run_export()
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Schedule data export runs.")
    parser.add_argument("--once", action="store_true", help="Run one-time export.")
    parser.add_argument("--loop", action="store_true", help="Run continuous loop.")
    parser.add_argument("--interval", type=int, default=DEFAULT_INTERVAL,
                        help="Loop interval in seconds (default: 3600)")
    args = parser.parse_args()

    if args.once:
        run_export()
    elif args.loop:
        schedule_loop(args.interval)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
