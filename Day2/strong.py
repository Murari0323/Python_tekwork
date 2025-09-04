def strong(n):
    s=0
    for i in str(n):
        s+=fact(int(i))
    if s==n:
        print("strong number")
    else:
        print("Not a strong number")

def fact(x):
    if x==1:
        return 1 
    return fact(x-1)*x 

num=int(input("Enter a number: "))
strong(num)