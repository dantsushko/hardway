print("Let's practice everything!")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none
"""

print('------------')
print(poem)
print('------------')

five = 10 - 2 + 3 - 6

print (f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return  jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point at {}".format(start_point))
print(f"We have {beans} beans {jars} jars and {crates} crates")

formula = secret_formula(start_point)
print("With a list we can do it easier: {} beans {} jars {} crates".format(*formula))