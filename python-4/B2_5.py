#B2_5

items = tuple(input("Enter 12 elements separated by spaces: ").split())
middle = len(items) // 2
print("First half:", items[:middle])
print("Second half:", items[middle:])

#OUTPUT:
#Enter 12 elements separated by spaces: 1 2 3 4 5 6 7 8 9 11 12 13
#First half: ('1', '2', '3', '4', '5', '6')
#Second half: ('7', '8', '9', '11', '12', '13')
