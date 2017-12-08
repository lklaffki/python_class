from PIL import Image
# 1. Task: download and extract pictures, done

# 2. Task: open and analyze each image
## open each image
import glob

### lists that are used in the code below are created
image_list = []
resBlue = []
blueImages = []

### with glob, all the files in the directory will be adressed and opened
### using this, there is no need to adress the single files / to know their name
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
### store the value for the average blue, the file and it's name in a list of tupels
	blueImages.append((blueAv, im, filename))


# 3. Task: sorting the images according to the values for blue

### to sort the tuples according to the value of b (first entry), I use the key with a lambda function to tell the programm that only the first is relevant
finalBlue = sorted(blueImages, key=lambda x: x[0])
print(finalBlue)


# 4. Task: create collage from sorted pictures

### first, a new image is created, the size arbitrary that from the original pictures
new_im = Image.new('RGB', (640,480))

### to fit the images into the collage, their size needs to be reduced to a third in heigth and width
width = 213
height = 160

### the starting point for the first picture gets defined; this is where the first image will be pasted
x = 0
y = 0

for im in image_list:
### due to the fact that 640 can't be divided by three, I took the closest integer
### another idea would be to create the new image with 3*width
	if (x == 639):
### when the first row is full / x runs to the limit of the width of the collage's size
### y gets increased with the height of a row (the height of the pictures)
		y = y + height
		x = 0
	im.thumbnail((width, height))
	new_im.paste(im, (x,y))
	x = x + width

### The new image, the collage itself is created.
new_im.save('collage.png')
### This sentence just signals that the program did run through as the image file is created in the file system, not to be seen in the terminal.
print("The requested file has been saved.")