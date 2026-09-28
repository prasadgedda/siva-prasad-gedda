#A5_11

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original:", numbers)
numbers.append(int(input("Enter value to append: ")))
print("After append():", numbers)
value = int(input("Enter value to insert: "))
position = int(input("Enter index: "))
numbers.insert(position, value)
print("After insert():", numbers)
extra = list(map(int, input("Enter elements to extend: ").split()))
numbers.extend(extra)
print("After extend():", numbers)
value = int(input("Enter value to remove: "))
if value in numbers:
    numbers.remove(value)
print("After remove():", numbers)
if numbers:
    print("Popped element:", numbers.pop())
print("After pop():", numbers)
numbers.sort()
print("After sort():", numbers)
numbers.reverse()
print("After reverse():", numbers)
value = int(input("Enter value to count: "))
print("count():", numbers.count(value))
value = int(input("Enter value to find index: "))
if value in numbers:
    print("index():", numbers.index(value))
else:
    print("Value not found")


#OUTPUT:
#Enter numbers separated by spaces: 22 16 29 27 17 7 20
#Original: [22, 16, 29, 27, 17, 7, 20]
#Enter value to append: 99
#After append(): [22, 16, 29, 27, 17, 7, 20, 99]
#Enter value to insert: 77
#Enter index: 3
#After insert(): [22, 16, 29, 77, 27, 17, 7, 20, 99]
#Enter elements to extend: 44
#After extend(): [22, 16, 29, 77, 27, 17, 7, 20, 99, 44]
#Enter value to remove: 22
#After remove(): [16, 29, 77, 27, 17, 7, 20, 99, 44]
#Popped element: 44
#After pop(): [16, 29, 77, 27, 17, 7, 20, 99]
#After sort(): [7, 16, 17, 20, 27, 29, 77, 99]
#After reverse(): [99, 77, 29, 27, 20, 17, 16, 7]
#Enter value to count: 7
#count(): 1
#Enter value to find index: 29
#index(): 2

