from sys import exit
from re import search

def gold_room():
    print("""This room is full of gold.
    There is also a door at the back of the room.""")
    wallet = 0
    got_money = False

    while True:

        choice = input("> ")
        if "take" and ("0" in choice or "1" in choice or "2" in choice or "3" in choice or "4" in choice or "5" in choice or "6" in choice or "7" in choice or "8" in choice or "9" in choice):
            how_much = int(search(r'\d+', choice).group())
            got_money = True
            wallet += how_much

        if got_money == True and wallet < 50:
            print(f"""You take {how_much} gold.
            You now have {wallet} gold.""")
        elif got_money == True and wallet >= 50:
            heavy = True
            print(f"You have {wallet} gold and that's a lot of gold to carry!")

        if choice == "open door" and wallet in range(1,49):
            print("You have entered the room of win. Congratulations and you have money too.")
            exit(0)
        elif choice == "open door" and wallet >= 50:
            dead("You are too fat with gold to go through the door and die instead.")
            exit(0)
        elif choice == "open door" and wallet == 0:
            dead("You have escaped but forgot the gold and so die of the sad.")
            exit(0)
            
        else:
            print("I don't understand.")



def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("the bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets annoyed and eats your bones.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I don't understand.")


def cthulu_room():
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()


def dead(why):
    print(why, "good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and one to your left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
