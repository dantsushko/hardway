from sys import argv

script, file = argv

text = open(file, mode = 'r+')

print ("this is ypur file")
print (text.read())
text.close()
print(text.read())
