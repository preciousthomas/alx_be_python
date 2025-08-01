class BankAccount:
    def __init__(self, account_balance=0):
        self.balance = account_balance
        self.transaction_history = []

    def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited: ${amount}")
            else:
                print("invalid deposit amount.")
    def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount}")
                return True
            else:
                print("insufficient funds or invalid withdrawal amount.")
                return False
    def display_balance(self):
                print(f"Current balance: ${self.balance}")