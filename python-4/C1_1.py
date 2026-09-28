#C1_1

students = {}
for i in range(5):
    roll = input(f"Enter roll number {i + 1}: ")
    name = input(f"Enter student name {i + 1}: ")
    students[roll] = name
print("Student dictionary:", students)

#OUTPUT:
#Enter roll number 1: 56
#Enter student name 1: POOJI
#Enter roll number 2: 40
#Enter student name 2: ISHU
#Enter roll number 3: 62
#Enter student name 3: ROSHNI
#Enter roll number 4: 32
#Enter student name 4: SANVI
#Enter roll number 5: 38
#Enter student name 5: DHARANI
#Student dictionary: {'56': 'POOJI', '40': 'ISHU', '62': 'ROSHNI', '32': 'SANVI', '38': 'DHARANI'}
