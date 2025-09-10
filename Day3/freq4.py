def freq4(s):
    m=[]
    for i in set(s):
        m.append(s.count(i))
    for j in set(s):
        if s.count(j)==min(m):
            print(f"Lowest frequency character is: {j}")
            
        

s=input("Enter a string: ")
freq4(s)