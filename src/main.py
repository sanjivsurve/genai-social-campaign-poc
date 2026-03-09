import sys
import json
import os

from campaign_engine import run_campaign
from logger import setup_logger


def main():

    if len(sys.argv) < 2:
        print("Usage: python src/main.py campaign.json")
        sys.exit(1)

    brief_file = sys.argv[1]

    if not os.path.exists(brief_file):
        print(f"Campaign file not found: {brief_file}")
        sys.exit(1)

    try:
        with open(brief_file) as f:
            brief = json.load(f)
    except Exception as e:
        print(f"Failed to load campaign JSON: {e}")
        sys.exit(1)

    logger = setup_logger()

    logger.info("Starting campaign generation")

    run_campaign(brief, logger)

    logger.info("Campaign generation finished")


if __name__ == "__main__":
    main()