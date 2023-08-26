'''
Samantha Ho
Project 3: Anagrams
'''

# opening the text file and storing as list of strings 
def openFile():
    f = input("File name: ")
    textFile = open(f)
    for ln in textFile:
        return ln.split()
    
#Getting rid of punctuation --> turns into string 
def noPunctuation(name):
    punct = "!.[]{};:@#$%^&,'*(?)_-+=\|"
    for char in name:
        if char in punct:
            name = name.replace(char, "")
    return name
   
#creates dictionary of "alphabetical key"
def makeDictionary(listInput):
    dictionary = {}
    for word in listInput:
        word = word.lower()
        word2 = noPunctuation(word)
        key = "".join(sorted(word2)) 
        if key in dictionary.keys():
            dictionary[key].append(word2)
        else:
            dictionary[key] = [word2]
    return dictionary

# removes duplicate words
def removeDuplicates(words):
    s = set(words)
    l = list(s)
    return l

#all anagram function - prints all unique anagrams sets
def allAnagrams(dictionary):
    for words in dictionary.values():
        newWords = removeDuplicates(words)
        if len(newWords) >=2:
            print("{}".format(" ".join(newWords)))

# anagrams letterstring - prints all unique anagrams in a text file as string
def anagrams(letterstring, dictionary):
    letterstring.lower()
    letterstring2 = noPunctuation(letterstring)
    nameSorted = sorted(letterstring2) 
    myString = "".join(nameSorted) 
    anagramList = []
    for key in dictionary.keys():
        value = dictionary[key]
        j = removeDuplicates(value)
        dictionary[key] = j
    for word in dictionary:
        if word == myString:
            anagrams = dictionary[word]
            anagramList.append(word)
            print("{}".format(" ".join(anagrams)))
    if len(anagramList) ==0:
        print("No anagrams.")


# count letterstring function - display number of occurrences of letterstring
def count(letterstring, dictionary):
    letterstring.lower()
    letterstring2 = noPunctuation(letterstring)
    nameSorted = sorted(letterstring2)  
    myString = "".join(nameSorted)
    count = 0
    for key in dictionary.keys():
        if key == myString:
            anagrams = dictionary[key]
            count = len(anagrams)
            print(count)
    if count==0:
        print("No anagrams.")
           
# top anagram function - display largest set of unique anagrams 
def top(dictionary):
    for key in dictionary.keys():
        value = dictionary[key]
        j = removeDuplicates(value)
        dictionary[key] = j  
    maxKey = ""
    maxLength = 0
    for key in dictionary:
        keyLength = len(dictionary[key])
        if keyLength > maxLength:
            maxKey = dictionary[key]
            maxLength = keyLength
    maxString = " ".join(maxKey)
    print(maxString)

# master function
def Function():
    x = openFile()
    i = 0
    dictionary = makeDictionary(x)
    print()
    while i>=0: 
        name = input("Command: ")
        try: 
            a,letterstring =name.split(" ")
            if name == "all anagrams":
                allAnagrams(dictionary)
                print()
            elif a == "anagrams":
                anagrams(letterstring, dictionary)
                print()
            elif a == "count":
                count(letterstring, dictionary)
                print()
            elif name == "top anagram":
                
                top(dictionary)
                print()
            else:  
                print("Invalid command.")
                print()
            i+=1
        except ValueError:
            print("Invalid command.")
            print()
    
    
Function()

