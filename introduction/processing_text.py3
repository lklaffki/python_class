f=open("four_sentences.txt")
text = f.read()

#lines = 0
#words = 0

#for line in text:
#	#if line==".":
#		lines=lines+1
#		words=words+1
#	if line==" ":
#		words=words+1
#characters=len(text)
#print ("number of lines", lines)
#print ("number of words", words)
#print ("number of characters", characters)

## same result, shorter way
## 5 lines, because empty cell after last punctuation markt; therefore -1
lines=text.split(".")
print ("number of lines", len (lines)-1)
words=text.split(" ") + text.split(".")
print ("number of words", len (words)-2)
print ("number of characters", len (text))