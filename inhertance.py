class bank_acc :
    def __init__(self,title,balance,accno,withdraw,deposite):
        self.title=title
        self.balance=balance
        self.accno=accno
        self.withdraw=withdraw
        self.deposite=deposite
         
        def dispaly (self):
           print(self.title)
class saving_acc(bank_acc):
    def __init__(self,ir):
        self.ir= ir
        def display(self):
            sb=(self.ir/100)*super()._init__(self.balance)
            print("saving account balance",sb)
            class current_acc(bank_acc):
                def ca():
                    if(bank_acc.withdraw)>(bank_acc().deposite):
                        cb=bank_acc().deposite - bank_acc().withdraw
                        return cb
                    

           