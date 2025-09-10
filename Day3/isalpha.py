def count(s):
    a=0
    b=0
    c=0
    for i in s:
        if i.isalpha():
            a+=1 
        elif i.isdigit():
            b+=1 
        else:
            c+=1 
    print(f"No.of alphabets: {a}\nNo.of digits: {b}\nNo.of special characters: {c}")

s=input("Enter a string: ")
count(s)