print("to store students details")
student={"name":"Alice","age":22,"major":"CSE"}
print(student)
print()

print("Create a phone book")
phone_book={"Rashmi":9742376648,"Queen":34351516536}
print(phone_book)
print()

print("Count word frequency")
alphabet="a g e s a g e r t i"
single_alphabet=alphabet.split()
frequency={}
for letter in single_alphabet:
    frequency[letter]=frequency.get(letter,0)+1
print("Frequency of alphabet:",frequency)
print()

print("Merge two dictionaries")
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
print('updated dictionary:',dict1|dict2)#or dict1.update(dict2)
print()

print("Find student with highest marks")
grades={"Alice":98,"Bob":76,"Charlie":99}
print("Student with highest marks:",max(grades,key=grades.get))