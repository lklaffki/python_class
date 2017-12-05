from PIL import Image
import glob

image_list = []

for filename in glob.glob('/Users/zorbas/Documents/GitHub/python_course/ass_4/img/*'):
	#print (filename)
	im = Image.open(filename)
	image_list.append(im)

size = 128

new_im = Image.new('RGB', (256,256))

x = 0
y = 0

for im in image_list:
	if (x == 256):
		y = y + size
		x = 0
	im.thumbnail((size, size))
	new_im.paste(im, (x,y))
	x = x + size

new_im.save('collage2.png')