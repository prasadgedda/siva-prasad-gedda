#D2_7

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))
if set1.isdisjoint(set2):
    print("The sets are disjoint.")
else:
    print("The sets are not disjoint.")

#OUTPUT:
#Enter first set:  1 2 3 4 5
#Enter second set: 6 7 8 9 10
#The sets are disjoint.

