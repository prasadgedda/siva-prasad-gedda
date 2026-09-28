#A4_9

items = input("Enter 7 elements separated by spaces: ").split()
print("Last element:", items[-1])
print("Second-last element:", items[-2])
print("Last 3 elements:", items[-3:])

#OUTPUT:
#Enter 7 elements separated by spaces: 22 16 29 27 17 7 20
#Last element: 20
#Second-last element: 7
#Last 3 elements: ['17', '7', '20']
