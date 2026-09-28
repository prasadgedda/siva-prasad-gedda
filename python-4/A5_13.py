#A5_13

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
maximum = numbers[0]
minimum = numbers[0]
total = 0
for value in numbers:
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value
    total += value
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)

#OUTPUT:
#Enter numbers separated by spaces: 20 7 17 27 29 16 22
#Maximum: 29
#Minimum: 7
#Sum: 138
