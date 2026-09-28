#C1_5

employees = {}
for i in range(3):
    employee_id = input(f"Enter employee ID {i + 1}: ")
    name = input("Enter name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    employees[employee_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }
print("Employee dictionary:")
print(employees)

#OUTPUT:
#Enter employee ID 1: 25341
#Enter name: AJAY
#Enter department: ECE
#Enter salary: 50.000
#Enter employee ID 2: 24341
#Enter name: VIJAY
#Enter department: MECH
#Enter salary: 70.000
#Enter employee ID 3: 23341
#Enter name: PRANAY
#Enter department: IT
#Enter salary: 90.000
#Employee dictionary:
{'25341': {'name': 'AJAY', 'department': 'ECE', 'salary': 50.0}, '24341': {'name': 'VIJAY', 'department': 'MECH', 'salary': 70.0}, '23341': {'name': 'PRANAY', 'department': 'IT', 'salary': 90.0}}
