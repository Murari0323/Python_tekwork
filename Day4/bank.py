class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited {amount}") 
    def withdraw(self,amount):
        if(self.__balance>=amount):
            self.__balance-=amount
            print(f"withdrawn: {amount}")
        else:
            print("Insufficent balance") 
    def get_balance(self):
        print(f"current balance: {self.__balance}") 




obj=BankAccount()
obj.deposit(5000)
obj.withdraw(2000)
obj.get_balance()
