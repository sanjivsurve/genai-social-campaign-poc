import os
import torch
from diffusers import StableDiffusionXLPipeline
from PIL import Image

PRODUCT_FOLDER = "assets/products"

pipe = None


def load_model():
    global pipe

    if pipe is not None:
        return pipe

    print("Loading SDXL model locally...")

    pipe = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        use_safetensors=True
    )

    if torch.cuda.is_available():
        pipe = pipe.to("cuda")

    return pipe


def remove_background(img):
    """
    Simple background removal to create transparency.
    """
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:

        # remove near white background
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255,255,255,0))
        else:
            newData.append(item)

    img.putdata(newData)

    return img


def generate_product_image(product_name):

    if not os.path.exists(PRODUCT_FOLDER):
        os.makedirs(PRODUCT_FOLDER)

    pipe = load_model()

    prompt = f"""
    high quality studio product photograph of {product_name},
    isolated product shot,
    clean lighting,
    centered,
    plain white background,
    commercial advertising photography,
    ultra realistic
    """

    negative_prompt = """
    blurry, low quality, watermark, text, logo, distorted, multiple shoes
    """

    print(f"Generating product with SDXL: {product_name}")

    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=30,
        guidance_scale=7.5,
        height=1024,
        width=1024
    ).images[0]

    image = remove_background(image)

    filename = f"{product_name}1.png"
    path = os.path.join(PRODUCT_FOLDER, filename)

    image.save(path)

    print(f"Generated asset saved to {path}")

    return path