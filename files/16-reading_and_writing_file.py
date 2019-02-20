from sys import argv

script, filename = argv

print "we're going read this file first > %r" %filename
target = open(filename)
print target.read()

print "We're going to delete this file now > %r" %filename
target1 = open(filename,'w')
print "To continue press enter, else press control+c"
raw_input('?')
print "Trucating the file. Goodbye."
target1.truncate()

print "Now reading after deletion to verify"
target1.close()
target2 = open(filename)
print target2.read()
target2.close()

print "Now, writing this file"
target3 = open(filename,'w')
line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
print "Going to write above 2 lines content in the file %r" %filename
target3.write(line1)
target3.write("\n")
target3.write(line2)
target3.write("\n")
print "Closing the file"
target3.close()

print "Reading the file Finally"
target4 = open(filename)
print target4.read()

print "closing the file"
target4.close()
