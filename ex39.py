# things = ['a', 'b', 'c', 'd']
# print(things[1])
# things[1] = 'z'
# print(things[1])
# print(things)
#
# stuff = {'Name': 'Dan', 'Age': 25, "Married": False}
# print(stuff['Married'] or True)
#
# stuff[1] = "wow"
# stuff['1'] = "NEWOW"
# print(stuff)
# del stuff[1]
# print(stuff)

states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI',
        'Texas': 'TX'
}

cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville',
        'TX': 'Austin'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'
i = 0
while i < 12:
    print(states)
    i += 1

# print("-" * 10)
# print("NY State has", cities['NY'])
# print("OR State has", cities['OR'])
#
# print("-" * 10)
# print("Michigan abbreviation is", states['Michigan'])
# print("New York abbreviation is", states['New York'])
#
# print("-" * 10)
# print("Michigan has", cities[states['Michigan']])
# print("Florida has", cities[states['Florida']])
#
# print("-" * 10)
# for state, abbrev in states.items():
#     print("State {} is abbreviated {}".format(state, abbrev))
#
# print("-" * 10)
# for abbrev, city in cities.items():
#     print("State {} has {}".format(abbrev, city))
#
# print("-" * 10)
# for state, abbrev in states.items():
#     print("State {} is abbreviated {} and has {}".format(state, abbrev, cities[abbrev]))
#
# state = states.get('Texas')
# if state:
#     print("State is {}".format(state))
# else:
#     print("Sorry, no Texas")
