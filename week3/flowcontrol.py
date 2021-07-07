#!/usr/bin/env python3

print("""You enter a dark room with three doors.
Do you go through door #1, door #2, or door #3?""")

door = input ("-> ")

# == Door Number 1 logic ============
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ===========
    bear = input ("-> ")
    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 logic ==========
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina. \n")

    print("1. Use your portal gun to escape.")
    print("2. Close the door.")
    print("3. Drop kick Cthulhu in the retina.")

    # == Insanity logic ==========
    insanity = input ("-> ")

    if insanity == "1" or insanity == "2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print("N) Cthulu turns you into a pile of muck.")
        print("N) Not so good job!")

# == Door Number 3 logic ==========
elif door == "3":
    print("It's a room full of puppies!")
    print("What do you do? \n")

    print("1. Pet the puppies.")
    print("2. Snuggle the puppies.")

    # == Cuteness logic ==========
    cuteness = input("-> ")

    if cuteness == "1" or cuteness == "2":
        print("1) Cuteness overload, you adopt all the puppies!")
    else:
        print(f"{cuteness}? Wrong answer, the puppies go into attack mode and take over the world.")

else:
    print("You did not select a door??? Good call :)")