import re

text = "Python is easy"

# match()
result1 = re.match("Python", text)
print(result1)

# search()
result2 = re.search("is", text)
print(result2)

# fullmatch()
result3 = re.fullmatch("Python is easy", text)
print(result3)
#output
#<re.Match object; span=(0, 6), match='Python'>
#<re.Match object; span=(7, 9), match='is'>
#<re.Match object; span=(0, 14), match='Python is easy'>
