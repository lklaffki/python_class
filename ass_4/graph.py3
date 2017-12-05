from PIL import Image
### reactangle, in this case a square

rectangle = Image.new ('RGB', (150,150), (0,0,0)) ###black
### nested loop
for x in range(150):
	for y in range(150):
		rectangle.putpixel((x,y),(127,127,127)) ###grey
rectangle.save('rectangle.png')