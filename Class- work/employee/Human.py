
class Human:
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob
        
    def __str__(self):
        return f'name: {self.name}\n age: {self.age}\n dob: {self.dob}'
        
    
class Employee(Human):
    def __init__(self, name, age,dob, employee_id):
        super().__init__(name, age,dob)
        self.employee_id = employee_id
        
    def __str__(self):
        return f"{super().__str__()}\n {self.employee_id}"
    

hi = Human("john",19,1990)
print(hi)

e1 = Employee("john",19,1990,88)
print(e1)