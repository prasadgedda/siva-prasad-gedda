#B3_9

marks = tuple(map(float, input("Enter 5 student marks: ").split()))
mark1, mark2, mark3, mark4, mark5 = marks
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
print("Marks:", marks)
print("Average:", average)

#OUTPUT:
#Enter 5 student marks: 98 87 76 65 54
#Marks: (98.0, 87.0, 76.0, 65.0, 54.0)
#Average: 76.0
