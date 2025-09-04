def pattern2(n):
    for i in range(n):
        for j in range(n):
            if j==i:
                print("$",end=" ")
            else:
                print("*",end=" ") 
        print() 

num=int(input("Enter n value: "))
pattern2(num)