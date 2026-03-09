PROHIBITED = ["fake","illegal","scam"]


def brand_check(image_path, brief, logger):

    if "brand_colors" not in brief:
        logger.warning("Brand colors missing from brief")
    else:
        logger.info("Brand colors validated")


def legal_check(text, logger):

    for word in PROHIBITED:

        if word in text.lower():
            logger.warning(f"Prohibited word detected: {word}")