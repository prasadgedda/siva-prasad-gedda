#B1_3

numbers = list(map(int, input("Enter list elements: ").split()))
my_tuple = tuple(numbers)
print("Tuple:", my_tuple)
my_list = list(my_tuple)
print("List:", my_list)

#OUTPUT:
#Enter list elements: 98 87 76 65 54 
#Tuple: (98, 87, 76, 65, 54)
#List: [98, 87, 76, 65, 54]
