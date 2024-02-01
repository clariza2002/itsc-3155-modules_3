class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, account):
        self.balance+=account
    
    def withdraw(self, account):
         if(self.balance < account):
             print("Insuffienct Withdrawl amount exceeds available balance")
         else:
             self.balance-=account
    
    def get_balance(self):
        return f"{self.account_name} has a balance of ${self.balance}"