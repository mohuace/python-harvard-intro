#Buggy, it takes string input by default
# x = input("What's the first number? ")
# y = input("What's the second number? ")

# x = int(input("What's the first number? "))
# y = int(input("What's the second number? "))

# res = x + y

# print("The sum is "+str(res))


a = float(3.43)
b = float(2.22)

c = a + b

#Round function rounds to the nearest integer, will print 6
print("The sum is: ", round(c))

#But it also takes optional parameter in which you can mention number of digits that it will round to
#Will print 5.7
print("The sum in nearest decimal up to 1 place is: ", round(c, 1))


print(2 / 3)

print(round(2 / 3, 2))

#we can round using f strings too
z = 2 / 3
print(f"{z:.2f}")