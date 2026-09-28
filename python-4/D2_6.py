#D2_6

my_set = set(map(int, input("Enter set elements: ").split()))
value = int(input("Enter element to remove using remove(): "))
try:
    my_set.remove(value)
    print("After remove():", my_set)
except KeyError:
    print("Element does not exist. remove() raises KeyError.")
value = int(input("Enter element to remove using discard(): "))
my_set.discard(value)
print("After discard():", my_set)

#OUTPUT:
#Enter set elements: 1 3 5 7 9 
#Enter element to remove using remove(): 5
#After remove(): {1, 3, 7, 9}
#Enter element to remove using discard(): 9
#After discard(): {1, 3, 7}
