class Account:
    
    """ This class defines the Account user name and bank balance also handles the deposit and withdrawal money"""
    
    def __init__(self, name, bank_balance):
        self.name = name
        self.bank_balance = bank_balance
        self.deposit = 0
        self.withdraw = 0

    def show_info(self):
        print(f"User_name : {self.name}")
        print(f"Bank_balance: {self.bank_balance}")


    
    def my_deposit(self, deposited):
        if self.deposit > 0:
            deposited = self.deposit
            return f"You have successfully deposited {deposited}/Rs"
        # else:
        #     return "Invalid amount "
    def withdrawal(self, withdrawed):
        if self.withdraw > 0 :
            withdrawed = self.withdraw
            return f"You have successfully withdrawed {withdrawed}/Rs"
        # else:
        #     return "Insufficient Balance"
new_user = Account('Zohaib', 200000)
print(new_user.my_deposit(2000))
print(new_user.withdrawal(10))
