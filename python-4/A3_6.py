#A3_6

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])
print("Alternate elements:", numbers[::2])


#OUTPUT:
#Enter numbers separated by spaces: 23 34 45 56 67 78 89
#First 3: [23, 34, 45]
#Last 3: [67, 78, 89]
#Alternate elements: [23, 45, 67, 89]
