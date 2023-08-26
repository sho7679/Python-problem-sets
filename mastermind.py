'''
Samantha Ho
Project 2: Mastermind
CS 130R
'''

# Check length of input is 4
def checkLength(guessKey):
    if len(str(guessKey)) == 4:
        return True
    print("ERROR -- Guess must be 4 digits.")
    return False 

# Check if input is all numbers
def checkInt(guessKey):
    try:
        int(guessKey)
        return True
    except ValueError:
        print("ERROR -- Contains non-numbers.")
        return False

# Check if input has repeats
def checkRepeats(guessKey):   
    memory = ""
    for char in guessKey:
        if not char in memory:
            memory += char
    if len(memory) == 4:
        return True
    else:
        print("ERROR -- No repeated digits allowed.")
        return False 

#Check all three conditions
def checkInput(guessKey):
    if (checkLength(guessKey) and checkInt(guessKey) and checkRepeats(guessKey)):
        return True
    else:
        print("Please try again.")
        
#Check conditions, then see if input has correct position or exact. Loop 12 times until input is correct or they lose.
#Position = correct number and in right position
#Exist = number in key, but wrong position
def Mastermind():
    i = 0
    realKey = input("What is the key: ")
    while i<12:
        guessKey = input("\nGuess: ")
        correctInput = checkInput(guessKey)
        countExact = 0
        countExist = 0
        if correctInput:
            for c in range(len(guessKey)):
                if guessKey[c] == realKey[c]:
                    countExact +=1
                if guessKey[c] != realKey[c] and guessKey[c] in realKey:
                    countExist +=1
            if countExact != 4:
                print(guessKey + ": " + "position: " + str(countExact) + ", exist: " + str(countExist))
                i+=1
            if countExact ==4:
                print("\nCongrats!\nYou guessed the key: " + str(realKey))
                print("It took you "+ str(i+1) +" tries.")
                return
    print("\nYou lost. \nThe key was " + realKey + ".")
            
Mastermind()    
