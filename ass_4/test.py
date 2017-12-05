from PIL import Image
# 1. Task: download and extract pictures, done

# 2. Task: open and analyze each image
## open each image
import glob

image_list = []


im = Image.open('/Users/zorbas/Documents/GitHub/python_course/ass_4/ass_img/LNU_library.png')
width = im.size[0]
height = im.size[1]
image_list.append(im)
print(image_list)


for x in range (width):
    for y in range (height):
        for z in (image_list):
            rgb  = z.getpixel((x,y))
            resBlue.append(rgb[2])
	    
blue = sorted(resBlue)
print(blue)