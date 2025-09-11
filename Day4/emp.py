class Emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

class Manager(Emp):
    def __init__(self, name, salary,department):
        super().__init__(name, salary) 
        self.department=department 
    def display(self):
        super().display()
        print(f"Department: {self.department}") 

emp_obj=Emp("Naveen", 100000)
man_obj=Manager("Raghav", 120000, "IT")
emp_obj.display()
man_obj.display()
        
