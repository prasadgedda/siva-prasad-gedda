#C1_4

keys = input("Enter keys separated by spaces: ").split()
values = input("Enter values separated by spaces: ").split()
dictionary = dict(zip(keys, values))
print("Dictionary:", dictionary)

#OUTPUT:
#Enter keys separated by spaces: 0 1 2 3 4 5
#Enter values separated by spaces: 7 29 18 20 24 11
#Dictionary: {'0': '7', '1': '29', '2': '18', '3': '20', '4': '24', '5': '11'}
