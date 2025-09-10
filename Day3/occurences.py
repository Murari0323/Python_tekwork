def occurences(s):
    c=input("Enter a character to count occurences: ")
    c1=[]
    for i in range(len(s)):
        if c==s[i]:
            c1.append(i)
    print(f"positions of character is: {c1}")

s=input("Enter a string: ")
occurences(s)