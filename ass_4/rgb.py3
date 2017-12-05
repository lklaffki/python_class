from PIL import Image

im = Image.open('/Users/zorbas/Documents/GitHub/python_course/ass_4/test.png')

width = im.size[0]
height = im.size[1]

print(width, 'x', height, '=', width*height)

new_im = Image.new('RGB', (width*height, 300), (255, 255, 255))

x = 0
for i in range(0, height):
	for j in range(0, width):
		r, g, b = im.getpixel((j, i))

		new_im.putpixel((x, 290 - r), (255, 0, 0))
		new_im.putpixel((x, 290 - g), (0, 255, 0))
		new_im.putpixel((x, 290 - b), (0, 0, 255))

		x = x + 1

new_im.save('rgb.png')
