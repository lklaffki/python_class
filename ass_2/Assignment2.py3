## 1. goal: retrive the text and prepare it
### The textual resource was given in a separate file and 
### needs to be loaded and assigned to the variable "orig_text".

f = open("Sapir1921_chapter1.txt")
orig_text = f.read()

### replace the backlashes with whitespaces and assign it to a new variable
text = orig_text.replace("\\"," ")

### stripping the string to delete the first lines of metadata
#text.lstrip("INTRODUCTORY")
### how to do that? cleaned it now manually

## 2. goal: extract the longest sentence
### therefore: split text in sentences
### this is not totally right, the headline will be also counted, should be eliminated

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
word_text = text.replace("--"," ").replace("."," ").replace(","," ").replace(";"," ")

### split the text in words
words = word_text.split(" ")

### reusing the code from getting the longest sentence
longest_word = max(words, key=len)

## the requested output is this:
print ("The longest word in the text is:", longest_word)


## 3. goal: extract the top ten of the most frequent words, including their frequency
# s. programming historian for that

## extract named entities

### closing the call from line 4
f.close()