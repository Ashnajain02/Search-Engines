Ashna Jain
CS 446 - Project 1
 
 AB Breakdown: 
    -Part A (1 - Tokenization): in project1.py lines 9 - 46
    -Part A (2 - Stopwords): in project1.py lines 48 - 66
    -Part A (3 - Stemming): in project1.py lines 68 - 158
    -Part B: in project1.py lines 160 - 165

Description:
    - For this project I created function for all the individual steps. 
    To start with tokenization, I started with making all the text lowercase. Then I replaces any titles such as Mr. and Mrs. 
    with their corresponding tokenized versions. Then since at this point my data was coming straight from the text file,
    I was able to parse through each character and check to see if any of the letters were special characters by seeing if they were not
    in my own predefined alphabet of allowed characters. If it was a special character I removed it bu replacing it with an empty space.
    I then went used then .replace() function to replace apotropes and periods that were all the end of sentences. 
    After this point, I split up all the data in the text file based on spaces so that all the words were stored in an array instead.
    I then passed this array into a function called removePeriods(). 
    - removePeriods() takes in a array of words and for each words checks if the word contains a period or not, 
    if it does, then it counts the number of occurances of the period. If the period is equal to the number of letters in the word, 
    then we know that the word is an abreviation in the form "X.Y.Z.", and we can replace the periods with an empty space.
    Otherwise, if the period is not equal to the number of letters, then we search for the index of the last period using rfind() 
    and then remove from the word and insert the suffix as its own word in the array.
    At the very end, we replace all the remaining periods with empty space as we know that at these places we
    do not need to create a new line.
    
    -Next for stopwords, I simply created a set with all the stopwords, and the had an array that appened the words from data 
    that were not in the stopwords set.

    -For stemming, I split up the 2 parts of porter stemming into partA and partB.
    In part A, I simply checked if the end of the words in the data were equal to any of special endings. 
    To check I simply used negative indexing function in python. Since we only apply only rule at a time, I set all my statements as elif.
    For any cases where I had to check if a substring of a word had a vowel, I employed the any function to check if any part of a specified word
    contain a letter from a set I made called vowels that contains all the vowel characters.

    -For partB of porter stemming process, I once again used negative indexing to check to see the endings matched.
    I wrote a function called addE that would essentially check if any of the conditions were met in that would result in 
    an "e" being added to the end of the string. If checked of any vowels were in the first part of the word,
    checked if the last 2 letters were any of the special endings, and then check if the word is short.

    -For checking if thw word is short, they way I went about it was by frist writing a function smoosh(word), that would take in a word
    and first replace all the letters in the word with either a V or a C. Then using recursion, I remove any cinsecutive duplicates from the string 
    of VC characters. Then I have a function that takes the smooshed word and checking if there a sequence of VC followed 
    by only V. If so, it returns true.

    -In partB of the project, to get the top most frequent words, I used the collections library
    and the counter fucnction to return a diction with all the words and their frequencies.
    Then I used the most common function to retrieve the top 300 values.

Libraries:
    -Collection library 

Dependencies:
    -Python 3:
    -MatplotLib:
        -Using pip:
        python -m pip install -U pip
        python -m pip install matplotlib

Running + Building:
    -After directing to the appropiate folder, type "python project1.py" into terminal
        -After doing this, tokenized-A.txt, tokenized-B.txt and terms-B.txt should now be
        visible in the folder

    