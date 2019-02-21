def break_words(stuff):
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    return word

def print_last_word(words):
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    words = break_words(sentence)
    print words
    first_word = print_first_word(words)
    print first_word
    last_word = print_last_word(words)
    print last_word

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print words
    first_sorted_word = print_first_word(words)
    print first_sorted_word
    last_sorted_word = print_last_word(words)
    print last_sorted_word


print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)


sentence = "All good things come to those who weight."

words = break_words(sentence)
print words
sorted_words = sort_words(words)
print sorted_words

first_word = print_first_word(words)
print first_word
last_word = print_last_word(words)
print last_word
first_sorted_word = print_first_word(sorted_words)
print first_sorted_word
last_sorted_word = print_last_word(sorted_words)
print last_sorted_word

print words
print sorted_words

sentence1 = "a g h b c f e d"
print_first_and_last(sentence1)
print_first_and_last_sorted(sentence1)
