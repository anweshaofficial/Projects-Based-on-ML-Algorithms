#Image Manipulations 

from PIL import Image 
#Pillow Library 

image = Image.open("/Users/anweshasen/Documents/logo.png")

rotated_image = image.rotate(90)
rotated_image.show()

cropped_image = image.crop((128,189,228,299))
cropped_image.show()

image.paste(cropped_image, (120,120))
image.show()

# Test cases
assert image.size == rotated_image.size

