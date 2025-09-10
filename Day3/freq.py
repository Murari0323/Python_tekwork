def countFrequency(list1):
    for j in set(list1):
        print(f"{j}-->{list1.count(j)}")
         
  


list1=[]
n=int(input("Enter size of list: "))
for i in range(n):
    list1.append(int(input(f"Enter {i}th element: "))) 

countFrequency(list1)