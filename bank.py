class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
    
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if (self.balance > amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insuffienct funds: Charging a $5 fee")
            return self

    def display_account_info(self):
        # your code here
        print(f"Balnace: {self.balance}")

    def yield_interest(self):
        # your code here
        if (self.balance > 0):
            self.balance *= (self.int_rate + 1)
        return self

    @classmethod
    def get_all_info(cls):
        for account in cls.accounts:
            print(f"Your interest rate is: {account.int_rate} Your balance is: {account.balance}")


#account1 = BankAccount(.01, 1000)
#account2 = BankAccount(.02, 10000)

#account1.deposit(500).deposit(500).deposit(100).yield_interest().display_account_info()
#account2.deposit(1000).deposit(750).withdraw(150).withdraw(100).withdraw(250).withdraw(500).yield_interest().display_account_info()

BankAccount.get_all_info()