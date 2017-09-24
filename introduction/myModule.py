## definition of function with parameters (a,b)
## zwo steps in one function
#def calSum(a,b):
#	x=a
#	y=b
	## this will calculate the sum
	#z=x+y
	## this will calculate an average
#	z=(x+y)/2
#	print (z)

## splitting up in two funtctions
#def calSum(a,b):
#	x=a
#	y=b
#	z=(x+y)
#	return (z)

#def calAvg(c,d):
#	r=c/d
#	return(r)


## calling of the function with two values for the parameters
#mySum=calSum(2,3)
#myAvg=calAvg(mySum,2)
#print (myAvg)

## function should not exceed 10-15 lines of code

## functions can calculate lists:

#def calSum(a):
#	mySumOfItems=0
#	for i in a:
#		mySumOfItems=mySumOfItems+i
#	return mySumOfItems

#def calAvg(c,d):
#	r=c/d
#	return(r)

#myList=[5,7,9,3]
#mySum=calSum(myList)
#myAvg=calAvg(mySum,len(myList))
#print (myAvg)

## average length of words

def calSum(a):
	mySumOfItems=0
	for i in a:
		mySumOfItems=mySumOfItems+ len(i)
	return mySumOfItems

def calAvg(c,d):
	r=c/d
	return(r)

#myList=["I", "like", "Python", "Three"]
#mySum=calSum(myList)
#myAvg=calAvg(mySum,len(myList))
#print (myAvg)

