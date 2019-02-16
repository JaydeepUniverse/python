ten_things = "Car Train Buse Plane Road"
print "There are ten things list : ", ten_things
print "Wait there are not really 10 things in above list. Let's fix that."
stuff = ten_things.split(' ')
more_stuff = ["Tiger", "Lion", "Elephant", "Monkey", "Cheetah", "Bear", "Fox"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding ", next_one
    stuff.append(next_one)
    print "There's %d item now in the list." %len(stuff)

print "There we go : ", stuff

print "Let's do something with stuff list."
print stuff[1]
print stuff[-1]
print stuff.pop()
print '111'.join(stuff)
print '#'.join(stuff[3:5])
