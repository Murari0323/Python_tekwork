def maximum(a,b,c):
    if a>b:
        if a>c:
            print(f"{a} is maximum") 
        else:
            print(f"{c} is maximum")
    else:
        if b>c:
            print(f"{b} is maximum")
        else:
            print(f"{c} is maximum")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
maximum(a,b,c)