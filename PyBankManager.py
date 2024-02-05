# Define a class for managing bank accounts
class Bank_account:

    # Constructor to initialize the account with a name and an optional initial balance
    def __init__(self, account_name, balance=0):
        self.account_name = account_name
        self.balance = balance

    # Get the account name
    def get_account_name(self):
        return f"Account name is {self.account_name}"

    # Set a new account name
    def set_account_name(self, new_account_name):
        self.account_name = new_account_name

    # Deposit money into the account
    def deposit(self, amount_of_money):
        # Ensure that the deposit amount is positive
        if amount_of_money > 0:
            self.balance += amount_of_money
            return f"Money deposit process is complete. You have {self.balance} lari in your bank account."
        else:
            return "Invalid deposit amount. Please enter a positive value."

    # Withdraw money from the account
    def withdraw(self, amount_of_money):
        # Ensure the withdrawal amount does not exceed the current balance
        if amount_of_money > 0 and amount_of_money <= self.balance:
            self.balance -= amount_of_money
            return f"Money withdrawal process is complete. You have {self.balance} lari in your bank account."
        elif amount_of_money <= 0:
            return "Invalid withdrawal amount. Please enter a positive value."
        else:
            return "Insufficient funds. Withdrawal canceled."

# Get user input for creating a bank account
account_name1 = input("What is your name: ")
balance1 = int(input("How much money do you have in your bank account?"))

# Create a Bank_account instance with user input
bank_account1 = Bank_account(account_name1, balance1)

# Get user input for choosing the operation (deposit or withdrawal) and the amount
x = int(input("Which operation do you want to do? If deposit, type 1; if withdrawal, type 2: "))
amount_of_money = int(input("How much money do you want to take? "))

# Perform the chosen operation and print the result
if x == 1:
    print(bank_account1.deposit(amount_of_money))
else:
    print(bank_account1.withdraw(amount_of_money))
