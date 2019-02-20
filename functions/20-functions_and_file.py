#!/usr/bin/env python2.7

from sys import argv

script, input_file = argv

#def print_all(f):
#    print f.read()

#def rewind(f):
#    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

#print "Let's print complete file first :"
#print_all(current_file)

#print "Now let's rewind like a tape."
#rewind(current_file)

print "Let's print each line separately :"
current_line = 1
while current_line <= 4:
    print_a_line(current_line, current_file)
    current_line = current_line + 1
