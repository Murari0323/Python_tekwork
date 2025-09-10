def delPosition(list1):
    m=int(input("Enter position of element to delete: "))
    list2=[]
    for i in range(len(list1)):
        if(i!=m):
            list2.append(list1[i])
    print(list2) 


list1=[]
n=int(input("Enter size of list: "))
for i in range(n):
    list1.append(int(input(f"Enter {i}th element: "))) 

delPosition(list1)