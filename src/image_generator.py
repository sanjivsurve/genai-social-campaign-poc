from PIL import Image, ImageDraw


def draw_soccer_field(img):

    draw = ImageDraw.Draw(img)

    w, h = img.size

    field = (34,139,34)
    line = (255,255,255)

    draw.rectangle([0,0,w,h], fill=field)

    # center line
    draw.line([(w/2,0),(w/2,h)], fill=line, width=4)

    # center circle
    r = h*0.12
    draw.ellipse([w/2-r, h/2-r, w/2+r, h/2+r], outline=line, width=4)

    # penalty boxes
    box_w = w*0.18
    box_h = h*0.3

    draw.rectangle([0,h/2-box_h/2,box_w,h/2+box_h/2], outline=line, width=4)
    draw.rectangle([w-box_w,h/2-box_h/2,w,h/2+box_h/2], outline=line, width=4)


def draw_basketball_court(img):

    draw = ImageDraw.Draw(img)

    w, h = img.size

    wood = (210,160,90)
    line = (255,255,255)

    draw.rectangle([0,0,w,h], fill=wood)

    # center line
    draw.line([(w/2,0),(w/2,h)], fill=line, width=4)

    # center circle
    r = h*0.12
    draw.ellipse([w/2-r,h/2-r,w/2+r,h/2+r], outline=line, width=4)

    # free throw arcs
    r2 = h*0.18
    draw.arc([w*0.1,h/2-r2,w*0.1+r2*2,h/2+r2], 270,90, fill=line,width=4)
    draw.arc([w*0.9-r2*2,h/2-r2,w*0.9,h/2+r2], 90,270, fill=line,width=4)


def generate_background(size, culture):

    img = Image.new("RGB", size, (60,110,180))

    sport = culture.get("sport","generic")

    if sport == "soccer":
        draw_soccer_field(img)

    elif sport == "basketball":
        draw_basketball_court(img)

    return img