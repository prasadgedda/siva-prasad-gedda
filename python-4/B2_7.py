#B2_7

numbers = tuple(map(int, input("Enter numbers: ").split()))
value = int(input("Enter value to count: "))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Count:", numbers.count(value))

#OUTPUT:
#Enter numbers: 2 4 6 8 10
#Enter value to count: 8
#Maximum: 10
#Minimum: 2
#Count: 1
