def digitSum2(n):
    n1=str(n)
    f=int(n1[0])
    l=int(n1[-1])
    print("First digit: ",f)
    print("Last digit: ",l)
    print("Sum: ",f+l)


num=int(input("Enter a Number: "))
digitSum2(num)