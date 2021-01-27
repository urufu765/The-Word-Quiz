"""
Name : Jason
Program : The Word Quiz
Filename : The Word Quiz.py
Date : 2018/09/14
Version : 0.2
"""
"""Changelog
0.1: Project started, and added introduction
0.2: Lists added with random word picker
"""
import random
Continue = False
Game = True
Stage = int(1)
Progress = input("Hey there! (hint: press enter to continue)")
print("Welcome! I'm Arri the Puzzle Master!")
Progress = input("Recognize me?")
print("Hope you do because it's time for the Word Quiz!")
while Continue is False:
    print("You have to guess three words! But don't worry,")
    print("you're allowed 5 wrong guesses for each word before game over!")
    Understand = input("Understand?")
    if Understand in ["Yes", "YES", "yes", "y", "Y"]:
        Continue = True
    elif Understand in ["No", "NO", "no", "n", "n"]:
        print("I'll repeat myself...")
        print("Welcome to the Word Quiz!")
    else:
        print("Do please say yes or no...")
        print("I'll just repeat myself.")
        print("Welcome to the Word Quiz!")
Progress = input("\nAlright! Let's begin!!!")
LIST1 = ["Dog", "Grey", "Fire", "Cat", "Water"]
LIST2 = ["Brick", "Terrain", "Maze", "Screen", "Blinds"]
LIST3 = ["Dinosaur", "Computer", "Library", "Uranium", "Rubber"]
while Game is True:
    MISS = int(0)
    Randomizer = random.randint(0, 4)
    while Stage == 1:
        if LIST1[Randomizer] == "Dog":
            print("Alright, this word is three letters!")
        elif LIST1[Randomizer] == "Grey":
            print("Alright, this word is four letters!")
        elif LIST1[Randomizer] == "Fire":
            print("Alright, this word is four letters!")
        elif LIST1[Randomizer] == "Cat":
            print("Alright, this word is three letters!")
        elif LIST1[Randomizer] == "Water":
            print("Alright, this word is five letters!")
