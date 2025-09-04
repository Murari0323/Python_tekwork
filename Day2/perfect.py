def perfect(n):
    s=0 
    for i in range(1,n):
        if n%i==0:
            s+=i 
    if s==n:
        print("perfect number")
    else:
        print("Not a perfect number")

num=int(input("Enter a number: "))
perfect(num)