#D1_1

values = input("Enter 8 elements, including some duplicates: ").split()
my_set = set(values)
print("Original elements:", values)
print("Set:", my_set)
print("Duplicates are automatically removed.")


#OUTPUT:
#Enter 8 elements, including some duplicates: 77 88 99 55 66 77 22 99
#Original elements: ['77', '88', '99', '55', '66', '77', '22', '99']
#Set: {'99', '55', '77', '88', '66', '22'}
#Duplicates are automatically removed.
