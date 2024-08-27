"""class student:

    def __init__(self,name, mark):
        self.name=name
        self.mark=mark

    def get_avg(self):
        sum=0
        for val in self.mark:
            sum+=val
        print("Hello",self.name,"your average score is:", sum/3)

obj = student("Ram kumar",[100,90,80])      
#obj.get_avg()"""


#Q2

class Account:
    def __init__(self,balance,account):
        self.balance = balance
        self.account = account

    def debit(self,amount): 
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance())
    

    def credit(self,amount):
        self.balance +=amount
        print("Rs.", amount,"was credited")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
obj = Account(10000, 123456789)
obj.debit(1000)
obj.credit(500)
obj.credit(40000)
    
