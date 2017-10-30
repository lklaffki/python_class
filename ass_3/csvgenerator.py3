f_1 = open("Sapir1921_chapter1.txt")
f_2 = open("Muller1861_lecture1.txt")
f_stop = open("stopwordlist.txt")

orig_chapter1 = f_1.read()
orig_chapter2 = f_2.read()

### cleaning of the textfiles
### replace the backlashes and punctuation with whitespaces and assign it to a new variable
text1 = orig_chapter1.replace("\\"," ").replace(","," ").replace(";"," ").replace("\n"," ")
text2 = orig_chapter2.replace("\\"," ").replace(","," ").replace(";"," ").replace("\n"," ")

### how to get rid of the start?

## Task 1: top ten longest sentences, put into a csv file
### splitting texts in sentences
lines1 = text1.split(".")
lines2 = text2.split(".")

print (lines1)

### split the words per sentence
#wordsPerLine1 = [line.split(" ") for line in lines1]
#wordsPerLine2 = [line.split(" ") for line in lines2]

def wordsPerLine(lines):
	for line in lines:
		wordsPerLine = line.split(" ")
		return (wordsPerLine)	

wordsPerLine1 = wordsPerLine(lines1)
wordsPerLine2 = wordsPerLine(lines2)


#use dictionaries!
### count the length (number of words) for each line

def sentLength(wordsPerLine):
	for i in wordsPerLine:
		sentLength = [wordsPerLine.count(p) for p in wordsPerLine]
	return dict(zip(wordsPerLine,sentLength))

def sortDict(dict):
	sortedSent = [(dict[key], key) for key in dict]
	sortedSent.sort()
	sortedSent.reverse()
	return sortedSent


### sentence itself

### chapter

### ranking (longest sentence rank 1)


#header1 = "length", "sentence", "chapter", "ranking\n"
#data1 = ""

#csvString1 = header1 + data1

#fw = open("task1csv.csv", "w+", encoding="utf-8")
#fw.write(csvString1)

## Task 2: top ten most frequent words, put into a csv file
### further text cleaning: getting rid of all punctuation marks
### can this be done better?
#word_text = text.replace("--"," ").replace("."," ").replace(","," ").replace(";"," ").replace("\n"," ")

### split the text in words
#words = word_text.split(" ")

### lower case to count all word occurences, also on the beginning of a sentence
#words = words.lower()

### reuse of the functions from assignment 2
### this function that checks, if word is a stopword and returns it if not
#def removeStopWords(words, stopwords):
#	return [i for i in words if i not in stopwords]

### counting the words each time they appear in the cleaned wordlist
### using a dictionary to store the word-frequency-pair 
#def wordListToDict(words):
#	wordfreq = [words.count(p) for p in words]
#	return dict(zip(words,wordfreq))
    
### another function for the sorting depending on the frequency
### reverse to set the hightest value on top
#def sortDict(dict):
#	sortedWords = [(dict[key], key) for key in dict]
#	sortedWords.sort()
#	sortedWords.reverse()
#	return sortedWords

### calling the three functions defined above with the given parameters 
### (list of words from the text-sources and stopwordlist)
#cleanedWords = removeStopWords(words, stopwordlist)
#dictionary = wordListToDict(cleanedWords)
#sortedDict = sortDict(dictionary)

### keyword (word itself)

### frequency

### length (number of characters)

### chapter

#header2 = "keyword", "frequency", "length", "chapter\n"
#data2 = ""

#csvString2 = header2 + data2

#fw = open("task2csv.csv", "w+", encoding="utf-8")
#fw.write(csvString2)

### closing all opened files 
#f.close()