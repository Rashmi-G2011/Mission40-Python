#print numbers from 1 to 100
print("Print numbers from 1 to 100")
for i in range (0,101):
    print(i)

#print even numbers
print("print even numbers")
num1=int(input("Enter the starting number:"))
num2=int(input("Enter the ending number:"))
for i in range (num1,num2):
    if i%2==0:
        print(i)

#print odd number
print("print odd numbers")
num1=int(input("Enter the starting number:"))
num2=int(input("Enter the ending number:"))
for i in range (num1,num2):
    if i%2!=0:
        print(i)

#Multiplication Table
print("Multiplication Table")
num=int(input("Enter the number:"))
for i in range(0,11):
    print(num,'*',i,'=',num*i)

#factorial of a number
print("Factorial of a number")
num=int(input("Enter a number:"))
if num==0 and num==2:
    print("factorial=1")
else:
    fact=1
    for i in range (2,num+1):
        fact*=i
    print("Factorial=",fact)

