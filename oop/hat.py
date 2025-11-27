#This example is for using (class level methods and variables)

import random

# This class represents a hat in harry potter
class Hat:
    # This is a class variable (static variable)
    houses = ["Gryffindor", "Hufflepuf", "Ravenclaw", "Slytherin"]

    # This is a class method. It has access to the class reference
    # called cls. This can be used to refer to class variables like houses.
    # In Harry Potter, there is only one sorting hat, hence it makes sense.
    # to keep one method that can be accessed without creating instances
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# Accessing the class method directly.
def main():
    Hat.sort("Harry")

if __name__ == "__main__":
    main()
 