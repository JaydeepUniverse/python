from sys import exit

def start():
    print """
    Welcome to my small, easy and fun game.
    There is a door to your right and left.
    Which one would you take ? Type right or left.
    """
    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        evil_room()
    else:
        dead2("You're not playing correctly.")

def bear_room():
    print """
    There is a bear here. The bear has a bunch of honey.
    The bear is standing on the door, how would you move it ?
    Type the ans. as below:
    1. take honey
    2. taunt bear
    3. open door
    """
    bear_moved = False

    while True:
        next = raw_input("> ")
        if next == "take honey":
            dead2("The bear would look at you and then slap at your face.")
        elif next == "taunt bear" and not bear_moved:
            print "                                 "
            print "The bear has moved from the door, door is open and you can go through it now."
            print "You can now 'open door' or it's your choice still to 'taunt beer' but ready for consequences of it."
            print "                                 "
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead2("Bear would going to chew your legs.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "                                 "
            print "I got no idea what that means."
            print "                                 "

def gold_room():
    print "                                 "
    print "This room is full of Gold. How may kg would you take ? Type 25 or 50"
    print "                                 "
    next = raw_input("> ")
    if next == "25" or next == "50":
        nex1 = int(next)
    else:
        print "                                 "
        print "You have to options only to type."
        print "                                 "

    if next1 == 25:
        print "                                 "
        print "Nice, you're not greedy, you win!"
        print "                                 "
        exit(0)
    else:
        dead2("You greddy bastard!")

def evil_room():
    print """
    Here you see great evil. To save yourself type,
    1. flee
    2. fight
    """
    next = raw_input("> ")
    if next == "flee":
        print "                                 "
        print "Good choice! You're still in the game."
        print "                                 "
        start()
    elif next == "fight":
        dead2("Oh that's bad! You lost the game.")
    else:
        evil_room()

def dead(why):
    print "                                 "
    print why, "Good Job!"
    print "                                 "
    exit(0)

def dead2(why):
    print "                                 "
    print why, "Bad Job!"
    print "                                 "
    exit(0)

start()
