def divisible(a):
    if a%5==0 and a%11==0:
        print("Divisible by both 5 and 11")
    elif a%5==0:
        print("Divisible by 5 only")
    elif a%11==0:
        print("Divisible by 11 only")
    else:
        print("Not divisible by both 5 and 11")

a=int(input("Enter a number: "))
divisible(a)        

