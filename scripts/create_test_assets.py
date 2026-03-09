from PIL import Image, ImageDraw

# Create shoe product image
img = Image.new("RGBA",(800,400),(0,0,0,0))
draw = ImageDraw.Draw(img)

draw.rectangle((100,200,700,300),fill=(0,0,0))
draw.ellipse((650,220,780,300),fill=(255,0,0))
draw.text((300,150),"NIKE SHOES",(255,255,255))

img.save("assets/products/shoes.png")

# Create second shoe variation
img2 = Image.new("RGBA",(800,400),(0,0,0,0))
draw2 = ImageDraw.Draw(img2)

draw2.rectangle((100,200,700,300),fill=(255,255,255))
draw2.ellipse((650,220,780,300),fill=(0,0,0))
draw2.text((280,150),"NIKE RUN",(0,0,0))

img2.save("assets/products/shoes2.png")

# Create logo
logo = Image.new("RGBA",(400,200),(0,0,0,0))
draw3 = ImageDraw.Draw(logo)

draw3.text((80,80),"NIKE",(0,0,0))

logo.save("assets/logo.png")

print("Test assets created.")