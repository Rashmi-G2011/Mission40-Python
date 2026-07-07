#Check whether the given number is positive, negative or zero
print("Check whether the given number is positive, negative or zero")
num=int(input("Enter the number:"))
if num<0:
    print("number is negative")
elif num>0:
    print("Number is positive")
else:
    print("Number is zero")
print()

#largest of three numbers
print("Largest of three numbers")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if (num1>num2)and(num1>num3):
    print("Largest number is ",num1)
elif (num2>num1)and(num2>num3):
    print("Largest number is ",num2)
else:
    print("Largest number is ",num3)
print()

#even or odd
print("Check whether the number is even or odd")
num=int(input("Enter the number:"))
if (num%2)==0:
    print("even number")
else:
    print("odd number")
print()

#grade calculator
print("Grade Calculator")
marks=int(input("Enter the marks:"))
if marks>=85:
    print("Grade:A")
elif marks>=45:
    print("Grade:B")
else:
    print("Grade:C")
print()

#ATM Withdrawal System
print("ATM Withdrawal System")
balance_amt=float(input("Enter the account balance:"))
withdrawal_amt=float(input("Enter the withdrawal amount:"))
if withdrawal_amt>balance_amt:
    print("Insufficient Balance")
else:
    print("Withdrawal Successfull!! Balance amount is", balance_amt-withdrawal_amt)
print()

#Login System
print("Login System")
user_name=str(input("Enter the username:"))
password=input("Enter the password:")
if user_name=="rash" and password=="rash2011":
    print("Login successfull")
else:
    print("Invalid Credentials")
print()

#Leap year program
print("Check whether the year is leap year or not")
year=int(input("Enter a year:"))
if (year%400)==0 and (year%4==0):
    print("Leap year")
else:
    print("not a leap year")