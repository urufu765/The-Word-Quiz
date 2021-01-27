"""
Name : Jason
Program : The Guess the Number Game
Filename : Main.py(Changed)
Date : 2018/09/05
"""
# Notes
'''#error checker example
def val():
    valid = False
    
    while valid != True:
        Ex = input("Type a number")
        try:
            E = int(Ex)
            print (E)
            valid = True
            return E
        except ValueError:
            print ("Please put a number")
            
#counter
while <condition>
for myVar in range(1,10):'''



import random  # import
#  set x, y, z to Y to loop
x = "Y"
y = "Y"

print("\nWelcome to the Guess the Number game! Your objective is to guess the number that I am thinking of!")
print("I'll choose a number between 1 and 100, and you'll have to guess what I chose!\n")
# these are the starting messages.

while x not in ["N", "n", "No", "no", "NO"]:
    # The initial loop

    x = input("Would you like to start the game? ")  # This determines whether the program should proceed or not.

    if x in ["Y", "y", "Yes", "yes", "YES"]:
        print("That's the spirit! Let's get this game started!\n")  # This will start the main loop

        while y not in ["N", "n", "No", "no", "NO"]:
            # The main loop: this will directly lead to the "non-loop like" loop section

            NUMBER = random.randint(1, 100)
            z = "Y"  # the z is set to Y here to re-enable the loop when the user selects "another round"
            valid = False
            print("Alright, I got my number!")
            # after the number is determined, the program tells the user that the number has been chosen

            while z != "N":
                # The non-loop like loop: here is where all the main action takes place

                n = "Y"
                while n != "N":
                    # this mini loop is to contain and stop the exception loop when the user did not put an integer
                    valid = False
                    rhe = input("Now, guess my number! What number am I thinking of? ")
                    # This is the error checker, to determine whether the input was integer or not
                    while valid != True:
                        test = rhe

                        try:
                            guess = int(test)
                            valid = True
                            n = "N"
                        except ValueError:
                            print ("\nOnly integers please! That means no decimals!")
                            valid = True

                GUESS = int(rhe)
                A = GUESS - NUMBER
                B = NUMBER - GUESS
                # these are equations to be used when the user gets it wrong.
                if GUESS < 1:
                    print("That's not a valid number, keep it above 1!")
                    # when the user inputs a number below 1, then this message alerts the user, before going back
                    # to square one.

                elif GUESS > 100:
                    print("That's not a valid number, keep it below 100!")
                    # when the user inputs a number above 100, then this message alerts the user, before going back
                    # to square one.

                elif NUMBER == GUESS:
                    print(" ______________________________________________________________ ")
                    print("|      _                                                    _  |")
                    print("|     | |     ___   __    ___    ___     ___   ___  _____  | | |")
                    print("|  ___| |    /     /  \  |   \  |   \   /     /       |    | | |")
                    print("| /___)  |  |     |    | |    | |    | |     |        |    | | |")
                    print("||_____) |  |     |    | |___/  |___/  |___  |        |    |_| |")
                    print("| \___)  |  |     |    | |   \  |   \  |     |        |     _  |")
                    print("|  \_)__|    \___  \__/  |    \ |    \  \___  \___    |    (_) |")
                    print("|           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     |")
                    print("|______________________________________________________________|\n")
                    print("You guessed it right!")
                    z = "N"
                    # The z is set to N to stop the loop and go back to the main loop.

                elif NUMBER > GUESS:
                    print(" __________________________________________________ ")
                    print("|                                               _  |")
                    print("|  \    /          ___     __            __    | | |")
                    print("|   \  /   |  | | |   \   /  \  |\   |  /  \   | | |")
                    print("|    \/    |  | | |    | |    | | \  | |       | | |")
                    print("|    /\    |  | | |___/  |    | |  | | | ___   |_| |")
                    print("|   /  \   |  | | |   \  |    | |   \| |    |   _  |")
                    print("|  /    \   \/\/  |    \  \__/  |    |  \__/   (_) |")
                    print("|          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      |")
                    print("|__________________________________________________|\n")
                    print("You guessed too low!")
                    print("You're off by", B)
                    z = "N"
                    # the function A determines how much the user is off by, with z set to N to stop the loop

                elif NUMBER < GUESS:
                    print(" __________________________________________________ ")
                    print("|                                               _  |")
                    print("|  \    /          ___     __            __    | | |")
                    print("|   \  /   |  | | |   \   /  \  |\   |  /  \   | | |")
                    print("|    \/    |  | | |    | |    | | \  | |       | | |")
                    print("|    /\    |  | | |___/  |    | |  | | | ___   |_| |")
                    print("|   /  \   |  | | |   \  |    | |   \| |    |   _  |")
                    print("|  /    \   \/\/  |    \  \__/  |    |  \__/   (_) |")
                    print("|          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      |")
                    print("|__________________________________________________|\n")
                    print("You guessed too high!")
                    print("You're off by", A)
                    z = "N"
                    # the function B determines how much the user is off by, with z set to N to stop the loop

                else:
                    print("Put a number!")
                    # just in case the user decides to "think outside the box" which is not even trying to type a
                    # number (after test: Turns out this is unnecessary because the program stops working once any
                    # non-integer is put in...

            print("\nThat was fun!")
            y = input("Want to go another round? ")

            if y in ["Y", "y", "Yes", "yes", "YES"]:
                print("Another round it is!\n")

            elif y in ["N", "n", "No", "no", "NO"]:
                x = "N"
                # x is set to N to go straight to the last message, skipping the initial loop all together.

            else:
                print("What?!")
                m = "Y"
                while m != "N":
                    print("Yes or no only!")
                    y = input("Want to go another round? ")
                    if y in ["Y", "y", "Yes", "yes", "YES"]:
                        print("Another round it is!\n")
                        m = "N"
                    elif y in ["N", "n", "No", "no", "NO"]:
                        x = "N"
                        m = "N"
                    else:
                        print("What?!")
                # this mini loop is only initiated when the user puts anything but yes or no.

    elif x in ["N", "n", "No", "no", "NO"]:
        print("Alright, come back when you are in the mood!")

    else:
        print("Yes and no answers only!")

print("\nSee you next time!!!")

# after test: if decimal is used for the GUESS in any way, it breaks the program.
