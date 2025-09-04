def armstrong(n):
    s=0
    for i in str(n):
        s+=(int(i))**3 
    if s==n:
        print("Armstrong number")
    else:
        print("Not a armstrong number")


num=int(input("Enter a number: "))
armstrong(num)