import HW03_Harsh_Agrawal_ui as ui


#Pseudocode

"""
SET solution word
WHILE number of attempts run out or user wins
    CHECK if number of attempts remaining are 0
    WHILE input is not 5 letters, unseen word and alphabetic
        TAKE user input
    FOR each letter in the input word
        CHECK if correct letter is in correct position (primary)
    FOR each letter in the input word
        CHECK if correct letter is in incorrect position (secondary)
    CHECK if each letter is guessed correctly (User wins)
"""



#Game Introduction
print()
print("Welcome to wordle")
print()
print("Correct letters in correct positions will have a nothing after them, correct letters in incorrect positions will have a ''' under them and incorrect letters will have '\"' under them.")
print("You will have 6 guesses.")
print()


solution = list("SONAR") # Solution variable
attempts = 6 # Number of attempts allowed
attemptList = [] # Records number of user's tried words

while True: # Runs the loop until number of attempts run out, or the user wins.

    if(ui.checkWin(attempts)):
        break

    flag = 0 # Tracks number of letters rightly guessed in the correct position on each attempt to check if user has one
    result = ["","","","",""] # Assigns space,' or " depending on correct and incorrect letters and positions
    search = ["0","0","0","0","0"] # Used to check if a letter has been used, so same letter doesn't give 2 positive outputs.
    pos = 0 # Used to track the letter that is being used in the actual word to create result
    print("This is attempt number ",(7-attempts)) 
    print()

    userInput = ui.userInputAndCheck(attemptList)

    attemptList.append("".join(userInput))
    
    for i in range(5): # Checking for correct letters in correct positions first, to ensure highest priority
        if(userInput[i] == solution[i]):
            flag = flag + 1
            search[i] = 1
            result[i] = " "

    for i in range(5): # Checking for correct letters in incorrect position and lastly incorrect letters
        if(userInput[i] in solution and result[i] == ""):
            pos = "".join(solution).find(userInput[i])
            if(search[pos] == 1):
                result[i] = ("\"")
            else:
                result[i] = ("'")
                search[pos] = 1
        elif result[i] == "":
            result[i] = ("\"")


    ui.printRound(userInput,result)

    if(ui.checkWin(attempts,flag)):
        break

    attempts = attempts-1