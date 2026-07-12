print("Students details")
students=["alia","charlie"]
print("Student names:",students)
print()

print("find largest number")
numbers=[1,2,3,4,5,1,2,3]
print("Largest numbers:",max(numbers))
print()

print("find smallest number")
numbers=[1,2,3,4,5,1,2,3]
print("Smallest numbers:",min(numbers))
print()

print("find sum of all number")
numbers=[1,2,3,4,5,1,2,3]
print("Sum:",sum(numbers))
print()

print("Count even and odd number")
numbers=[1,2,3,4,5,1,2,3]
even_count=0
odd_count=0
for number in numbers:
    if number%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)
print()

print("Remove duplicate values")
numbers=[1,2,3,4,5,1,2,3]
print("List after removing duplicates:",list(set(numbers)))
print()

print("Reverse the list")
numbers=[1,2,3,4,5,1,2,3]
print("Reversed list:",numbers[::-1])