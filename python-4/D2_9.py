#D2_9

odd_squares = {number ** 2 for number in range(1, 21) if number % 2 != 0}
print("Squares of odd numbers:", odd_squares)

#OUTPUT:
#Squares of odd numbers: {1, 121, 225, 289, 9, 169, 361, 81, 49, 25}
