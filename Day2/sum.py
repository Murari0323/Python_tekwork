def sum(n):
    s=0
    while(n>=1):
        s+=n 
        n-=1 
    print("Sum: ",s)


num=int(input("Enter a Natural number: "))
sum(num)

