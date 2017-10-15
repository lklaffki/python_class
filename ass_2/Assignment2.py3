## 1. goal: retrive the text and prepare it
### The textual resource was given in a separate file and 
### needs to be loaded and assigned to the variable "orig_text".

f = open("Sapir1921_chapter1.txt")
orig_text = f.read()

### replace the backlashes with whitespaces and assign it to a new variable
text = orig_text.replace("\\"," ")

### stripping the string to delete the first lines of metadata
### how to do that? maybe something with "text.lstrip("INTRODUCTORY")"? cleaned it now manually

## 2. goal: extract the longest sentence
### therefore: split text in sentences
### this is not totally right, the headline will be also counted, 
### should be eliminated, with "isupper"?

lines = text.split(".")

### split the words per sentence
wordsPerLine = [line.split(" ") for line in lines]

### get longest sentence
longest_sen = max(wordsPerLine, key=len)

## the requested output is this:
### to concatenate the string, I used the join-method
print ("The longest sentence in the text is:", ' '.join(longest_sen))


## 3. goal: extract the longest word
### further text cleaning: getting rid of all punctuation marks
word_text = text.replace("--"," ").replace("."," ").replace(","," ").replace(";"," ").replace("\n"," ")

### split the text in words
words = word_text.split(" ")

### reusing the code from getting the longest sentence
longest_word = max(words, key=len)

## the requested output is this (ignoring compound words):
print ("The longest word in the text is:", longest_word)


## 4. goal: extract the top ten of the most frequent words, including their frequency

### setting all upper case letters to lower case to comply with stopwordlist
words_low = [item.lower() for item in words]

### several functions (goal 6) are defined to carry out the task 
### (could be done in separate file for reuse, here included)

### the stopwordlist is opened
f = open("stopwordlist.txt")
stopwordlist = f.read()

### and used later with this function that checks, if word is a stopword and returns it if not
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
### (list of words from the text-source and stopwordlist)
cleanedWords = removeStopWords(words_low, stopwordlist)
dictionary = wordListToDict(cleanedWords)
sortedDict = sortDict(dictionary)

### printing the sortedDict would return the whole content (all words minus the stopwords)
### therefore restricting the output to the first ten word-frequency-pairs
print("The ten most frequent words and their frequencies are:",sortedDict[0:10]) 

## 5. extract named entities
### assumed: "named entities" are written with capital letter such as names or places
### therefore using "words" from lines 36/37 to avoid the necessary modification from line 49

### checking if word begins with capital letter via istitle
### then appending it to a list and sort this

entities = []

for i in words:
	if i.istitle():
		entities.append(i)
entities.sort()

print(entities)	

### closing the calls from line 4 and line 55
f.close()