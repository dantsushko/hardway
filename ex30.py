people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take a car")
elif cars < people:
    print("We will not take a car")
else:
    print("We cant decide")


if trucks > cars:
    print("Too many trucks")
elif trucks < cars:
    print("Maybe truck")
else:
    print("We still cant decide")

if people > trucks:
    print("Ok, lets take a truck")
else:
    print("Stay home bitch")
