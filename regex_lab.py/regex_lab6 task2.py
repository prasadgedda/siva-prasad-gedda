import re

text = "I have 10 apples and 20 oranges."

# findall()
result1 = re.findall(r"\d+", text)
print(result1)

# finditer()
result2 = re.finditer(r"\d+", text)

for match in result2:
    print("Match:", match.group())
    print("Position:", match.span())
#output
    ['10', '20']
Match: 10
Position: (7, 9)
Match: 20
Position: (21, 23)
