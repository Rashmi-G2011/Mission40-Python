print("Creating a file and writing my name in it")
file=open("notes.txt",'w')
file.write("my name is Rashmi")
file.close()
print()

print("Reading the contents of the file and printing in the console")
with open("notes.txt",'r') as file:
    content=file.read()
    print(content)
print()

print("Append the text to eof")
with open("notes.txt",'a') as file:
    file.write("\nI am a engineering student")
print()

print("COunt number of words")
with open("notes.txt",'r') as file:
    content=file.read()
    words=len(content.split())
print("Number of words:",words)
print()

print("Count number of lines")
with open("notes.txt",'r') as file:
    lines=len(file.readlines())
print("Number of lines:",lines)
print()

print("search a word")
word="Rashmi"
with open("notes.txt",'r') as file:
    content=file.read()
if word in content:
    print("word is found")
else:
    print("word not found")
print()

print("Replace the word")
with open("notes.txt",'r') as file:
    content=file.read()
content=content.replace('engineering','data science')
with open("notes.txt",'w') as file:
    file.write(content)
print("the word is replaced successfully") 
print()

print("Student's details")
with open("notes.txt",'a') as file:
    n=int(input("Enter the number of students:"))
    for i in range(n):
        name=input("Enter the name:")
        age=int(input("Enter the age:"))

        file.write(f"\n{name} is {age} years old")

with open("notes.txt",'r') as file:
    print(file.read())