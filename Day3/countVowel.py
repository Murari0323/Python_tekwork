def countVowel(s):
    v=0
    c=0
    s1="aeiouAEIOU"
    for i in s:
        if i in s1:
            v+=1 
        else:
            c+=1 
    print(f"Vowels Count: {v}\nConsonants Count: {c}")


s=input("Enter a string: ")
countVowel(s)