#EXERCISE-4

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print("Largest number =", largest)

#OUTPUT:
#Enter first number: 29
#Enter second number: 7
#Enter third number: 18
#Largest number = 29

