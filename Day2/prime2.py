import primee
def func(n):
    for i in range(1,n+1):
        res=primee.checkPrime1(i)
        print(res)
        

num=int(input("Enter a number: "))
func(num)