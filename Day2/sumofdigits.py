def digitSum(n):
    s=0
    for i in str(n):
        s+=int(i)
    return s 

num=int(input("Enter a Number: "))
print(digitSum(num))