class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds"
        else:
            return "Invalid withdrawal amount"

    def check_balance(self):
        return f"Current balance: ${self.balance}"

# Example usage:
account = BankAccount(1000)  # Initial balance of $1000

print(account.check_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(1500)) 

