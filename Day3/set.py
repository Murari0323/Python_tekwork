def displaySet(s):
    print(f"Set is: {s}")

s=set()
n=int(input("Enter size of the set: "))
for i in range(n):
    s.add(input(f"Enter {i}th element: "))
displaySet(s)
