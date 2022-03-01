######################################
#               Filters              #
#                                    #
#             UTeach CSP             #
#             Brian Ford             #
#                                    #
#              9/23/19               #
#                                    #
######################################

# importing PIL.Image library and os library
from PIL import Image 
from PIL import ImageFilter # Library needed for filters
import os
import math
import random

# Adds two blank lines before output
print("\n\n")

# Deletes old created images if they exist
if os.path.exists("newImage.jpg"):
  os.remove("newImage.jpg")

# Opens image - Local File in repl.it
img = Image.open('image.jpg')

# Rescale image size down, if needed
width = img.width
height = img.height
mwidth = width // 250
mheight = height // 250
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

########################
#        Filters       #
#   Create newImage1   #
#   Create newImage2   #
#   Create newImage3   #
#                      #
#   ENTER CODE BELOW   #
########################


newImage1 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
newImage1 = newImage1.filter(ImageFilter.BLUR)


for i in range(3):
    newImage2 = img.filter(ImageFilter.GaussianBlur(random.randint(0, 100)))


newImage3 = img.filter(ImageFilter.DETAIL)
newImage3 = newImage3.filter(ImageFilter.EDGE_ENHANCE)


###################################

# Combines all images together
def warhol():
  # Creates an all white array that is 4 times the original size
  # to hold placeholders for all four images
  all_pixels = []
  rgb = (255,255,255)
  for i in range(img.width * img.height * 4):
    all_pixels.append(rgb)

  # location indicates current pixel location
  location = 0

  # Cycles through each pixel
  while location < len(new_pixels):
    # Gets the pixel at location in each image
    p = new_pixels[location]
    p1 = new_pixels1[location]
    p2 = new_pixels2[location]
    p3 = new_pixels3[location]
    
    # Finds the value of the correct pixel location for each image
    pos = (location * 2) - (location % img.width)
    pos1 = (location * 2) - (location % img.width) + img.width
    pos2 = (location * 2) - (location % img.width) + (img.height * img.width * 2)
    pos3 = (location * 2) - (location % img.width) + (img.height * img.width * 2) + img.width

    # Assigns the pixels to the correct location in the all_pixels array
    all_pixels[pos] = p
    all_pixels[pos1] = p1
    all_pixels[pos2] = p2
    all_pixels[pos3] = p3

    # move to next pixel in images
    location = location + 1

  # Creates a newImage with a size twice of what it was originally
  newImage = Image.new("RGB", (img.width * 2, img.height * 2))
  # Assigns the pixel values to newImage
  newImage.putdata(all_pixels)
  # Saves the new image file
  newImage.save("newImage.jpg")

# Creates an array of pixels for the original image
pixels = img.getdata()
new_pixels = []
for p in pixels:
  new_pixels.append(p)

# Creates an array of pixels for the first filter image
pixels1 = newImage1.getdata()
new_pixels1 = []
for p in pixels1:
  new_pixels1.append(p)

# Creates an array of pixels for the second filter image
pixels2 = newImage2.getdata()
new_pixels2 = []
for p in pixels2:
  new_pixels2.append(p)
  
# Creates an array of pixels for the third filter image
pixels3 = newImage3.getdata()
new_pixels3 = []
for p in pixels3:
  new_pixels3.append(p)

# Combines all images together
warhol()
