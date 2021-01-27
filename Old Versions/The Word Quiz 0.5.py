"""
Name : Jason
Program : The Word Quiz
Filename : The Word Quiz.py
Date : 2018/09/14
Version : 0.5
"""
"""Changelog
0.1: Project started, and added introduction
0.2: Lists added with random word picker
0.3: Words are associated with functions
0.4: first stage programed
0.5: first stage completed
"""
import random
Continue = False
Game = True
Stage = int(1)
Round = False
GUESS = ""
INPUT = ""
Progress = input("Hey there! (hint: press enter to continue)")
print("Welcome! I'm Arri the Puzzle Master!")
Progress = input("Recognize me? ")  # just for fun, serves no real purpose
while Continue is False:
    if Progress in ["Yes", "YES", "yes", "y", "Y"]:
        print("Nice~ Glad to meet you too!\n")
        Continue = True
    else:
        print("Oh well, it's fine I guess...\n")
        Continue = True
Continue = False
while Continue is False:
    print("You have to guess three words! But don't worry,")
    print("you're allowed 5 wrong guesses for each word before game over!")
    print("However you only get 10 guesses per word.")
    Understand = input("Understand? ")
    if Understand in ["Yes", "YES", "yes", "y", "Y"]:
        Continue = True
    elif Understand in ["No", "NO", "no", "n", "n"]:
        print("I'll repeat myself...")
        print("Welcome to the Word Quiz!")
    else:
        print("\nDo please say yes or no...")
        print("I'll just repeat myself.")
        print("Welcome to the Word Quiz!")
