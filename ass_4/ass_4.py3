from PIL import Image
# 1. Task: download and extract pictures, done

# 2. Task: open and analyze each image
## open each image
import glob

image_list = []
resBlue = []

for filename in glob.glob('/Users/zorbas/Documents/GitHub/python_course/ass_4/ass_img/*'):
	im = Image.open(filename)
	image_list.append(im)
	width = im.size[0]
	height = im.size[1]

### adressing each pixel, row by row
	for i in range(0, height):
		for j in range(0, width):
### using "getpixel" to get the value of each pixel adressed with j and i
			b = im.getpixel((j, i))
### appending the third number, which is the value for blue, to a list			
			resBlue.append(b[2])
### calculate the average value for blue
	blueSum = sum(resBlue)
### using //, the floats get converted to integers	
	blueAv = blueSum//(width*height)


	print(blueAv)

## store each value with image in a list

# 3. Task: sorting the images according to the values for blue



## print (output)
#print(sortedBlue)


# 4. Task: create collage


## this needs to change, use the sorted images

new_im = Image.new('RGB', (640,480))

width = 213
height = 160

x = 0
y = 0

for im in image_list:
### due to the fact that 640 can't be divided by three, I took the closest integer
### another idea would be to create the new image with 3*width
	if (x == 639):
		y = y + height
		x = 0
	im.thumbnail((width, height))
	new_im.paste(im, (x,y))
	x = x + width

new_im.save('collage.png')
print("The requested file has been saved.")