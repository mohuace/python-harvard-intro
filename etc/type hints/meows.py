# This class is for type hints in python

def meow(n: int):
    for _ in range(n):
        print("Meow!")


number = int(input("Enter number of meows: "))
meow(number)