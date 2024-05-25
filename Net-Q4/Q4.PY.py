class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return interest_amount

    def print_details(self):
        print(f"Current balance: {self.balance}, Interest rate: {self.interest_rate}")

bank_account = BankAccount("1357", "AHMAD")
print("Initial Balance:", bank_account.get_balance())
bank_account.deposit(1000)
print("Balance after deposit: $", bank_account.get_balance())
bank_account.withdraw(500)
print("Balance after withdrawal: $", bank_account.get_balance())

savings_account= SavingsAccount("2468", "OSAMA", 5000, 0.05)
print("\nInitial Savings Account:")
savings_account.print_details()

savings_account.apply_interest()
print("\nBalance after applying interest:")
savings_account.print_details()
