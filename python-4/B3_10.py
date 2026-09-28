#B3_10

numbers = tuple(map(int, input("Enter tuple elements: ").split()))
try:
    numbers[0] = 100
except TypeError as error:
    print("Error:", error)
    print("Tuples are immutable.")

#OUTPUT:
#Enter tuple elements: 29 27 28 26
#Error: 'tuple' object does not support item assignment
#Tuples are immutable.
