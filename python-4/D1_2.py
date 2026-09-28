#D1_2

my_list = input("Enter list elements separated by spaces: ").split()
my_string = input("Enter a string: ")
set_from_list = set(my_list)
set_from_string = set(my_string)
print("Set from list:", set_from_list)
print("Set from string:", set_from_string)

#OUTPUT:
#Enter list elements separated by spaces: 22 33 44 55 66 77 
#Enter a string: ISHU
#Set from list: {'44', '33', '22', '77', '55', '66'}
#Set from string: {'I', 'H', 'U', 'S'}
