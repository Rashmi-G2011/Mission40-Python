#Function to add two numbers
print("function to add two numbers")
n1=int(input("Enter number 1:"))
n2=int(input("enter the number 2:"))
def add_nums(a,b):
    return a+b
sum=add_nums(n1,n2)
print("Sum: ",sum)
print()

#Function to find even or odd
print("Function to check even or odd")
n=int(input("Enter the number:"))
def even_odd(a):
    if a%2 ==0:
        return 'even'
    else:
        return 'odd'
print("number is ",even_odd(n))
print()

#Largest of three
print("Largest of three numbers")
def two_numbers(a,b):
    if a>b:
        return a
    else:
        return b
def three_numbers(a,b,c):
        largest=two_numbers(a,b)
        if c>largest:
            return c
        else:
            return largest
num1=int(input("Enter the number 1:"))
num2=int(input("enter the number 2:"))
num3=int(input("Enter the number 3:"))
print("largest:",three_numbers(num1,num2,num3))
print()

#Function to calculate factorial
print("Function to calculate factorial")
def factorial(n):
    if n<=1:
        return 1
    else:
        fact=1
        for i in range(2,n+1):
            fact=fact*i
        return fact
num=int(input("Enter the number:"))
print("Factorial:",factorial(num))
print()

#function to check prime number
print("function to check prime number")
number=int(input("Enter the number:"))
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i!=0:
                return 'prime'
            else:
                return 'not prime'
    else:
        return 'not prime'
print(number," is ",prime(number))
print()

#fibbonacci series
print("Function to print fibonacci series")
no_terms=int(input("Enter the number of terms:"))
def fibonacci(t):
    a=0
    b=1
    for i in range (t):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
print("Fibonacci series:")
fibonacci(no_terms)

