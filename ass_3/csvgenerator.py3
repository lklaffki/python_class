f_chapter1 = open("Sapir1921_chapter1.txt", encoding="utf-8")
f_chapter2 = open("Muller1861_lecture.txt", encoding="utf-8")
f_stopwordlist = open("stopwordlist.txt", encoding="utf-8")

orig_chapter1 = f.read("Sapir1921_chapter1.txt")
orig_chapter2 = f.read("Muller1861_lecture.txt")

### cleaning of the textfiles
### replace the backlashes with whitespaces and assign it to a new variable
text = orig_text.replace("\\"," ")

### how to get rid of the start?
### how to deal effectively with two texts at once while storing the information?

## Task 1: top ten longest sentences, put into a csv file
### splitting texts in sentences
lines = text.split(".")

### split the words per sentence
wordsPerLine = [line.split(" ") for line in lines]

### length (number of words)
### working with that? gets longest sentence
longest_sen = max(wordsPerLine, key=len)

### sentence itself

### chapter

### ranking (longest sentence rank 1)


header1 = "length", "sentence", "chapter", "ranking\n"
data1 = ""

csvString1 = header1 + data1

fw = open("task1csv.csv", "w+", encoding="utf-8")
fw.write(csvString1)

## Task 2: top ten most frequent words, put into a csv file
### further text cleaning: getting rid of all punctuation marks
### can this be done better?
word_text = text.replace("--"," ").replace("."," ").replace(","," ").replace(";"," ").replace("\n"," ")

### split the text in words
words = word_text.split(" ")

### lower case to count all word occurences, also on the beginning of a sentence
words = words.lower()

### reuse of the functions from assignment 2
### this function that checks, if word is a stopword and returns it if not
def removeStopWords(words, stopwords):
	return [i for i in words if i not in stopwords]

### counting the words each time they appear in the cleaned wordlist
### using a dictionary to store the word-frequency-pair 
def wordListToDict(words):
	wordfreq = [words.count(p) for p in words]
	return dict(zip(words,wordfreq))
    
### another function for the sorting depending on the frequency
### reverse to set the hightest value on top
def sortDict(dict):
	sortedWords = [(dict[key], key) for key in dict]
	sortedWords.sort()
	sortedWords.reverse()
	return sortedWords

### calling the three functions defined above with the given parameters 
### (list of words from the text-sources and stopwordlist)
cleanedWords = removeStopWords(words, stopwordlist)
dictionary = wordListToDict(cleanedWords)
sortedDict = sortDict(dictionary)

### keyword (word itself)

### frequency

### length (number of characters)

### chapter

header2 = "keyword", "frequency", "length", "chapter\n"
data2 = ""

csvString2 = header2 + data2

fw = open("task2csv.csv", "w+", encoding="utf-8")
fw.write(csvString2)

### closing all opened files 
f.close()