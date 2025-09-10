def freq3(s):
    m=[]
    for i in set(s):
        m.append(s.count(i))
    for j in set(s):
        if s.count(j)==max(m):
            print(f"Highest frequency character is: {j}")

        



s=input("Enter a string: ")
freq3(s)