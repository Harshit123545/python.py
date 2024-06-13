class Customer:
    def __init__(self,id1,name,age,wallet_balance):
        self.id1=id1
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def get_id1(self):
        return self.id1
    def set_id1(self,id1):
        self.id1=id1
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age
    def get_wallet_balance(self):
        return self.__wallet_balance
    def set_wallet_balance(self,wallet_balance):
        if(wallet_balance<10000 and wallet_balance>0):
            self.__wallet_balance=wallet_balance
cus_obj=Customer(102,"Raghav",21,50000)
print("before updation")
print(cus_obj.get_id1())
print(cus_obj.get_name())
print(cus_obj.get_age())
print(cus_obj.get_wallet_balance())
cus_obj.set_id1(103)
cus_obj.set_name("harsh")
cus_obj.set_age(25)
cus_obj.set_wallet_balance(6000)
print("after updation")
print(cus_obj.get_id1())
print(cus_obj.get_name())
print(cus_obj.get_age())
print(cus_obj.get_wallet_balance())
