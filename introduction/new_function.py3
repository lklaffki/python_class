## using module from myModule.py here in a new function
## "import calSum, calAvg" OR "*"" (all functions)

from myModule import *
myWords=["Hey!", "i'm", "using", "external", "functions"]
a=(calSum(myWords))
b=calAvg(a,float(len(myWords)))
print (b)


def calSum(a):
	mySumOfItems=0
	for i in a:
		mySumOfItems=mySumOfItems+ len(i)
	return mySumOfItems

def calAvg(c,d):
	r=c/d
	return(r)