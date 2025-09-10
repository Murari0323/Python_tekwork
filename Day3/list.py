def displayList(list1):
    print(list1)  


list1=[]
n=int(input("Enter size of list: "))
for i in range(n):
    list1.append(input(f"Enter {i}th element: ")) 

displayList(list1)