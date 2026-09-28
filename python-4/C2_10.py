#C2_10

items = {}
n = int(input("Enter number of items: "))
for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    items[name] = price
highest_item = max(items, key=items.get)
lowest_item = min(items, key=items.get)
print("Highest priced item:", highest_item, items[highest_item])
print("Lowest priced item:", lowest_item, items[lowest_item])


#OUTPUT:
#Enter number of items: 3
#Enter item name: CUP
#Enter price: 20.00
#Enter item name: SPOON
#Enter price: 10.00
#Enter item name: PAN
#Enter price: 100.00
#Highest priced item: PAN 100.0
#Lowest priced item: SPOON 10.0
