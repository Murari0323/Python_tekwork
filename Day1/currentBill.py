cNum=int(input("Enter Consumer Number: "))
cName=input("Enter Consumer Name: ")
pmr=int(input("Enter present month reading: "))
lmr=int(input("Enter last month reading: "))
cost=3.80
tmr=pmr-lmr
cBill=tmr*cost
print("Customer Number: ",cNum)
print("Customer Name: ",cName)
print("Present month reading: ",pmr)
print("last month reading: ",lmr)
print("cost per unit: ",cost)
print("Current bill: ",cBill)

