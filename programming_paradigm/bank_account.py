class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)  
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
                print("Insufficient funds or invalid withdrawal amount.")
                return False
    def display_balance(self):
            print(f"Current Balance: ${self.account_balance:.2f}")