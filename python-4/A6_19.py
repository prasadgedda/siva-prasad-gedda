#A6_19

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = [0 if number < 0 else number for number in numbers]
print("Original:", numbers)
print("Modified:", result)

#OUTPUT:
#Enter numbers separated by spaces: 88 77 66 55 44
#Original: [88, 77, 66, 55, 44]
#Modified: [88, 77, 66, 55, 44]
