def cBill(u):
    if u<=50:
        return u*3.80
    elif u>50 and u<=100:
        return (50*3.80)+(u-50)*4.20
    elif u>100 and u<=200:
        return (50*3.80)+(50*4.20)+(u-100)*5.10
    elif u>200 and u<=300:
        return (50*3.80)+(50*4.20)+(100*5.10)+(u-200)*6.30
    elif u>300:
        return (50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)+(u-300)*7.50


units=int(input("Enter total units: "))
print(cBill(units))