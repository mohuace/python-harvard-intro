# Example to demonstrate inheritance in Python

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ... # Other methods and properties of Wizard class

# Student class inherits from Wizard class
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)  # Call the constructor of the parent class
        self.house = house
    ... # Other methods and properties of Student class


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the parent class
        self.subject = subject
    ... # Other methods and properties of Professor class