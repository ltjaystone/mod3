def add(num1, num2):
    return num1+num2

def subtract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2


runAgain = True

while runAgain == True:
    oper = input("enter the operation - edward karusko")
    num1 = int(input("enter the first number - random lvl 1 crook named sam hendrix miller"))
    num2 = int(input("enter the second number - jack fe!n"))

    if oper ==  "+":
        print(add(num1, num2))
    elif oper == "-":
        print(subtract(num1, num2))
    elif oper == "*":
        print(multiply(num1, num2))
    elif oper == "/":
        print(divide(num1, num2))
    else:
        print("invalid operation")
    
    again = input("do anotehr calculation? (y/n)")
    if again=="n":
        runAgain=False
