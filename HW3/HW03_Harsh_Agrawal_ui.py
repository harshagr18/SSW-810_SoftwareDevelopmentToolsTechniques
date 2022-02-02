def userInputAndCheck(attemptList):
    while True: # Input from user until the correct type of input is provided (size, alphabetic, not previously used)
        userInput = list(input().upper())

        if(len(userInput) == 5):
            if("".join(userInput) not in attemptList):
                if("".join(userInput).isalpha()):
                    break
                else:
                    print("The word contains non alphabetic characters. (Please retry)")
            else:
                print("Word has been tried before. (Please retry)")
        else:
            print("Word length is not 5. (Please retry)")
    return userInput

def checkWin(attempts,flag=0):
    if(attempts == 0): 
        print("Sorry, you lose. Better luck next time")
        print()
        return True
    elif(flag == 5):
        print("Congratulations! You win.")
        print()
        return True
    return False

def printRound(userInput,result):
    print()
    for i in range(5):
        print(userInput[i]+result[i], end = "")
    print()