
#EXERCISE-24

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#OUTPUT:
#Enter number of rows: 7
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 
#1 2 3 4 5 6 
#1 2 3 4 5 6 7 
 
