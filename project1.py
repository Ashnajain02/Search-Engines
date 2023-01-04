#Ashna Jain
#"https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/"

#total number of words vs total unique words

from collections import Counter
import matplotlib.pyplot as plt

def tokenize(data):
    #last occurance of period -> next line
    #all of punctuation
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890.'"
        data = data.lower()
        data = data.replace("mr. ", "mr").replace("mrs. ", "ms").replace("dr. ", "dr")
        for letter in data: 
            if letter not in alphabet: 
                data = data.replace(letter, " ")
        data = data.replace("'", "").replace(". ", " ")
        data = data.split()
        data = removePeriods(data)
        return data

def removePeriods(data):
    i = 0
    while(i < len(data)):
            if "." in data[i]:
                #print(0)
                periodCount = 0
                for j in range(len(data[i])):
                    if data[i][j] == '.':
                        periodCount = periodCount + 1
                        #print("periodCount: ", periodCount)
                if periodCount == len(data[i])/2:
                    #print("yay")
                    data[i] = data[i].replace(".", "")
                elif periodCount != len(data[i])/2:
                    indexOfLastPeriod = data[i].rfind(".")
                    str = data[i][indexOfLastPeriod+1:]
                    #print(str)
                    data[i] = data[i].removesuffix(str)
                    data.insert(i+1, str)
    
            data[i] = data[i].replace(".", "")
            i = i + 1
            
    return data

def getStopwords():
    with open(r"stopwords.txt", 'r') as file:
        stopwords = file.read()
        stopwords = stopwords.split()
        stopwordsSet = set()

        for word in stopwords:
            stopwordsSet.add(word)

        return stopwordsSet

def stopwords(data):
    stopwordsSet = getStopwords()
 
    no_stop_data = []
    for word in data:
        if word not in stopwordsSet:
            no_stop_data.append(word)
    return no_stop_data

def porterStem1a(data):
    vowels = {"a", "e", "i", "o", "u"}
    for i in range(len(data)):
        if data[i][-4:] == "sses":
            data[i] = data[i][:-2]
        elif data[i][-2:] == "ss" or data[i][-2:] == 'us':
            continue
        elif data[i][-3:] == "ies" or data[i][-3:] == "ied" :
            if len(data[i][:-3]) > 1:
                data[i] = data[i][:-2]
            else:
                data[i] = data[i][:-1]
        #Delete s if the preceding word part contains a vowel not immediately before the s 
        elif data[i][-1] == "s" and any(vowel in data[i][:-2] for vowel in vowels):
        #any(char in vowels for char in data[i][:-1]):
            if(data[i][-2] not in vowels):
                data[i] = data[i][:-1]
    return data

def porterStem1b(data): #feed
    vowels = {"a", "e", "i", "o", "u"}
    for i in range(len(data)):
        if data[i][-3:] == "eed": #or data[i][-5:] == "eedly":
            for x in range(len(data[i][:-3])):
                if data[i][x] in vowels and data[i][x+1] not in vowels:
                    data[i] = data[i][:-1]     
        elif data[i][-5:] == "eedly":
            for x in range(len(data[i][:-5])):
                if data[i][x] in vowels and data[i][x+1] not in vowels:
                    data[i] = data[i][:-3] 
        elif data[i][-2:] == "ed":
            data[i] = addE(data[i], len("ed"))
        elif data[i][-4:] == "edly":
            data[i] = addE(data[i], len("edly"))
        elif data[i][-3:] == "ing":
            data[i] = addE(data[i], len("ing"))
        elif data[i][-5:] == "ingly":
            data[i] = addE(data[i], len("ingly"))
        

    return data

def addE(word, len):
    vowels = {"a", "e", "i", "o", "u"}
    if any(char in vowels for char in word[:-len]): 
        word = word[:-len]
        
    if word[-2:] in ["at", "bl", "iz"]:
        word = word + "e"

    elif word[-2:] in ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", 
    "mm", "oo", "pp", "qq", "rr", "tt", "uu", "vv", "ww", "xx", "yy"]:
        word = word[:-1]

    elif isShort(word):
        word = word + 'e'
    return word


def smoosh(word):
    vowels = {"a", 'e', 'i', 'o', 'u'}
    newWord = ""
    for i in range(len(word)):
        if word[i] in vowels:
            newWord += "V"
        else:
            newWord += "C"

    #print("newWord:" + newWord)
    return removeDuplicates(newWord)

def removeDuplicates(word):
    if len(word) < 2:
        return word
    if word[0] != word[1]:
        return word[0]+removeDuplicates(word[1:])
    return removeDuplicates(word[1:])

 
def isShort(word):
    word = smoosh(word)
    foundVC = False
    i = 0
    while(i < len(word)):
        if(i < len(word) -1 and word[i] == "V" and word[i+1] == "C") and not foundVC:
            foundVC = True
            i = i + 1
        elif(word[i] == "C" and foundVC):
            return False
        i = i + 1
    return foundVC

def top300frequency(data):
    dict = Counter(data)
    top_300 = dict.most_common(300)  
    return top_300       
     
#////////////////////////////////////////////////////////////

with open(r'tokenization-input-part-A.txt', 'r') as file:
    dataA = file.read()   
    dataA = tokenize(dataA)
    dataA = stopwords(dataA)
    dataA = porterStem1a(dataA)
    dataA = porterStem1b(dataA)

with open(r'tokenized-A.txt', 'w') as file:
    #file.write(data)
    for line in dataA:
        file.write(line)
        file.write("\n")

with open(r'tokenization-input-part-B.txt', 'r') as file:
    dataB = file.read()   
    dataB = tokenize(dataB)
    dataB = stopwords(dataB)
    dataB = porterStem1a(dataB)
    dataB = porterStem1b(dataB)

    freq = top300frequency(dataB)

with open(r'tokenized-B.txt', 'w') as file:
    #file.write(data)
    for line in dataB:
        file.write(line)
        file.write("\n")

with open(r'terms-B.txt', 'w') as file:
    for line in freq:
        file.write(str(line))
        file.write("\n")


totalWords = 0
totalUniqueWords = 0
totalWordArr = []
uniqueWordArr = [] 
allWords = set()

for word in dataB:
    if word not in allWords:
        allWords.add(word)
        totalUniqueWords = totalUniqueWords + 1
        uniqueWordArr.append(totalUniqueWords)
    else:
        uniqueWordArr.append(totalUniqueWords)
    
    totalWords = totalWords + 1
    totalWordArr.append(totalWords)

def plotData():
    plt.plot(totalWordArr, uniqueWordArr)
    plt.ylabel('total unique words')
    plt.xlabel('total words')
    plt.title('total unique vs total words')
    #plt.legend()
    plt.show()
    plt.savefig("plot.pdf")

plotData()
print("Text replaced")
