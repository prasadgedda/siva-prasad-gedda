#D1_3

my_set = set(input("Enter initial set elements: ").split())
element = input("Enter one element to add: ")
my_set.add(element)
multiple = input("Enter multiple elements to add: ").split()
my_set.update(multiple)
print("Final set:", my_set)

#OUTPUT:
#Enter initial set elements: 12 23 34 45 56 
#Enter one element to add: 67
#Enter multiple elements to add: 78 89
#Final set: {'23', '12', '56', '67', '45', '89', '34', '78'}
