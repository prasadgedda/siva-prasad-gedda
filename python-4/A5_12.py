#A5_12

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique = []
for value in numbers:
    if value not in unique:
        unique.append(value)
print("Original list:", numbers)
print("Without duplicates:", unique)

#OUTPUT:
#Enter numbers separated by spaces: 22 16 29 27 17 7 20
#Original list: [22, 16, 29, 27, 17, 7, 20]
#Without duplicates: [22, 16, 29, 27, 17, 7, 20]
