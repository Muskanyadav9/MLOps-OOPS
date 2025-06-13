# initiate a class
class Employee:
    #special method/ magic method/ dunder method
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = 'Data Scientist'

    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")

#create an object/ instance of the class
Muskan = Employee()
print(Muskan.salary)
Muskan.travel("Haryana")
