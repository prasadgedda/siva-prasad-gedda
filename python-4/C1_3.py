#C1_3

student = {
    "name": "Ravi",
    "age": 18,
    "branch": "CSE"
}
print("Before update:", student)
new_name = input("Enter new name: ")
student["name"] = new_name
print("After update:", student)

#OUTPUT:
#Before update: {'name': 'Ravi', 'age': 18, 'branch': 'CSE'}
#Enter new name: ISHU
#After update: {'name': 'ISHU', 'age': 18, 'branch': 'CSE'}
