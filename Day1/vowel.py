def vowel(a):
    vowel_seq="aeiouAEIOU"
    if a in vowel_seq:
        print("Value is vowel: ")
    else:
        print("Value is consonant: ")
    
a=input("Enter any alphabet")
vowel(a)