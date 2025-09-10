def displayNeg(list1):
      print("Displaying Negative numbers: ")
      for j in list1:
           if j<0:
                print(j)


list1=[]
n=int(input("Enter size of list: "))
for i in range(n):
    list1.append(int(input(f"Enter {i}th element: "))) 

displayNeg(list1)