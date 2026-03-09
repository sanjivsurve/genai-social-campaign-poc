import os
from PIL import Image, ImageDraw
import random
from genai_product_generator import generate_product_image

PRODUCT_FOLDER = "assets/products"
LOGO_FOLDER = "assets/logo"


def _is_image(file):
    return file.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))


def _generate_product_image(product_name):
    """
    Generates a simple placeholder product image using local GenAI logic.
    Saves to PRODUCT_FOLDER as <product_name>1.png
    """

    width = 1024
    height = 1024

    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    color = (
        random.randint(80, 200),
        random.randint(80, 200),
        random.randint(80, 200)
    )

    # simple placeholder "shoe-like" shape
    draw.rounded_rectangle(
        (200, 450, 820, 650),
        radius=80,
        fill=color
    )

    filename = f"{product_name}1.png"

    path = os.path.join(PRODUCT_FOLDER, filename)

    img.save(path)

    print(f"Generated product asset: {path}")

    return path


def load_products(product_name=None):
    """
    Loads product images as PIL RGBA images.

    Returns:
        list of dict:
        {
            "name": filename_without_ext,
            "image": PIL.Image
        }
    """

    if not os.path.exists(PRODUCT_FOLDER):
        os.makedirs(PRODUCT_FOLDER)

    files = sorted(os.listdir(PRODUCT_FOLDER))

    assets = []

    # look for files starting with product name
    for f in files:

        if not _is_image(f):
            continue

        if product_name and not f.lower().startswith(product_name.lower()):
            continue

        path = os.path.join(PRODUCT_FOLDER, f)

        try:

            img = Image.open(path).convert("RGBA")

            name = os.path.splitext(f)[0]

            assets.append(
                {
                    "name": name,
                    "image": img
                }
            )

        except Exception as e:

            print(f"Skipping asset {f}: {e}")

    # If no matching assets → generate one
    if not assets and product_name:

        print(f"No product assets found for '{product_name}'. Generating using local GenAI...")

        generated_path = generate_product_image(product_name)

        try:

            img = Image.open(generated_path).convert("RGBA")

            name = os.path.splitext(os.path.basename(generated_path))[0]

            assets.append(
                {
                    "name": name,
                    "image": img
                }
            )

        except Exception as e:

            print(f"Failed to load generated asset: {e}")

    return assets


def load_logo():
    """
    Loads brand logo.
    """

    if not os.path.exists(LOGO_FOLDER):
        return None

    for f in os.listdir(LOGO_FOLDER):

        if _is_image(f):

            path = os.path.join(LOGO_FOLDER, f)

            try:

                logo = Image.open(path).convert("RGBA")

                return logo

            except Exception as e:

                print(f"Failed to load logo {f}: {e}")

    return None