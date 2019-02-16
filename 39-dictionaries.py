states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '1' * 10
for key in cities:
    print key, "State has : ", cities[key]

print '2' * 10
for key in states:
    print key, "state's abbreviation is : ", states[key]

print '3' * 10
print "Michigan has : ", cities[states['Michigan']]
print "Florida has : ", cities[states['Florida']]

print '4' * 10
for state, abbrev in states.items():
    print "%s is abbreviated as %s." % (state, abbrev)

print '5' * 10
for state, city in cities.items():
    print "%s has the city %s." % (state,city)

print '6' * 10
for state, abbrev in states.items():
    print "%s is abbreviated as %s and has the city %s." % (state, abbrev, cities[abbrev])

print '7' * 10
state = states.get('Texas', None)
if not state:
    print "There's not state Texas in the states dictionary."

city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is %s." % city
