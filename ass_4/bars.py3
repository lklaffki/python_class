from PIL import Image

### first version
#cat=[100,90,65,96,120]
#rectangle = Image.new ('RGB', (150,150), (0,0,0)) ###black

### nested loop
#for x in range(4):
#	for y in range(cat[x]):
#		rectangle.putpixel((x,y),(127,127,127)) ###grey
#rectangle.save('bars.png')

from PIL import ImageFont
from PIL import ImageDraw

### second version, broader bars with space between
cat=[100,90,65,96,120]
### text in the graphs
nameCat=["a","b","c","d","e"] 
rectangle = Image.new ('RGB', (150,150), (0,0,0)) ###black
for x in range(5):
	for w in range(10):
		for y in range(149,149-cat[x],-1): ### put the graphs upside down
			rectangle.putpixel((x*20+w,y),(127,127,127)) ###grey
### text to the picture
### headline
draw=ImageDraw.Draw(rectangle)
draw.text((0,0), "Sample Text",(255,255,255))
### text for the bars !not finished!
drawLegend=ImageDraw.Draw(rectangle)
for i in range(5):
	### here sequence is needed instead of the arrays, but how?
	drawLegend.text(cat[x],nameCat[x],(255,255,255))
	cat[x]=cat[x]-1
	nameCat[x]=nameCat[x]-1
rectangle.save('bars2.png')

