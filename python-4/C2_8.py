#C2_8

data = {
    "name": "Iswarya",
    "age": 18,
    "branch": "CSE"
}
key = input("Enter key to search: ")
if key in data:
    print("Value:", data[key])
else:
    print("Key does not exist.")

#OUTPUT:
#Enter key to search: 4
#Key does not exist.
