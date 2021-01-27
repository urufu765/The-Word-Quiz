"""
Name : Jason
Program : The Word Quiz
Filename : The Word Quiz.py
Date : 2018/09/14
Version : 0.3
"""
"""Changelog
0.1: Project started, and added introduction
0.2: Lists added with random word picker
0.3: Words are associated with functions
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
    Round = True
    if Stage == 1:
        Randomizer = random.randint(0, 4)
        while Round is True:
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
    elif Stage == 2:
        Randomizer = random.randint(0, 4)
        while Round is True:
            if LIST2[Randomizer] == "Brick":
                print("Alright, this word is five letters!")
            elif LIST2[Randomizer] == "Terrain":
                print("Alright, this word is seven letters!")
            elif LIST2[Randomizer] == "Maze":
                print("Alright, this word is four letters!")
            elif LIST2[Randomizer] == "Screen":
                print("Alright, this word is six letters!")
            elif LIST2[Randomizer] == "Blinds":
                print("Alright, this word is six letters!")
    elif Stage == 3:
        Randomizer = random.randint(0, 4)
        while Round is True:
            if LIST3[Randomizer] == "Dinosaur":
                print("Alright, this word is eight letters!")
            elif LIST3[Randomizer] == "Computer":
                print("Alright, this word is eight letters!")
            elif LIST3[Randomizer] == "Library":
                print("Alright, this word is eight letters!")
            elif LIST3[Randomizer] == "Uranium":
                print("Alright, this word is seven letters!")
            elif LIST3[Randomizer] == "Rubber":
                print("Alright, this word is six letters!")
