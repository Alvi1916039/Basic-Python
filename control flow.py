"""
#if, else, elif
a = int(input("Enter the first number: ")) #variable a with an integer value
b = int(input("Enter the second number: ")) #variable b with an integer value
if a>b: #condition
    print("a is greater than b") #executable command if condition satisfies
elif a<b: #condition
    print("b is greater than a") #executable command if condition satisfies
else: #condition
    print("a is equal to b") #executable command if condition satisfies
"""

# Nested if
x = int(input("Enter any integer: "))
if x>10:
    print(">10")
    print("inside top if block")
    if x>30:
        print(">30")
        print("inside the nested if block")
    else:
        print("<=30")
        print("Outside of if block & inside of else block")
print("Outside of all blocks")
