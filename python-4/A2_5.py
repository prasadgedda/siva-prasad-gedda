#A2_5

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for index, value in enumerate(numbers):
    print("Index:", index, "Value:", value) 


#OUTPUT:
#Enter numbers separated by spaces: 44 55 66 77 88 99
#Index: 0 Value: 44
#Index: 1 Value: 55
#Index: 2 Value: 66
#Index: 3 Value: 77
#Index: 4 Value: 88
#Index: 5 Value: 99
