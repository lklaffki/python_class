text="The tile on the roof is loose. The water in the pool is cool. Can the root hold the plant in loose soil? See you soon in the afternoon."
#print (len (text))
f=0
for i in range(0, len(text)-1,1):
	if text[i]==text[i+1]:
		f=f+1
print ("The same pair of letters appears", f, "times")
