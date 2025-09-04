def checkPrime1(n):
    c = 0
    if n == 2:
        return f"{n} is prime"
        
    for i in range(2, n):
        if n % i == 0:
            c += 1
            break   # no need to keep checking
    
    if c == 0 and n > 1:
        return f"{n} is prime"
    else:
        return f"{n} is not prime"
