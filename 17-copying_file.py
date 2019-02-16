from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %r to %r " %(from_file, to_file)

in_file = open(from_file)
print "Reading from file"
print in_file.read()
in_file.close()

in_file1 = open(from_file)
indata = in_file1.read()
print "The input file is %d bytes long." % len(indata)

print "Does the output file exists ? %r" % exists(to_file)
print "hit Enter to contiue copying or control+c to Abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()

print "Reading %r file" %to_file
target = open(to_file)
print target.read()

print "Copying successful."
target.close()
in_file1.close()
