
#EXERCISE-22

n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

for i in range(n, 0, -1):
    print(" " * (n - i), end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

#OUTPUT:
#Enter N: 6
#     *
#    ***
#   *****
#  *******
# *********
#***********
#***********
# *********
#  *******
#   *****
#    ***
#     *
