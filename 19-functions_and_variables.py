def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese !" % cheese_count
    print "You have %d boxes of crackers." % boxes_of_crackers
    print "Man that's enough for party !!"
    print "Get a blanket !\n"

print "We can give values to function arguments directly :"
cheese_and_crackers(20, 30)

print "OR we can give another set of variables and set in the same functions :"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside arguments :"
cheese_and_crackers(10+20, 5+6)

print "We can sum our variables and predefined values :"
cheese_and_crackers(100+amount_of_cheese, 100+amount_of_crackers)
