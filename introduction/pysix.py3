#this program prints some requested letter, 3 times within one run.
for i in range(0,3,1):
	text="The tile on the roof is loose. The water in the pool is cool. Can the root hold the plant in loose soil? See you soon in the afternoon."
	x=float(input("Please enter a number: "))
	x=round(x)
	if x>len(text):
		print ("error...")
	else:
		print (text[x])
