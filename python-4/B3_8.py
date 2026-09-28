#B3_8

tuple1 = tuple(input("Enter first tuple elements: ").split())
tuple2 = tuple(input("Enter second tuple elements: ").split())
print("Concatenated tuple:", tuple1 + tuple2)
print("Tuple 1 repeated 3 times:", tuple1 * 3)

#OUTPUT:
#Enter first tuple elements: 9 7 5 3 1
#Enter second tuple elements: 8 6 4 2 0
#Concatenated tuple: ('9', '7', '5', '3', '1', '8', '6', '4', '2', '0')
#Tuple 1 repeated 3 times: ('9', '7', '5', '3', '1', '9', '7', '5', '3', '1', '9', '7', '5', '3', '1')
