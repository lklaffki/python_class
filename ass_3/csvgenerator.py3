f_1 = open("Sapir1921_chapter1.txt")
f_2 = open("Muller1861_lecture1.txt")

orig_chapter1 = f_1.read()
orig_chapter2 = f_2.read()

### cleaning of the textfiles
### would be more efficient with regular expressions
### replace the backlashes and punctuation with whitespaces and assign it to a new variable
text1 = orig_chapter1.replace("\\"," ").replace(","," ").replace(";"," ").replace("\n"," ").replace("?",".").replace("!",".").replace("--"," ")
text2 = orig_chapter2.replace("\\"," ").replace(","," ").replace(";"," ").replace("\n"," ").replace("?",".").replace("!",".").replace("--"," ").replace("u8208"," ")


## Task 1: top ten longest sentences, put into a csv file with length, sentence itself, chapter and ranking

### creating the csv file
header1 = "length, sentence, chapter, ranking\n"
data1 = ""

### splitting texts in sentences
lines1 = text1.split(".")
lines2 = text2.split(".")

### split the words per sentence and create a list of lists
wordsPerLine1 = [line.split(" ") for line in lines1]
wordsPerLine2 = [line.split(" ") for line in lines2]

### creating data
for i in range(len(wordsPerLine1)):
 	data1 = data1 + str(len(wordsPerLine1[i])) + "," + str(' '.join(wordsPerLine1[i])) + ",1\n"
 	
for m in range(len(wordsPerLine2)):
  	data1 = data1 + str(len(wordsPerLine2[m])) + "," + str(' '.join(wordsPerLine2[m])) + ",2\n"

csvString1 = header1 + data1 

### writing the csv file
fw = open("task1csv.csv", "w+")
fw.write(csvString1)


## Task 2: top ten most frequent words, put into a csv file

### creating the csv file as shown in video 
### could not store the data in it, so resumed to another way to wrtie csv
#header2 = "keyword, frequency, length, chapter\n"
#data2 = ""


words1 = text1.replace("."," ").split(" ")
words2 = text2.replace("."," ").split(" ")

### lower case to count all word occurences, also on the beginning of a sentence
words1_low = [item.lower () for item in words1]
words2_low = [item.lower () for item in words2]

### reuse of functions from assignment 2
### this function checks, if word is a stopword and returns it if not
def removeStopWords(words, stopwords):
	return [i for i in words if i not in stopwords]

### counting the words each time they appear in the cleaned wordlist
### using a dictionary to store the word-frequency-pair 
def wordListToDict(words):
	wordfreq = [words.count(p) for p in words]
	return dict(zip(words,wordfreq))
    
### another function for the sorting depending on the frequency
### reverse to set the highest value on top
def sortDict(dict):
	sortedWords = [(dict[key], key) for key in dict]
	sortedWords.sort()
	sortedWords.reverse()
	return sortedWords

f = open("stopwordlist.txt")
stopwordlist = f.read()

### calling the three functions defined above with the given parameters 
### (list of words from the text-sources and stopwordlist)
cleanedWords1 = removeStopWords(words1_low, stopwordlist)
cleanedWords2 = removeStopWords(words2_low, stopwordlist)

dictionary1 = wordListToDict(cleanedWords1)
dictionary2 = wordListToDict(cleanedWords2)

sortedDict1 = sortDict(dictionary1)
sortedDict2 = sortDict(dictionary2)

### keyword (word itself), frequency, length (number of characters), chapter

result1 = sortedDict1[0:10]
result2 = sortedDict2[0:10]

import csv

item_length1 = len(result1[0])
item_length2 = len(result2[0])

with open("task2csv.csv", "w+") as output:
	file_writer = csv.writer(output)
	file_writer.writerow(["frequency", "keyword", "length", "chapter"])
	for n in range(item_length1):
		file_writer.writerows(result1)
	for m in range(item_length2):
		file_writer.writerows(result2)


# for n in result1:
# 	data2 = data2 + str(result1[0]) + "," + ",1\n"
# 	#data2 = data2 + + ",2\n"

#csvString2 = header2 + data2

#fw = open("task2csv.csv", "w+")
#fw.write(csvString2)

### closing all opened files 
f.close()