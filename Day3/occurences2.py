def occurences2(s):
    c=input("Enter a character to count occurences: ")
    c1=0
    for i in s:
        if c==i:
            c1+=1 
    print(f"Occurences of character is: {c1}")

s=input("Enter a string: ")
occurences2(s)