def countNotes(a):
    while(a>=10):
        if a>=500:
            print("500 Notes: ",a//500)
            a=a%500
        elif a>=200:
            print("200 Notes: ",a//200)
            a=a%200
        elif a>=100:
            print("100 Notes: ",a//100)
            a=a%100 
        elif a>=50:
            print("50 Notes: ",a//50)
            a=a%50 
        elif a>=20:
            print("20 Notes: ",a//20)
            a=a%20 
        elif a>=10:
            print("10 Notes: ",a//10)
            a=a%10
         
        
amount=int(input("Enter amount to check number of notes: "))
countNotes(amount)