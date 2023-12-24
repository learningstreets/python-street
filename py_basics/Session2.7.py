
#Encapsulation:
class BankAccount:
    def __init__(self,acc_num,acc_name,balance):
        self.__acc_num = acc_num
        self.__acc_name = acc_name
        self.__balance = balance
    def get_acc_name(self):
        return self.__acc_name
    def get_balance(self):
        return self.__balance
    def set_balance(self,new_balance):
        self.__balance = new_balance
    def add_money(self,deposit_amt):
        self.__balance += deposit_amt
        print("amount deposited ",self.__balance)
    def withdraw_money(self,withdraw_amt):
        if withdraw_amt > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= withdraw_amt
            print("Amount withdrawn",self.__balance)
millionaire = BankAccount(1101,"Jeff",100000000)
#print(millionaire.acc_name)            
#millionaire.acc_name = "msk"
#print(millionaire.get_balance())  
millionaire.__balance = 10
#print(millionaire.get_balance())
#get and set method
#print(millionaire.__dict__)        
#millionaire._BankAccount__balance = 10
#print(millionaire.get_balance())   
millionaire.set_balance(100)
print(millionaire.get_balance())