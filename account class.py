class Account:
    def __init__(self):
        self.name = None
        self.acc_number=None
        self.deb_amount = None
        self.credit_amount=None
    def display_name(self,acc_number,name):
        self.acc_number=acc_number
        self.name=name
        print(self.acc_number,self.name)
    def debit_money( self,deb_amount):
        self.deb_amount=deb_amount
    def credit_money(self,credit_amount):
        self.credit_amount=credit_amount
s1 = Account()
s1.display_name(20087145155,"harshit")  
s2 = Account() 
s2.display_name(20845188428 , "Arvind") 
s3 = Account()
s3.debit_money(1000000) 
s4 = Account()   
s4.credit_money(20000)