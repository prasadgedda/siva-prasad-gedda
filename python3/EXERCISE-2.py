#EXERCISE-2

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#OUTPUT:  
#Enter a year: 2007
#Not a Leap Year

#Enter a year: 2008
#Leap Year


