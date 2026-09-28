#B2_6

items = tuple(input("Enter tuple elements: ").split())
value = input("Enter value to search: ")
if value in items:
    print(value, "exists in the tuple")
else:
    print(value, "does not exist in the tuple")

#OUTPUT:
#Enter tuple elements: 1 3 5 7 9 11
#Enter value to search: 7
#7 exists in the tuple
