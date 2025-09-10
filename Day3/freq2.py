def freq(s):
    m=[]
    for i in s:
        if i not in m:
            print(i,end=str(s.count(i)))
            m.append(i)

s=input("Enter a string: ")
freq(s)