#A6_17

words = input("Enter words separated by spaces: ").split()
result = [word for word in words if len(word) > 4]
print("Words with more than 4 letters:", result)

#OUTPUT:
#Enter words separated by spaces: ISHU  CHERRY HARSHI POOJI 
#Words with more than 4 letters: ['CHERRY', 'HARSHI', 'POOJI']

