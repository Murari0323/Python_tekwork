def palindrome2(n):
    for i in range(1,n+1):
        i=str(i)
        if i==i[::-1]:
            print(i)

n=int(input("Enter number"))
palindrome2(n)