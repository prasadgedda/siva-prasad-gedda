
#EXERCISE-11

num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")


#OUTPUT:
#Enter a number: 2907
#Not a Palindrome

