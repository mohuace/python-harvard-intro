class Student:
    # This is a initialization method that is called when an object of the class is created.
    # self refers to the current instance of the class.
    # When name and house are passed, they are assigned to the current instance's attributes.
    # The instance is already created when __init__ is called.
    # That is available in self variable.
    # This is not a constructor in other languages like C++ or Java.
    # Because in those languages, constructor is responsible for creating the object.
    # In Python, object creation is handled by __new__ method internally that is already called before __init__. We don't usually override it.
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if not house:
            raise ValueError("Missing house")

        # These two assignments will also call setter methods defined below automatically.
        # This are NOT creating new attributes name and house in the instance.
        # Instead they are calling the setter methods defined below.
        self.name = name
        self.house = house
    
    # This is exactly like toString() method in Java.
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter for name
    # Same name as variable name
    @property
    def name(self):
        # Return the actual instance variable _name
        print( "Getter for name called" )
        return self._name

    # Getter for house
    # Same name as variable name
    @property
    def house(self):
        # Return the actual instance variable _house
        print( "Getter for house called" )
        return self._house

    # Setter for name
    # Has to be same name as variable name
    # In the function, need to use self._name to avoid collision with property name
    # To avoid collision, we name our actual attribute (instance variable) with a leading underscore (_name)
    # Meant to indicate that it is intended for internal use only.
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        # This means we are creating an instance variable _name to store the actual value
        self._name = name

    # Setter for house
    # If you want to do some validation or processing,
    # you can do it here.
    @house.setter
    def house(self, house):
        if house not in ["Mulund", "Matunga", "Patlipada"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()

    # Problem, I can update name and house directly (when getters and setters are not used)
    # To circumvent this, we use properties with decorators. Decorators
    # are functions that modify the behavior of other functions or methods.


    # Once setter is defined, the setter methods will be called automatically when
    # we try to set the attribute value.
    student.name = "Corrupted Name"

    # This won't work as we have validation in setter method of house property
    #student.house = "Corrupted House"

    print(student)

# def get_student():
#     # Creating student object
#     student = Student()
#     # Assigning values to attributes.
#     # But this is not the best way to do it.
#     student.name = input("Enter Name: ")
#     student.house = input("Enter house: ")

#     return student

def get_student():
    name = input("Enter Name: ")
    house = input("Enter house: ")

    # This is better way to create an object by passing the attributes
    # to the class init method.
    return Student(name, house)

if __name__ == "__main__":
    main()
