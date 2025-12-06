# This function is for unpacking in python

def total(a, b, c):
    return a + b + c

arr = [1, 2, 3]

print(total(*arr))  # Unpacking the array into individual arguments

# Unpacking for dictionaries

def total(knut, sickle, galleon):
    return knut + sickle * 29 + galleon * 17 * 29

coins = {"galleon": 3, "sickle": 14, "knut": 27}

# Unpacking the dictionary into keyword arguments.
# We use ** for unpacking dictionaries
print(total(**coins))


# Variable length arguments in functons
# Using args for positional arguments
# Using kwargs for keyword arguments
def test(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

test(1, 2, 3, name="Harry", house="Gryffindor")