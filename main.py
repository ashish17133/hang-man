# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from word import words
import random
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def getRandomWord(words):
    randomWord=random.choice(words)
    print(randomWord)
    while randomWord == " " or randomWord=="_" :
        randomWord=random.choice(words)
    return randomWord



def hangMan():
    randomWord=getRandomWord(words)
    randomWordSets=set(randomWord)
    print(randomWord)
    while True:
        userGuessWord=input("Enter your Guess word: ")
        if userGuessWord in randomWordSets:
            print("Perfect Guess!! one step closer to win.")
            randomWordSets.remove(userGuessWord)
            if(len(randomWordSets)==0):
                print("You won the game congrats!!Hurry!!")
                return False
        else:
            print("Wrong!! Try again another word.")




if __name__ == '__main__':
    hangMan()
