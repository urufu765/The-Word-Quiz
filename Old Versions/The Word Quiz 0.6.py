"""
Name : Jason
Program : The Word Quiz
Filename : The Word Quiz.py
Date : 2018/09/14
Version : 0.6
"""
"""Changelog
0.1: Project started, and added introduction
0.2: Lists added with random word picker
0.3: Words are associated with functions
0.4: first stage programed
0.5: First stage completed
0.6: Second stage completed
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
    elif Stage == 2:
        Randomizer = random.randint(0, 4)
        while Round is True:
            Ready = True
            if LIST2[Randomizer] == "Brick":
                Brick = ["_", "_", "_", "_", "_"]
                print("Alright, this word is five letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{3}{4}".format(Brick[0], Brick[1], Brick[2], Brick[3], Brick[4]))
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
                        if INPUT in ["B", "b"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Brick[0] = "B"
                            W5[0] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Brick[1] = "r"
                            W5[1] = int(1)
                            GUESS = False
                        elif INPUT in ["I", "i"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Brick[2] = "i"
                            W5[2] = int(1)
                            GUESS = False
                        elif INPUT in ["C", "c"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Brick[3] = "c"
                            W5[3] = int(1)
                            GUESS = False
                        elif INPUT in ["K", "k"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Brick[4] = "k"
                            W5[4] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST2[Randomizer] == "Terrain":
                Ter = ["_", "_", "_", "_", "_", "_"]
                print("Alright, this word is seven letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{2}{3}{4}{5}".format(Ter[0], Ter[1], Ter[2], Ter[3], Ter[4], Ter[5]))
                    # Terrain didn't fit within the limit so it is shortened to Ter
                    while CHECK is True:
                        if W6 == C6:
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
                        if INPUT in ["T", "t"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ter[0] = "T"
                            W6[0] = int(1)
                            GUESS = False
                        elif INPUT in ["E", "e"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ter[1] = "e"
                            W6[1] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's two!")
                            GuessNo = (GuessNo + 1)
                            Ter[2] = "r"
                            W6[2] = int(1)
                            GUESS = False
                        elif INPUT in ["A", "a"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ter[3] = "a"
                            W6[3] = int(1)
                            GUESS = False
                        elif INPUT in ["I", "i"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ter[4] = "i"
                            W6[4] = int(1)
                            GUESS = False
                        elif INPUT in ["N", "n"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ter[5] = "n"
                            W6[5] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST2[Randomizer] == "Maze":
                Maze = ["_", "_", "_", "_"]
                print("Alright, this word is four letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{3}".format(Maze[0], Maze[1], Maze[2], Maze[3]))
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
                        if INPUT in ["M", "m"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Maze[0] = "M"
                            W4[0] = int(1)
                            GUESS = False
                        elif INPUT in ["A", "a"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Maze[1] = "a"
                            W4[1] = int(1)
                            GUESS = False
                        elif INPUT in ["Z", "z"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Maze[2] = "z"
                            W4[2] = int(1)
                            GUESS = False
                        elif INPUT in ["E", "e"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Maze[3] = "e"
                            W4[3] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST2[Randomizer] == "Screen":
                Screen = ["_", "_", "_", "_", "_"]
                print("Alright, this word is six letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{3}{3}{4}".format(Screen[0], Screen[1], Screen[2], Screen[3], Screen[4]))
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
                        if INPUT in ["S", "s"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Screen[0] = "S"
                            W5[0] = int(1)
                            GUESS = False
                        elif INPUT in ["C", "c"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Screen[1] = "c"
                            W5[1] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Screen[2] = "r"
                            W5[2] = int(1)
                            GUESS = False
                        elif INPUT in ["E", "e"]:
                            print("Nice! That's two!")
                            GuessNo = (GuessNo + 1)
                            Screen[3] = "e"
                            W5[3] = int(1)
                            GUESS = False
                        elif INPUT in ["N", "n"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Screen[4] = "n"
                            W5[4] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST2[Randomizer] == "Blinds":
                Blinds = ["_", "_", "_", "_", "_", "_"]
                print("Alright, this word is six letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{3}{4}{5}".format(Blinds[0], Blinds[1], Blinds[2], Blinds[3], Blinds[4], Blinds[5]))
                    while CHECK is True:
                        if W6 == C6:
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
                        if INPUT in ["B", "b"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Blinds[0] = "B"
                            W6[0] = int(1)
                            GUESS = False
                        elif INPUT in ["L", "l"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Blinds[1] = "l"
                            W6[1] = int(1)
                            GUESS = False
                        elif INPUT in ["I", "i"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Blinds[2] = "i"
                            W6[2] = int(1)
                            GUESS = False
                        elif INPUT in ["N", "n"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Blinds[3] = "n"
                            W6[3] = int(1)
                            GUESS = False
                        elif INPUT in ["D", "d"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Blinds[4] = "d"
                            W6[4] = int(1)
                            GUESS = False
                        elif INPUT in ["S", "s"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Blinds[5] = "s"
                            W6[5] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
    else:
        break
"""
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
