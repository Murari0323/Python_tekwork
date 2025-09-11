class Payment:
    def __init__(self,amount):
        self.amount=amount
    def pay(self):
        pass 

class CashPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid {self.amount} in cash")

class CardPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid {self.amount} using credit/debit card")

class UPIPayment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        print(f"Paid {self.amount} using UPI") 

pays=[CashPayment(1000),CardPayment(1000),UPIPayment(1000)]
for p in pays:
    p.pay()