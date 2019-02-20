from sys import argv

script, username = argv
prompt = '> '

print "Hi %s, I'm %s script." % (username, script)
print "I'd like to ask you few questions."
print "Do you like me %s ?" % username
likes = raw_input(prompt)

print "Where do you live %s ?" % username
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where it is.
You have %r computer, that's nice.""" % (likes, lives, computer)
