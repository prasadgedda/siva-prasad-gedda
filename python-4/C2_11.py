#C2-11

text = input("Enter a string: ")
frequency = {}
for character in text:
    frequency[character] = frequency.get(character, 0) + 1
print("Character frequency:", frequency)

#OUTPUT:
#Enter a string: ISHU
#Character frequency: {'I': 1, 'S': 1, 'H': 1, 'U': 1}
