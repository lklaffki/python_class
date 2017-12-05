from PIL import Image

### triangle with a 90° 

triangle = Image.new ('RGB', (150,150), (0,0,0)) ###black
h=0
### nested loop
for x in range(150):
	for y in range(h):
		triangle.putpixel((x,y),(127,127,127)) ###grey
	h=h+1
triangle.save('triangle.png')



