print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Avoid the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "3":
        print("""You carefully avoid drawing attention to yourself.
        Looking around you see that there is another door and a painting on the wall.
        Do you: #1 look at the painting or #2 go through the door.""")

        boring = input("> ")

        if boring == "1":
            print("""It turns out that you are Dorian Grey and looking at the painting makes you age by a million years instantly
            resulting in crumbly death.""")
        elif boring =="2":
            print("""Through the door is win. Congratulations""")
        else:
            print("The bear gets bored and eats you anyway.")
    else:
        print(f"well doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jelly.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into puddles of goo.")
        print("Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
