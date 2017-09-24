## using module from myModule.py here in a new function
## "import calSum, calAvg" OR "*"" (all functions)

from myModule import *
myWords=["Hey!", "i'm", "using", "external", "functions"]
a=(calSum(myWords))
b=calAvg(a,len(myWords))
print (b)