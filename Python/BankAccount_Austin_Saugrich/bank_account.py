class BankAccount:

    def __init__(self, accountname, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.accountname = accountname

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

    def display_account_info(self, name):
        print(f"{name} {self.accountname} Balance: ${self.balance}")
        return self

    def yield_intrest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print('You dont have enough in your account.')
        return self


class User:

    def __init__(self, name, email, accountname):
        self.name = name
        self.email = email
        self.account = [BankAccount(accountname, int_rate=0.02, balance=0)]

    def make_deposit(self, amount, bank):
        self.account[bank].deposit(amount)
        return self

    def make_withdrawal(self, amount, bank):
        self.account[bank].withdraw(amount)
        return self

    def display_user_balance(self):
        for i in self.account:
            i.display_account_info(self.name)
        return self

    def add_account(self, accountname):
        self.account.append(BankAccount(accountname, int_rate=0.02, balance=0))
        return self

    def transfer_money(self, amount, other_user, bank):
        if amount > self.account[bank].balance:
            print('You dont have enough to transfer.')
        else:
            self.make_withdrawal(amount, bank)
            other_user.make_deposit(amount, 0)
        return self


user1 = User("Tyrone", "user@email.com", 'savings')
user2 = User("Nolan", "nolan@email.com", 'savings')
user1.make_deposit(50, 0).make_withdrawal(5, 0)
user1.add_account('checking').make_deposit(100, 1).display_user_balance()
user1.transfer_money(34, user2, 0).display_user_balance()
user2.display_user_balance()

# from last assignment
# user1 = BankAccount(0.02, 500)
# user2 = BankAccount(0.05, 50)

# user1.deposit(5).deposit(10).deposit(15).withdraw(
#     32).yield_intrest().display_account_info()

# user2.deposit(20).deposit(40).withdraw(10).withdraw(
#     5).withdraw(7).withdraw(13).yield_intrest().display_account_info()
