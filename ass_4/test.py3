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
	for i in range(0, height):
		for j in range(0, width):
			b = im.getpixel((j, i))
			resBlue.append(b[2])
	blueSum = sum(resBlue)
	### using //, the floats get converted to integers
	blueAv = blueSum//(width*height)
	
print(image_list)
print(blueAv)


