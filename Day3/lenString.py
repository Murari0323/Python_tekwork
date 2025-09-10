def stringLength(s):
    c=0
    for j in s:
        c+=1 
    print(f"length of string is: {c}")

def compare(s,s1):
    if s==s1:
        print("strings are equal")
    else:
        print("strings are not equal")
    print(s+" "+s1) 

s=input("Enter a string: ")
s1=input("Enter string to compare: ")
stringLength(s)
compare(s,s1)