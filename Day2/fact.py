def fact(n):
    f=1
    while(n>=1):
        f*=n 
        n-=1 
    return f



num=int(input("Enter a Number: "))
print(fact(num))