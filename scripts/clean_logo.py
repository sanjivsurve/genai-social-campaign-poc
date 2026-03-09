import os
from PIL import Image
import numpy as np


INPUT_PATH = "assets/logo.png"
OUTPUT_PATH = "assets/logo_clean.png"


def remove_white_background(image, threshold=240):
    """
    Convert white pixels to transparent.
    Keeps dark logo pixels intact.
    """

    img = np.array(image)

    r = img[:, :, 0].astype(int)
    g = img[:, :, 1].astype(int)
    b = img[:, :, 2].astype(int)

    alpha = np.ones_like(r) * 255

    mask = (r > threshold) & (g > threshold) & (b > threshold)

    alpha[mask] = 0

    img = np.dstack([r, g, b, alpha])

    return Image.fromarray(img.astype("uint8"), "RGBA")


def clean_logo():

    img = Image.open(INPUT_PATH).convert("RGB")

    cleaned = remove_white_background(img)

    cleaned.save(OUTPUT_PATH)

    print(f"Saved cleaned logo -> {OUTPUT_PATH}")


if __name__ == "__main__":
    clean_logo()