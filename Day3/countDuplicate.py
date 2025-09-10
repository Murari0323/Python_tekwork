def duplicate(list1):
    uniqueCount=len(set(list1))
    Total=len(list1)
    print(f"Duplicates Count: {Total-uniqueCount}")
    print(list(set(list1)))
         
  


list1=[]
n=int(input("Enter size of list: "))
for i in range(n):
    list1.append(int(input(f"Enter {i}th element: "))) 

duplicate(list1)