Progress = input("\nAlright! Let's begin!!! Press enter to start!\n")
LIST1 = ["Dog", "Grey", "Fire", "Cat", "Water"]
LIST2 = ["Brick", "Terrain", "Maze", "Screen", "Blinds"]
LIST3 = ["Dinosaur", "Computer", "Library", "Uranium", "Rubber"]
while Game is True:  # game starts
    MISS = int(0)
    GuessNo = int(0)
    FAIL = int(0)
    # Preparing the checker
    W3 = [0, 0, 0]
    W4 = [0, 0, 0, 0]
    W5 = [0, 0, 0, 0, 0]
    W6 = [0, 0, 0, 0, 0, 0]
    W7 = [0, 0, 0, 0, 0, 0, 0]
    W8 = [0, 0, 0, 0, 0, 0, 0, 0]
    C3 = [1, 1, 1]
    C4 = [1, 1, 1, 1]
    C5 = [1, 1, 1, 1, 1]
    C6 = [1, 1, 1, 1, 1, 1]
    C7 = [1, 1, 1, 1, 1, 1, 1]
    C8 = [1, 1, 1, 1, 1, 1, 1, 1]
    while Round is False:  # resetting the checker
        W3[0] = int(0)
        W3[1] = int(0)
        W3[2] = int(0)
        W4[0] = int(0)
        W4[1] = int(0)
        W4[2] = int(0)
        W4[3] = int(0)
        W5[0] = int(0)
        W5[1] = int(0)
        W5[2] = int(0)
        W5[3] = int(0)
        W5[4] = int(0)
        W6[0] = int(0)
        W6[1] = int(0)
        W6[2] = int(0)
        W6[3] = int(0)
        W6[4] = int(0)
        W6[5] = int(0)
        W7[0] = int(0)
        W7[1] = int(0)
        W7[2] = int(0)
        W7[3] = int(0)
        W7[4] = int(0)
        W7[5] = int(0)
        W7[6] = int(0)
        W8[0] = int(0)
        W8[1] = int(0)
        W8[2] = int(0)
        W8[3] = int(0)
        W8[4] = int(0)
        W8[5] = int(0)
        W8[6] = int(0)
        W8[7] = int(0)
        Round = True
    if Stage == 1:
        Randomizer = random.randint(0, 4)  # this will determine which word out of the list of five will be used
        while Round is True:
            Ready = True
            if LIST1[Randomizer] == "Dog":  # when the Randomizer selects 0, it will start this word
                Dog = ["_", "_", "_"]
                print("Alright, this word is three letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}".format(Dog[0], Dog[1], Dog[2]))
                    while CHECK is True:  # this will check if the user has gotten all the letters
                        if W3 == C3:
                            print("You got it! Onto the next round!")
                            Stage = (Stage + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif MISS == 5:  # this will end the first stage when the user messes up 5 times
                            print("Too many wrongs! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif GuessNo == 10:  # this will end the stage when the user guessed too many times.
                            # it makes the later stages harder.
                            print("You've guessed 10 times, and didn't get the answer! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        else:  # if none of the above conditions are met, it will just ask the user to guess.
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            CHECK = False
                    while GUESS is True:
                        if INPUT in ["D", "d"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Dog[0] = "D"
                            W3[0] = int(1)
                            GUESS = False
                        elif INPUT in ["O", "o"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Dog[1] = "o"
                            W3[1] = int(1)
                            GUESS = False
                        elif INPUT in ["G", "g"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Dog[2] = "g"
                            W3[2] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST1[Randomizer] == "Grey":
                Grey = ["_", "_", "_", "_"]
                print("Alright, this word is four letters!")
                while Ready is True:  # edit
                    CHECK = True
                    print("{0}{1}{2}{3}".format(Grey[0], Grey[1], Grey[2], Grey[3]))
                    while CHECK is True:
                        if W4 == C4:
                            print("You got it! Onto the next round!")
                            Stage = (Stage + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif MISS == 5:
                            print("Too many wrongs! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif GuessNo == 10:
                            print("You've guessed 10 times, and didn't get the answer! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        else:
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            CHECK = False
                    while GUESS is True:
                        if INPUT in ["G", "g"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Grey[0] = "G"
                            W4[0] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Grey[1] = "r"
                            W4[1] = int(1)
                            GUESS = False
                        elif INPUT in ["E", "e"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Grey[2] = "e"
                            W4[2] = int(1)
                            GUESS = False
                        elif INPUT in ["Y", "y"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Grey[3] = "y"
                            W4[3] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST1[Randomizer] == "Fire":
                Fire = ["_", "_", "_", "_"]
                print("Alright, this word is four letters!")
                while Ready is True:  # edit
                    CHECK = True
                    print("{0}{1}{2}{3}".format(Fire[0], Fire[1], Fire[2], Fire[3]))
                    while CHECK is True:
                        if W4 == C4:
                            print("You got it! Onto the next round!")
                            Stage = (Stage + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif MISS == 5:
                            print("Too many wrongs! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif GuessNo == 10:
                            print("You've guessed 10 times, and didn't get the answer! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        else:
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            CHECK = False
                    while GUESS is True:
                        if INPUT in ["F", "f"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Fire[0] = "F"
                            W4[0] = int(1)
                            GUESS = False
                        elif INPUT in ["I", "i"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Fire[1] = "i"
                            W4[1] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Fire[2] = "r"
                            W4[2] = int(1)
                            GUESS = False
                        elif INPUT in ["E", "e"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Fire[3] = "e"
                            W4[3] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST1[Randomizer] == "Cat":
                Cat = ["_", "_", "_"]
                print("Alright, this word is three letters!")
                while Ready is True:  # edit
                    CHECK = True
                    print("{0}{1}{2}".format(Cat[0], Cat[1], Cat[2]))
                    while CHECK is True:
                        if W3 == C3:
                            print("You got it! Onto the next round!")
                            Stage = (Stage + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif MISS == 5:
                            print("Too many wrongs! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif GuessNo == 10:
                            print("You've guessed 10 times, and didn't get the answer! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        else:
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            CHECK = False
                    while GUESS is True:
                        if INPUT in ["C", "c"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Cat[0] = "C"
                            W3[0] = int(1)
                            GUESS = False
                        elif INPUT in ["A", "a"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Cat[1] = "a"
                            W3[1] = int(1)
                            GUESS = False
                        elif INPUT in ["T", "t"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Cat[2] = "t"
                            W3[2] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST1[Randomizer] == "Water":
                Water = ["_", "_", "_", "_", "_"]
                print("Alright, this word is five letters!")
                while Ready is True:  # edit
                    CHECK = True
                    print("{0}{1}{2}{3}{4}".format(Water[0], Water[1], Water[2], Water[3], Water[4]))
                    while CHECK is True:
                        if W5 == C5:
                            print("You got it! Onto the next round!")
                            Stage = (Stage + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif MISS == 5:
                            print("Too many wrongs! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        elif GuessNo == 10:
                            print("You've guessed 10 times, and didn't get the answer! You lose!")
                            Stage = (Stage + 1)
                            FAIL = (FAIL + 1)
                            Round = False
                            GUESS = False
                            Ready = False
                            CHECK = False
                        else:
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            CHECK = False
                    while GUESS is True:
                        if INPUT in ["W", "w"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Water[0] = "W"
                            W5[0] = int(1)
                            GUESS = False
                        elif INPUT in ["A", "a"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Water[1] = "a"
                            W5[1] = int(1)
                            GUESS = False
                        elif INPUT in ["T", "t"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Water[2] = "t"
                            W5[2] = int(1)
                            GUESS = False
                        elif INPUT in ["E", "e"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Water[3] = "e"
                            W5[3] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Water[4] = "r"
                            W5[4] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
    else:
        break

"""
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
    else:
        break
"""