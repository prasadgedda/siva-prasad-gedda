
#EXERCISE-20

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(i):
        print("*", end=" ")

    print()


#OUTPUT:
#Enter number of rows: 9
#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * * 
#   * * * * * * 
#  * * * * * * * 
# * * * * * * * * 
#* * * * * * * * * 
