def checkPrime(n):
    c=0
    if n==2:
        return"Prime Number"
        
    for i in range(2,n):
        if n%i==0:
            c+=1 
    if c==0:
        return "Prime Number"
    else:
        return "Not a Prime Number" 
        

num=int(input("Enter a Number: "))
print(checkPrime(num))