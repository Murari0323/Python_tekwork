class Student:
    def __init__(self,name,rno,marks):
        self.name=name
        self.rno=rno
        self.marks=marks

    def display(self):
        print(f"Name: {self.name}\nRoll No: {self.rno}\nMarks: {self.marks}") 

s1=Student("Hari", 1, 90)
s2=Student("Sameer", 2, 89)
s1.display()
s2.display()
