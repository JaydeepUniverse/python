count = [1, 2, 3, 4, 5]
fruits = ['orange', 'apple', 'banana', 'mango']
change = [1, 'bus', 2, 'car', 3, 'train']

for number in count:
    print "This is count list : %d" % number

for fruit_type in fruits:
    print "Types of fruits : %s" % fruit_type

for i in change:
    print "I've got %r in change list." % i

elements = []
for i in range(0, 6):
    print "Adding %d to the new element list." % i
    elements.append(i)

for i in elements:
    print "We added %d" % i
