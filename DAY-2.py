print("check whether the number is positive, negative or zero")
num=int(input("enter the number:"))
if num>0:
    print("The number is positive.")
elif num<0:
    print("The number is negative.")
else:
    print("The number is zero.")
print()

print("find the largest of three numbers")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if (num1>=num2) and (num1>=num3):
    largest=num1
elif (num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3
print("The largest number is:", largest)
print()

print("check if a year is a leap year")
year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
print()

print("grade calculator")
marks=int(input("Enter your marks: "))
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
else:
    print("Grade: C")
print()

print("ATM withdrawal eligibility")
balance=float(input("Enter your account balance: "))
withdrawal_amount=float(input("Enter the amount you want to withdraw: "))
if withdrawal_amount<=balance:
    print("Withdrawal successful. Your new balance is:", balance-withdrawal_amount)
else:
    print("Insufficient balance. Withdrawal failed.")
print()

print("login system")
username=input("Enter your username: ")
password=input("Enter your password: ")
if username=="admin" and password=="password":
    print("Login successful.")
else:
    print("Invalid username or password.")