import os
from rembg import remove
from PIL import Image


INPUT_DIR = "assets/products"
OUTPUT_DIR = "assets/products"

SUPPORTED = (".png", ".jpg", ".jpeg")


def clean_image(path):
    img = Image.open(path).convert("RGBA")

    # Remove background using rembg AI model
    output = remove(img)

    return output


def process_products():
    for file in os.listdir(INPUT_DIR):

        if not file.lower().endswith(SUPPORTED):
            continue

        path = os.path.join(INPUT_DIR, file)

        name, ext = os.path.splitext(file)
        out_path = os.path.join(OUTPUT_DIR, f"{name}_clean.png")

        try:

            cleaned = clean_image(path)

            cleaned.save(out_path)

            print(f"Saved: {out_path}")

        except Exception as e:

            print(f"Failed processing {file}: {e}")


if __name__ == "__main__":

    process_products()