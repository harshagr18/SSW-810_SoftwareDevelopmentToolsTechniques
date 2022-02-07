import random

if __name__ == "__main__":
    print("Please run the wordle applcation.")

def createWordList():
    f = open("words.txt", "r")
    data = f.read().split("\n")
    words = []
    for j in data:
        if len(j) == 5: # There are 1379, 5 letter words
            words.append(j)

    return words


def randomWord(): # Generate a random word for solution
    words = createWordList()

    solution = list(words[random.randint(0, 1378)].upper())
    return solution

def checkWord(word):
    words = createWordList()
    
    if word.lower() in words:
        return True
    else:
        return False