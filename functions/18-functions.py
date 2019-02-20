def print_two(*args):
    arg1, arg2, arg3 = args
    print "arg1 : %r, arg2 : %r, arg3 : %r" % (arg1, arg2, arg3)

def print_two_again(arg1, arg2):
    print "arg1 : %r, arg2 : %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1 : %r" % arg1

def print_none():
    print "Nothing to print from any argument."

print_two("abc", "pqr", "xyz")
print_two_again("xyz", "jkl")
print_one("only one")
print_none()
