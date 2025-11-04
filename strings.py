name = input("Hey, whats your full name? ")

#Removes whitespace and Capitalize (first letter will be caps)
#strip removes spaces from start and end of the string
name = name.strip().capitalize()

#First letter of all words will be capital
name = name.title()

#Split user's name into first name and last name
# first, last = name.split(" ")

# print("Hello, "+first)

#print("Hi "+name)

#name = input("What is your name ")
#Adding multiple arguments to print adds a space in between automatically
# print("Hello, ", name)

#This by default will print in two separate lines
# print("Hello")
# print(name)

#There is an end parameter of print that is \n by default. You can change that
# print("Hello, ", end="")
# print(name)

#Can add separator between params
#print("Hello", name, sep="###")

#How to add quotes in print
# print("Hello, \"Friend\"")
# print('Hello, "Friend"')

#f strings
#print(f"Hello, {name}")


### Join function ###

arr = ["My", "name", "is", "Mohit"]

#First, need to add a string that you want to append with each element of the list
#And then the join function will take the list itself as the argument
print(" ".join(arr))