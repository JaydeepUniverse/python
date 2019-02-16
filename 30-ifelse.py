print "Enter number of people : ",
people = int(raw_input())
print "Enter number of cars : ",
cars = int(raw_input())
print "Enter number of buses : ",
buses = int(raw_input())

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "There are too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, Let's take the buses."
else:
    print "Fine, Let's stay at Home then."
