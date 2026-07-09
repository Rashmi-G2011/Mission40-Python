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

#prime number checker
print("Prime number checker")
n=int(input("Enter the number:"))
if n>1:
    for i in range (2,n):
        if n % i == 0:
            print(n,"Not a prime number")
            break
    else:
            print(n ,"is a prime number")
else:
    print(n,"is Not a prime number")

#fibbonacci series
print("Fibbonacci series")
n=int(input("Enter the number of terms:"))
a=0
b=1
print("Fibbonacci series:")
for i in range (n):
    print(a,end='')
    c=a+b
    a=b
    b=c

#sum of n numbers
print("Sum of first n natural numbers")
n=int(input("enter the number:"))
sum=0
for i in range(0,n+1):
    sum+=i
print("Sum:",sum)