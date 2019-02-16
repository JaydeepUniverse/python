formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"I am typing without single quote in it.",
"Now I'm using single qoute.",
"since there are four percentage r in formatter variable",
"we have to add four lines only"
)

