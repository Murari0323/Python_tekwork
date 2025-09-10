def countEvenOdd(list1):
    evenCount=0 
    oddCount=0
    for j in list1:
        if j%2==0: 
            evenCount+=1
        else:
            oddCount+=1 
    print(f"EvenCount: {evenCount}\nOddCount: {oddCount}")  


list1=[]
n=int(input("Enter size of list: "))
for i in range(n):
    list1.append(int(input(f"Enter {i}th element: "))) 

countEvenOdd(list1)