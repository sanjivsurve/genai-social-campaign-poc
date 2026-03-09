import cv2
import numpy as np
from PIL import Image


def remove_background(image_path, output_path, threshold=240):
    """
    Removes white/light background and converts image to transparent PNG.
    Also crops extra padding.
    """

    # Load image
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Create mask for white background
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mask = gray < threshold
    mask = mask.astype(np.uint8) * 255

    # Clean mask with morphology
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    # Create RGBA image
    rgba = np.dstack((img_rgb, mask))

    # Convert to PIL
    pil_img = Image.fromarray(rgba)

    # Auto-crop transparent borders
    bbox = pil_img.getbbox()
    if bbox:
        pil_img = pil_img.crop(bbox)

    # Save
    pil_img.save(output_path)

    print(f"Saved transparent image -> {output_path}")


if __name__ == "__main__":

    # Example usage
    remove_background("logo.png", "logo_clean.png")
    remove_background("shoes1.png", "shoes1_clean.png")
    remove_background("shoes2.png", "shoes2_clean.png")