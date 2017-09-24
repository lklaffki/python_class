## this is the provided textual source, assigned to the variable "text"
## alternatively, one could outsource the text in a .txt-file and let it be read
## but because it is rather short, I decided to let it stay in the .py3-file

text="""We have developed speed, but we have shut ourselves in. 
Machinery that gives abundance has left us in want. 
Our knowledge has made us cynical. 
Our cleverness, hard and unkind. 
We think too much and feel too little. 
More than machinery we need humanity. 
More than cleverness we need kindness and gentleness."""

## 1. counting the sentences
lines=text.split(".")
print ("This text contains", len (lines)-1, "sentences.")

## 2. counting the words
words=text.split(" ")
print ("This text contains", len (words), "words.")

## 3. ordering the sentences according to their length (amount of words)
# Wörter pro Satz zählen
#dann sortieren

for i in range(0,7,1):
	text=text 
	print (len(text))



#for lines in range(0,7,1):
#	if lines==".":
#		len(lines).sort()
#		print (lines)

#for line in text:
#	if line==".":
#		print (len(line))


#.sort
#	The second longest sentence in this text contains", len, "words. \
#	The third longest sentence in this text contains", len, "words. \
#	The forth longest sentence in this text contains", len, "words. \
#	The fifth longest sentence in this text contains", len, "words. \
#	The sixth longest sentence in this text contains", len, "words. \
#	The shortest sentence in this text contains", len, "words.")

## 4. ordering the five longest words alphabetically

#print ("The five longest words in the text are in alphabatic order:"
	#)