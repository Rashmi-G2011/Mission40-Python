#hello world program
print("hello world!")

#print function
name='Rashmi'
age=20
print("My name is", name, "and I am", age, "years old.")

#add two numbers
num1=10
num2=20
sum=num1+num2
print("Sum of", num1, "and", num2, "is:", sum)

#area of rectangle
l=5
b=10
area=l*b
print("Area of rectangle is:", area)

#celsius to fahrenheit
celsius=65
fahrenheit=(celsius*9/5)+32
print(celsius, "degree Celsius is equal to", fahrenheit, "degree Fahrenheit.")

#simple calculator
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
diff=num1-num2
product=num1*num2
quotient=num1/num2
print("Sum:", sum)
print("Difference:", diff)
print("Product:", product)
print("Quotient:", quotient)

#percentage calculator
marks_obtained=int(input("Enter marks obtained: "))
total_marks=int(input("Enter total marks: "))
percentage=(marks_obtained/total_marks)*100
print("Percentage:", percentage, "%")

#age calculator
current_year=int(input("Enter current year: "))
birth_year=int(input("Enter your birth year: "))
age=current_year-birth_year
print("Your age is:", age, "years old.")
