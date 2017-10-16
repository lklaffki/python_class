f = open("Sapir1921_chapter1.txt","Muller1861_lecture.txt","stopwordlist.txt")
orig_text = f.read()

### cleaning of the textfiles
### replace the backlashes with whitespaces and assign it to a new variable
text = orig_text.replace("\\"," ")

### how to get rid of the start?
### how to deal effectively woth two texts at once while storing the information?

## Task 1: top ten longest sentences, put into a csv file
### splitting texts in sentences
lines = text.split(".")

### split the words per sentence
wordsPerLine = [line.split(" ") for line in lines]

### length (number of words)
### working with that? get longest sentence
longest_sen = max(wordsPerLine, key=len)

### sentence itself

### chapter

### ranking (longest sentence rank 1)




## Task 2: top ten most frequent words, put into a csv file
### further text cleaning: getting rid of all punctuation marks
### can this be done better?
word_text = text.replace("--"," ").replace("."," ").replace(","," ").replace(";"," ").replace("\n"," ")

### split the text in words
words = word_text.split(" ")

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


### closing the calls from line 1 and line 55
f.close()