print("*******************")
print("Welcome to wordle")
print("*******************")
print()
print("Correct letters in correct positions will have a '+' under them, correct letters in incorrect positions will have a '^' under them and incorrect letters will have '-' under them.")
print("You will have 6 guesses.")
print()

solution = list("heart")
attempts = 6
attemptList = []

while True:
    if(attempts == 0):
        print("Sorry, you lose. Better luck next time")
        print()
        break
    flag = 0
    result = ["","","","",""]
    search = ["0","0","0","0","0"]
    pos = 0
    print("This is attempt number ",(7-attempts))
    print()
    while True:
        userInput = list(input().lower())    

        if(len(userInput) == 5):
            if("".join(userInput) not in attemptList):
                break
            else:
                print("Word has been tried before. (Please retry)")
        else:
            print("Word length is not 5. (Please retry)")
    
    attemptList.append("".join(userInput))
    
    for i in range(5):
        if(userInput[i] == solution[i]):
            count = count - 1
            flag = flag + 1
            result[i] = ("+ ")
            search[i] = 1

    for i in range(5):
        if(userInput[i] in solution and result[i] == ""):
            pos = "".join(solution).find(userInput[i])
            if(search[pos] == 1):
                result[i] = ("- ")
            else:
                result[i] = ("^ ")
                search[pos] = 1
        elif result[i] == "":
            result[i] = ("- ")

    print(" ".join(userInput))
    print("".join(result))
    print()
    if(flag == 5):
        print("Congratulations! You win.")
        break
    attempts = attempts-1