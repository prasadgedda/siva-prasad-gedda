#C2_6

data = {}
n = int(input("Enter number of entries: "))
for i in range(3):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value
print("Keys:")
for key in data.keys():
    print(key)
print("Values:")
for value in data.values():
    print(value)
print("Key-value pairs:")
for key, value in data.items():
    print(key, ":", value)

#OUTPUT:
#Enter number of entries: 3
#Enter key: 2
#Enter value: 26
#Enter key: 1
#Enter value: 29
#Enter key: 0
#Enter value: 27
#Keys:
#2
#1
#0
#Values:
#26
#29
327
#Key-value pairs:
#2 : 26
#1 : 29
#0 : 27
