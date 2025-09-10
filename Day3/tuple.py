def displayStudent(students):
    print("\nStudent Details:")
    for s in students:
        print(f"Roll No: {s[0]}, Name: {s[1]}, Marks: {s[2]}")

n = int(input("Enter number of students: "))
students = []

for i in range(n):
    rno = int(input(f"Enter roll number of student {i+1}: "))
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks of student {i+1}: "))
    t1 = (rno, name, marks)
    students.append(t1)

displayStudent(students)
