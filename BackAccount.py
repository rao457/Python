""" This module shows simple bank account details and can be modified if needed"""
class BankAccount:
    """ This class is about basic details of account"""
    def __init__(self, name, bank_balance):
        self.name = name
        self.bank_balance =  bank_balance
    def owner_details(self):
        """ Neat owner details"""
        print(f"Owner : {self.name} \nBalance : {self.bank_balance}/Rs")
    def deposit(self, amount):
        """ Keep count of deposit money"""
        self.bank_balance += amount
        print(f"You current Balance is {self.bank_balance}/Rs")
    def withdraw(self, amount):
        """Keep count of withdraw money"""
        if amount <= self.bank_balance:
            print(f"You have successfully withdrew {amount}/Rs.")
        else:
            print("Your account balance is insufficient to make this transaction.")
        remaining_balance = self.bank_balance - amount
        print(f"Your remaining account balance is {remaining_balance}.")
# Instance
a_user = BankAccount('Zohaib', 200000)
a_user.owner_details()
deposit_money = 50000
a_user.deposit(deposit_money)
withdraw_money = 20000
a_user.withdraw(withdraw_money)


