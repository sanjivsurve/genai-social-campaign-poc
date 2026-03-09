from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def clean_logo_background(logo_img):
    """
    Remove white background but keep logo colors intact.
    """

    logo = logo_img.convert("RGBA")
    datas = logo.getdata()

    new_data = []

    for r, g, b, a in datas:

        # detect near-white pixels
        if r > 240 and g > 240 and b > 240:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append((r, g, b, a))

    logo.putdata(new_data)

    return logo


def choose_text_color(background):

    small = background.resize((50, 50)).convert("L")
    brightness = sum(small.getdata()) / (50 * 50)

    if brightness > 140:
        return (20, 20, 20)
    else:
        return (255, 255, 255)


def load_font(size):

    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()


def fit_text(draw, text, max_width, base_size):
    """
    Reduce font size until text fits canvas width.
    """

    font_size = base_size

    while font_size > 20:

        font = load_font(font_size)

        if draw.textlength(text, font=font) <= max_width:
            return font

        font_size -= 2

    return load_font(font_size)

def compose_creative(
        background,
        product_path,
        logo_path,
        message,
        brand_colors,
        cta,
        culture):

    img = background.copy()
    draw = ImageDraw.Draw(img)

    width, height = img.size

    # -----------------------------
    # BRAND HEADER BAR
    # -----------------------------

    header_h = int(height * 0.08)

    brand_color = brand_colors.get("primary", "#000000")

    draw.rectangle(
        [0, 0, width, header_h],
        fill=brand_color
    )

    # -----------------------------
    # LOAD LOGO
    # -----------------------------

    if isinstance(logo_path, Image.Image):
        logo = logo_path.convert("RGBA")
    else:
        logo = Image.open(logo_path).convert("RGBA")
    
    logo_w = int(width * 0.12)
    logo_h = int(logo.height * (logo_w / logo.width))

    logo = logo.resize((logo_w, logo_h))

    img.paste(logo, (30, int(header_h/2 - logo_h/2)), logo)

    # -----------------------------
    # LOAD PRODUCT
    # -----------------------------

    # Load product image safely
    if isinstance(product_path, Image.Image):
        product = product_path.convert("RGBA")
    else:
        product = Image.open(product_path).convert("RGBA")

    prod_w = int(width * 0.30)
    prod_h = int(product.height * (prod_w / product.width))

    product = product.resize((prod_w, prod_h))

    px = int(width/2 - prod_w/2)
    py = int(height * 0.45)

    # -----------------------------
    # SHOE GLOW EFFECT
    # -----------------------------

    glow = Image.new("RGBA", img.size, (0,0,0,0))

    glow_draw = ImageDraw.Draw(glow)

    glow_draw.ellipse(
        [
            px - 40,
            py - 40,
            px + prod_w + 40,
            py + prod_h + 40
        ],
        fill=(255,255,255,90)
    )

    glow = glow.filter(ImageFilter.GaussianBlur(40))

    img = Image.alpha_composite(img.convert("RGBA"), glow)

    img.paste(product, (px, py), product)

    draw = ImageDraw.Draw(img)

    # -----------------------------
    # TEXT SIZES (RESPONSIVE)
    # -----------------------------

    title_size = int(width * 0.045)
    cta_size = int(width * 0.06)
    chant_size = int(width * 0.04)

    try:
        font_title = ImageFont.truetype("arial.ttf", title_size)
        font_cta = ImageFont.truetype("arial.ttf", cta_size)
        font_chant = ImageFont.truetype("arial.ttf", chant_size)
    except:
        font_title = ImageFont.load_default()
        font_cta = ImageFont.load_default()
        font_chant = ImageFont.load_default()

    # -----------------------------
    # MAIN MESSAGE
    # -----------------------------

    bbox = draw.textbbox((0,0), message, font=font_title)
    tw = bbox[2]-bbox[0]

    draw.text(
        (width/2 - tw/2, height*0.18),
        message,
        fill="white",
        font=font_title
    )

    # -----------------------------
    # CTA
    # -----------------------------

    bbox = draw.textbbox((0,0), cta, font=font_cta)
    tw = bbox[2]-bbox[0]

    draw.text(
        (width/2 - tw/2, height*0.30),
        cta,
        fill="white",
        font=font_cta
    )

    # -----------------------------
    # CULTURE CHANT
    # -----------------------------

    chant = culture.get("chant", "")

    bbox = draw.textbbox((0,0), chant, font=font_chant)
    tw = bbox[2]-bbox[0]

    draw.text(
        (width/2 - tw/2, height*0.88),
        chant,
        fill="white",
        font=font_chant
    )

    return img