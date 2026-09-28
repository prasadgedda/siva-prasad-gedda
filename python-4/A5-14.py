#A5_14

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
merged = list1 + list2
merged.sort(reverse=True)
print("Merged list in descending order:", merged)

#OUTPUT:
#Enter first list: 1 3 5 7 9
#Enter second list: 2 4 6 8 10
#Merged list in descending order: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
