#D2_8

numbers = list(map(int, input("Enter numbers with duplicates: ").split()))
unique_set = set(numbers)
sorted_list = sorted(unique_set)
print("Unique elements:", unique_set)
print("Sorted unique list:", sorted_list)

#OUTPUT:
#Enter numbers with duplicates: 23 34 56 23 34 58
#Unique elements: {56, 34, 58, 23}
#Sorted unique list: [23, 34, 56, 58]
