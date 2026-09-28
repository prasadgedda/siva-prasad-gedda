#C2_9

dict1 = {}
dict2 = {}
n = int(input("Number of entries for first dictionary: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value
n = int(input("Number of entries for second dictionary: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value
merged1 = dict1.copy()
merged1.update(dict2)
merged2 = dict1 | dict2
print("Using update():", merged1)
print("Using | operator:", merged2)

#OUTPUT:
#Number of entries for first dictionary: 3
#Enter key: 0
#Enter value: 29
#Enter key: 1
#Enter value: 27
#Enter key: 2
#Enter value: 25
#Number of entries for second dictionary: 3
#Enter key: 3
#Enter value: 23
#Enter key: 4
#Enter value: 21
#Enter key: 5
#Enter value: 19
#Using update(): {'0': '29', '1': '27', '2': '25', '3': '23', '4': '21', '5': '19'}
#Using | operator: {'0': '29', '1': '27', '2': '25', '3': '23', '4': '21', '5': '19'}


