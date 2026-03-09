import os
from PIL import Image

from asset_manager import load_products
from image_generator import generate_background
from overlay_engine import compose_creative
from compliance import brand_check, legal_check


ASPECT_RATIOS = {
    "1x1": (1080,1080),
    "9x16": (1080,1920),
    "16x9": (1920,1080)
}

OUTPUT_DIR = "outputs"


def normalize_regions(brief):

    if "regions" in brief:
        return brief["regions"]

    if "region" in brief:
        return [
            {
                "name": brief["region"],
                "campaign_message": brief.get("campaign_message",""),
                "cta": brief.get("cta","Shop Now"),
                "culture": {}
            }
        ]

    raise ValueError("Campaign brief missing region info")


def get_brand_colors(brief):

    colors = brief.get("brand_colors", {})

    return {
        "primary": colors.get("primary", "#000000"),
        "secondary": colors.get("secondary", "#ffffff")
    }


def resolve_product(product, index):

    """
    Converts different product formats into
    (product_name, product_img_path_or_image)
    """

    if isinstance(product, dict):

        name = product.get("name", f"product_{index}")
        image = product.get("image")

        return name, image

    if isinstance(product, str):

        name = os.path.splitext(os.path.basename(product))[0]
        return name, product

    if isinstance(product, Image.Image):

        return f"product_{index}", product

    return None, None


def run_campaign(brief, logger):

    brand_colors = get_brand_colors(brief)

    regions = normalize_regions(brief)

    products = load_products(brief["product"])

    if not products:
        logger.error("No product assets found")
        return

    logger.info(f"Found {len(products)} product assets")

    logo_path = os.path.join("assets","logo_clean.png")

    if not os.path.exists(logo_path):
        logger.error("Missing logo file")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    total = 0

    for region in regions:

        region_name = region["name"].lower()
        message = region.get("campaign_message","")
        cta = region.get("cta","Shop Now")
        culture = region.get("culture",{})

        logger.info(f"Generating creatives for region: {region_name}")

        for i, product in enumerate(products):

            product_name, product_img = resolve_product(product, i)

            if product_img is None:
                logger.error(f"Invalid product asset: {product}")
                continue

            if isinstance(product_img, str) and not os.path.exists(product_img):
                logger.error(f"Missing product image: {product_img}")
                continue

            for ratio, size in ASPECT_RATIOS.items():

                try:

                    scene = generate_background(size, culture)

                    final = compose_creative(
                        scene,
                        product_img,
                        logo_path,
                        message,
                        brand_colors,
                        cta,
                        culture
                    )

                    filename = f"creative_{region_name}_{product_name}_{ratio}.png"

                    outfile = os.path.join(OUTPUT_DIR, filename)

                    final.save(outfile)

                    brand_check(outfile, brief, logger)
                    legal_check(message, logger)

                    logger.info(f"Saved -> {outfile}")

                    total += 1

                except Exception as e:

                    logger.error(f"Creative generation failed: {e}")

    logger.info(f"Campaign generation finished | Total creatives: {total}")