class mystuff(object):

    def __init__(self):
        self.variable = "Now and Then"

    def apple(self):
        print "I'm classy Apple !"
        print self

thing = mystuff()
thing.apple()
print thing.variable
