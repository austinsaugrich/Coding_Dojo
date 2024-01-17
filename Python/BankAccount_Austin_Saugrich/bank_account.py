class BankAccount:

    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print('You dont have enough in your account.')
        return self


user1 = BankAccount(0.02, 500)
user2 = BankAccount(0.05, 50)

user1.deposit(5).deposit(10).deposit(15).withdraw(
    32).yield_intrest().display_account_info()

user2.deposit(20).deposit(40).withdraw(10).withdraw(
    5).withdraw(7).withdraw(13).yield_intrest().display_account_info()
