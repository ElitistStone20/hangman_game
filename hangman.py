# Callum Gill, 05/12/17, Python 3.6.1
import numpy as np
import random
# Welcome function to wlecome the new guy to the game!
def welcome():
    name = input("Welcome person, what is your name? ")
    print("Hello", name, " welcome to the game where you will be drastically humiliated infront of your peers, enjoy! :}")
# gets a random word from a list of words
def ranWord():
    words = ["asshole", "dickhead", "stuff", "house", "person", "thing", "adventure", "array", "ship"]
    word = random.choice(words)
    return word.lower()
# main function of the game
def guess(word, dash):
    win = 0
    lives = 5
    while win == 0:
        if "_" not in dash:
            print("Somehow you won!")
            win = 1
        elif lives == 0:
            print("you lost")
            break
        else:
            choice = (input("Have guess then: ")).lower()
            if choice in word:
                # use a enumerate method to find all instances of a dashes and replace with letters
                charIndex = [i for i, x in enumerate(word) if x == choice]
                for i in charIndex:
                    dash[i] = choice
            else:
                print("Wrong choice")
                lives = lives - 1
                print("remianing lives ", lives)
            print(dash)
# prints word in form of dashes so the user  can start guessing
def screen(word):
    dash = []
    dash = dash
    for i in word:
        dash.append("_")
    print(dash)
    return dash

def runGame():
    welcome()
    word = ranWord()
    dash = screen(word)
    guess(word, dash)
runGame()
