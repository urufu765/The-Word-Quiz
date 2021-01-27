"""
Name : Jason
Program : The Word Quiz
Filename : The Word Quiz.py
Date : 2018/09/14
Version : 1.1
"""
"""Changelog
0.1: Project started, and added introduction
0.2: Lists added with random word picker
0.3: Words are associated with functions
0.4: first stage programed
0.5: First stage completed
0.6: Second stage completed
0.7: Third stage completed
1.0: Added judgement, and completed game!
1.1: Added letter input limit
"""
import random
Continue = False
Game = True
Stage = int(1)
Round = False
GUESS = ""
INPUT = ""
FAIL = int(0)
Judgement = True
ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
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
    elif Stage == 3:
        Randomizer = random.randint(0, 4)
        while Round is True:
            Ready = True
            if LIST3[Randomizer] == "Dinosaur":
                Di = ["_", "_", "_", "_", "_", "_", "_", "_"]
                print("Alright, this word is eight letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{3}{4}{5}{6}{7}".format(Di[0], Di[1], Di[2], Di[3], Di[4], Di[5], Di[6], Di[7]))
                    while CHECK is True:
                        if W8 == C8:
                            print("You got it! Great job!")
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
                    while GUESS is True:
                        if INPUT in ["D", "d"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Di[0] = "D"
                            W8[0] = int(1)
                            GUESS = False
                        elif INPUT in ["I", "i"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Di[1] = "i"
                            W8[1] = int(1)
                            GUESS = False
                        elif INPUT in ["N", "n"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Di[2] = "n"
                            W8[2] = int(1)
                            GUESS = False
                        elif INPUT in ["O", "o"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Di[3] = "o"
                            W8[3] = int(1)
                            GUESS = False
                        elif INPUT in ["S", "s"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Di[4] = "s"
                            W8[4] = int(1)
                            GUESS = False
                        elif INPUT in ["A", "a"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Di[5] = "a"
                            W8[5] = int(1)
                            GUESS = False
                        elif INPUT in ["U", "u"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Di[6] = "u"
                            W8[6] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Di[7] = "r"
                            W8[7] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST3[Randomizer] == "Computer":
                Co = ["_", "_", "_", "_", "_", "_", "_", "_"]
                print("Alright, this word is eight letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{3}{4}{5}{6}{7}".format(Co[0], Co[1], Co[2], Co[3], Co[4], Co[5], Co[6], Co[7]))
                    while CHECK is True:
                        if W8 == C8:
                            print("You got it! Great job!")
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
                    while GUESS is True:
                        if INPUT in ["C", "c"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Co[0] = "C"
                            W8[0] = int(1)
                            GUESS = False
                        elif INPUT in ["O", "o"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Co[1] = "o"
                            W8[1] = int(1)
                            GUESS = False
                        elif INPUT in ["M", "m"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Co[2] = "m"
                            W8[2] = int(1)
                            GUESS = False
                        elif INPUT in ["P", "p"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Co[3] = "p"
                            W8[3] = int(1)
                            GUESS = False
                        elif INPUT in ["U", "u"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Co[4] = "u"
                            W8[4] = int(1)
                            GUESS = False
                        elif INPUT in ["T", "t"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Co[5] = "t"
                            W8[5] = int(1)
                            GUESS = False
                        elif INPUT in ["E", "e"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Co[6] = "e"
                            W8[6] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Co[7] = "r"
                            W8[7] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST3[Randomizer] == "Library":
                Lib = ["_", "_", "_", "_", "_", "_"]
                print("Alright, this word is seven letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{3}{4}{3}{5}".format(Lib[0], Lib[1], Lib[2], Lib[3], Lib[4], Lib[5]))
                    while CHECK is True:
                        if W6 == C6:
                            print("You got it! Great job!")
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
                    while GUESS is True:
                        if INPUT in ["L", "l"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Lib[0] = "L"
                            W6[0] = int(1)
                            GUESS = False
                        elif INPUT in ["I", "i"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Lib[1] = "i"
                            W6[1] = int(1)
                            GUESS = False
                        elif INPUT in ["B", "b"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Lib[2] = "b"
                            W6[2] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's two!")
                            GuessNo = (GuessNo + 1)
                            Lib[3] = "r"
                            W6[3] = int(1)
                            GUESS = False
                        elif INPUT in ["A", "a"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Lib[4] = "a"
                            W6[4] = int(1)
                            GUESS = False
                        elif INPUT in ["Y", "y"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Lib[5] = "y"
                            W6[5] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST3[Randomizer] == "Uranium":
                print("Alright, this word is seven letters!")
                Ura = ["_", "_", "_", "_", "_", "_", "_"]
                print("Alright, this word is seven letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{2}{3}{4}{6}{5}".format(Ura[0], Ura[1], Ura[2], Ura[3], Ura[4], Ura[5], Ura[6]))
                    while CHECK is True:
                        if W6 == C6:
                            print("You got it! Great job!")
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
                    while GUESS is True:
                        if INPUT in ["U", "u"]:
                            print("Nice! That's two!")
                            GuessNo = (GuessNo + 1)
                            Ura[0] = "U"
                            Ura[6] = "u"
                            W6[0] = int(1)
                            GUESS = False
                        elif INPUT in ["R", "r"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ura[1] = "r"
                            W6[1] = int(1)
                            GUESS = False
                        elif INPUT in ["A", "a"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ura[2] = "a"
                            W6[2] = int(1)
                            GUESS = False
                        elif INPUT in ["N", "n"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ura[3] = "n"
                            W6[3] = int(1)
                            GUESS = False
                        elif INPUT in ["I", "i"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ura[4] = "i"
                            W6[4] = int(1)
                            GUESS = False
                        elif INPUT in ["M", "m"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            Ura[5] = "m"
                            W6[5] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
            elif LIST3[Randomizer] == "Onomatopoeia":
                print("Alright, this word is 12 letters!")
                On = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
                print("Alright, this word is eight letters!")
                while Ready is True:
                    CHECK = True
                    print("{0}{1}{8}{2}{3}{4}{8}{5}{8}{6}{7}{3}"
                          .format(On[0], On[1], On[2], On[3], On[4], On[5], On[6], On[7], On[8]))
                    while CHECK is True:
                        if W8 == C8:
                            print("You got it! Great job!")
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
                            ONE = True
                            INPUT = input("\nNow, guess a letter: ")
                            GUESS = True
                            while ONE is True:
                                if len(INPUT) == 1:
                                    CHECK = False
                                    ONE = False
                                else:
                                    print("One letter please!")
                                    ONE = False
                    while GUESS is True:
                        if INPUT in ["O", "o"]:
                            print("Nice! That's four!")
                            GuessNo = (GuessNo + 1)
                            On[0] = "O"
                            On[8] = "o"
                            W8[0] = int(1)
                            GUESS = False
                        elif INPUT in ["N", "n"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            On[1] = "n"
                            W8[1] = int(1)
                            GUESS = False
                        elif INPUT in ["M", "m"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            On[2] = "m"
                            W8[2] = int(1)
                            GUESS = False
                        elif INPUT in ["A", "a"]:
                            print("Nice! That's two!")
                            GuessNo = (GuessNo + 1)
                            On[3] = "a"
                            W8[3] = int(1)
                            GUESS = False
                        elif INPUT in ["T", "t"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            On[4] = "t"
                            W8[4] = int(1)
                            GUESS = False
                        elif INPUT in ["P", "p"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            On[5] = "p"
                            W8[5] = int(1)
                            GUESS = False
                        elif INPUT in ["E", "e"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            On[6] = "e"
                            W8[6] = int(1)
                            GUESS = False
                        elif INPUT in ["I", "i"]:
                            print("Nice! That's one!")
                            GuessNo = (GuessNo + 1)
                            On[7] = "i"
                            W8[7] = int(1)
                            GUESS = False
                        else:
                            print("Nope, that's not a correct letter.")
                            GuessNo = (GuessNo + 1)
                            MISS = (MISS + 1)
                            GUESS = False
    else:
        break
while Judgement is True:
    # there is a reason I added Stage == 3... because I want to do something crazy!
    if Stage == 3 and FAIL == 0:
        print("\nCongrats! You've got all right! Pat yourself in the back~!")
        Progress = input("Press enter to end...")
        break
    elif Stage == 3 and FAIL == 1:
        print("\nYou got two out of three right! Pretty close~!")
        Progress = input("Press enter to end...")
        break
    elif Stage == 3 and FAIL == 2:
        print("\nOne right.... I guess it's something...")
        Progress = input("Press enter to end...")
        break
    elif Stage == 3 and FAIL == 3:
        print("\nCongratulations! You failed all words! Be ashamed of yourself!")
        Progress = input("Press enter to end...")
        break
