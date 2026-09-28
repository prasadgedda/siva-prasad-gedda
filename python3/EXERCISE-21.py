
#EXERCISE-21

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")

    for j in range(i):
        print("*", end=" ")

    print()

#OUTPUT:
#Enter number of rows: 8
#* * * * * * * * 
# * * * * * * * 
#  * * * * * * 
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 
