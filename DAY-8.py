print("division with zero")
try:
    print(2/0)
except ZeroDivisionError:
    print("division with zero is not accepted")
print()

print("invalid integer value")
try:
    n=int(input("Enter the integer value:"))
    print(n)
except ValueError:
    print("Please enter the valid integer value")
print()

print("file not found")
try:
    with open("rash.txt","r") as file:
        file.read()
except FileNotFoundError:
    print("Error:File not found")
print()

print("Safe calculator")
try:
    num1=int(input("Enter number-1:"))
    num2=int(input("Enter number-2:"))
    op=input("Enter the operator(+,-,*,/):")
    if op=='+':
        result=num1+num2
    elif op=='-':
        result=num1-num2
    elif op=='*':
        result=num1*num2
    elif op=='/':
        result=num1/num2
    else:
        print("Invalid operator")
        result=None
    if result is not None:
        print("Result:",result)
except ZeroDivisionError:
    print("Division with zero is not accpeted")
except ValueError:
    print("Please enter the valid number")
print()