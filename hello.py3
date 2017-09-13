# this program prints the last character of a
a="Hello World!"
#b=len(a)
#print (a[b-1])
# this program prints the first five characters of a, using for-loop
myText=""
myCounter=0
while myCounter<5:
	if myCounter==1:
		myText=myText + "#" +a[myCounter]
	else:
		myText=myText +a[myCounter]
	myCounter=myCounter+1
print myText
