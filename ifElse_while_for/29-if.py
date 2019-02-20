print "Number of dogs : ",
dog = int(raw_input())
print "Number of cats : ",
cat = int(raw_input())
print "Number of people : ",
people = int(raw_input())

if people < cat:
    print "Too many cats!"

if people > cat:
    print "Not many cats!"

if people < dog:
    print "Too many dogs!"

if people > dog:
    print "Not many dogs!"

print "Increase the number of dogs : ",
dog1 = int(raw_input())
dog2 = dog + dog1

print "Now total value of dogs : %d" %dog2
if people >= dog2:
    print "People are greater than or equal to dogs."

if people <= dog2:
    print "People are less than or equal to dogs."

if people == dog2:
    print "People are dog."
