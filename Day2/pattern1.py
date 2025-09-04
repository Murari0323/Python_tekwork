def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ") 
        print() 

num=int(input("Enter n value: "))
pattern1(num)