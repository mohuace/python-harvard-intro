class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address
    
    def __str__(self):
        return f"Student {self.name} is from {self.address}"
    

def main():
    stud1 = Student("Mohit", "Bhivandi")
    stud2 = Student("Manasvi", "Matunga")

    print(stud1)
    print(stud2)

if __name__ == "__main__":
    main()