#D2_4

set1 = set(map(int, input("Enter elements of set 1: ").split()))
set2 = set(map(int, input("Enter elements of set 2: ").split()))
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

#OUTPUT:
#Enter elements of set 1: 1 3 5 7 9
#Enter elements of set 2: 2 4 6 8 1
#Union: {1, 2, 3, 4, 5, 6, 7, 8, 9}
#Intersection: {1}
#Difference: {9, 3, 5, 7}
#Symmetric Difference: {2, 3, 4, 5, 6, 7, 8, 9}
