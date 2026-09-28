#D2_5

set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))
print("Set 1 is subset of Set 2:", set1.issubset(set2))
print("Set 1 is superset of Set 2:", set1.issuperset(set2))

#OUTPUT:
#Enter first set: 2 4 6 8 1
#Enter second set: 1 3 5 7 9
#Set 1 is subset of Set 2: False
#Set 1 is superset of Set 2: False
