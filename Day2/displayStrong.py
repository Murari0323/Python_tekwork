def fact(x):
    if x == 0 or x == 1:
        return 1
    return fact(x - 1) * x

def displayStrong(n):
    for j in range(1, n + 1):
        s = 0
        for i in str(j):
            s += fact(int(i))
        if s == j:   # check with j, not n
            print(j)

num = int(input("Enter a number: "))
print(f"Strong numbers between 1 and {num}:")
displayStrong(num)
