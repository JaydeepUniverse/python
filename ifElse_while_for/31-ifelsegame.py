print "You see 2 doors. Which door you'd like to open it up ? 1 or 2"
print "Enter the number of door : ",
door = raw_input()

if door == "1":
    print """
    There's a giant beer eating cheese and cake. What would you do ?
    1. Take the cake.
    2. Scream at the bear.
    3. Run away
    """
    print "Enter your choice : ",
    bear = raw_input()

    if bear == "1":
        print "Now bear will eat your face off."
    elif bear == "2":
        print "Now bear will eat your legs off."
    else:
        print "Well, That's good choice."

elif door == "2":
    print """
    You're in shopping mall now. What would you like to purchase ?
    1. Fashion
    2. Daily needs
    3. No money
    """
    print "Enter your choice : ",
    mall = raw_input()

    if mall == "1" or mall == "2":
        print "Good choice, go ahead and make yourself happy."
    else:
        print "Earn the money and comeback."

else:
    print "You're not playing game, it's not good."
