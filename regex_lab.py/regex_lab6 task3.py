import re

text = "I like Java. Java is easy."

result = re.sub("Java", "Python", text)

print(result)
#output
#I like Python. Python is easy.
