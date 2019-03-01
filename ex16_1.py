from sys import argv

script, filename = argv

text = open(filename)
print (f"You have opened file {filename}\nHere is Your text")
print(text.read())
