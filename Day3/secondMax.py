def secondMax(list1):
    maxi=list1[0]
    secondmax=list1[0]
    for j in list1:
        if maxi<j: 
            secondmax=maxi
            maxi=j 
        elif maxi>j and secondmax<j:
            secondmax=j 
    print("Second Largest element in the list is: ",secondmax)  


list1=[]
n=int(input("Enter size of list: "))
for i in range(n):
    list1.append(int(input(f"Enter {i}th element: "))) 

secondMax(list1)