#A1_2


data = [
    int(input("Enter an integer: ")),
    float(input("Enter a float: ")),
    input("Enter a string: "),
    input("Enter True or False: ") == "True",
    input("Enter 3 list elements separated by spaces: ").split()
]
for item in data:
    print(item, "->", type(item))


#OUTPUT:
#Enter an integer: 729
#Enter a float: 7.18
#Enter a string: Arya
#Enter True or False: True
#Enter 3 list elements separated by spaces: hi hello bye
#729 -> <class 'int'>
#7.18 -> <class 'float'>
#Arya -> <class 'str'>
#True-> <class 'bool'>
#['hi', 'hello', 'bye'] -> <class 'list'>
