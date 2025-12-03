# This class is for type hints in python

def meow(n: int) -> str:
    """ 
    This is the convention for docstring.
    This is how you document a function in Python.
    Return a string with n meows, each on its own line.
    :type n: int
    :raise TypeError: if n is not an int
    :return: string with n meows

    """
    return "meow\n" * n


number = int(input("Enter number of meows: "))
meows: str = meow(number)
print(meows, end="")