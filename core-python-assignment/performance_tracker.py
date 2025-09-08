def calculate_average(marks):
    return sum(marks) / len(marks)

def track_performance(students):
    averages = {name: round(calculate_average(marks), 2) for name, marks in students.items()}
    top_student = max(averages, key=averages.get)
    return averages, top_student

n = int(input("Enter number of students: "))
students = {}
for _ in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    students[name] = marks
avg, topper = track_performance(students)
print("Average Marks:", avg)
print("Top Performer:", topper)
