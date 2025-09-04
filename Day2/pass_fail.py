def checkRes(marks):
    if marks<40:
        return "Fail"
    else:
        if marks>80:
            return "Distinction"
        elif marks>70 and marks<=80:
            return "A"
        elif marks>50 and marks<=70:
            return "B"
        elif marks<=50:
            return "C"
        else:
            return "Enter valid marks"

marks=int(input("Enter the marks: "))
print(checkRes(marks))