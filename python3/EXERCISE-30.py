
#EXERCISE-30

n = int(input("Enter N: "))

# Upper half
for i in range(1, n + 1):
    print("* " * i, end="")
    print("  " * (2 * (n - i)), end="")
    print("* " * i)

# Lower half
for i in range(n, 0, -1):
    print("* " * i, end="")
    print("  " * (2 * (n - i)), end="")
    print("* " * i)

#OUTPUT:
#Enter N: 7
#*                         * 
#* *                     * * 
#* * *                 * * * 
#* * * *             * * * * 
#* * * * *         * * * * * 
#* * * * * *     * * * * * * 
#* * * * * * * * * * * * * * 
#* * * * * * * * * * * * * * 
#* * * * * *     * * * * * * 
#* * * * *         * * * * * 
#* * * *             * * * * 
#* * *                 * * * 
#* *                     * * 
#*                         * 
