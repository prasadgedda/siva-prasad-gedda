#C2_7

data = {
    "name": "Iswarya",
    "age": 18,
    "branch": "CSE"
}
key = input("Enter key to remove: ")
if key in data:
    removed = data.pop(key)
    print("Removed value:", removed)
else:
    print("Key does not exist.")
search_key = input("Enter key to access: ")
value = data.get(search_key, "Key not found")
print("Result:", value)
print("Dictionary:", data)

#OUTPUT:
#Enter key to remove: a
#Key does not exist.
#Enter key to access: 7
#Result: Key not found
#Dictionary: {'name': 'Iswarya', 'age': 18, 'branch': 'CSE'}
