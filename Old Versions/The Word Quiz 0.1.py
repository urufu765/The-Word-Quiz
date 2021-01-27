"""
Name : Jason
Program : The Word Quiz
Filename : The Word Quiz.py
Date : 2018/09/14
Version : 0.1
"""
"""Changelog
0.1: Project started, and added introduction
"""
Continue = False
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
Progress = input("Alright! Let's begin!!!")
