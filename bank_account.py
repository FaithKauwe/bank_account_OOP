

import random
class BankAccount:
    def __init__(self, full_name, account_number=None, balance=0):
        self.full_name = full_name
    # set account number to random 8 digit number    
        if account_number is None:
            self.account_number = self.generate_account_number()
        else:
            self.account_number = account_number
        self.balance = balance
    # function that returns account number
    def generate_account_number(self):
        # Generate a random 8-digit number
        return random.randint(10000000, 99999999)

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print((f"Amount deposited: {deposit_amount}\n"
              f"New Balance: {self.balance}"))
        return self.balance

    def withdraw(self, withdrawal_amount):
        if self.balance < withdrawal_amount:
            print((f"Insufficient funds. $10 overdrafte fee assessed. \n"
                   f"New balance: {self.balance - 10}"))
    # reassign balance to reflect 10 overdraft
            self.balance = self.balance - 10
        else:
            self.balance = self.balance - withdrawal_amount
            print((f"Amount withdrawn: {withdrawal_amount} \n"
              f"New Balance: {self.balance}"))
        return self.balance
 
    def get_balance(self):
        print(f"Your current balance is: {self.balance}")

#     The print_statement method prints a message with the account name, account number, and balance like this:
# Joi Anderson
# Account No.: ****5678
# Balance: $100.00
    def print_statement(self):
        # Convert account number to string and format with asterisks
        account_str = str(self.account_number)
         # Get last 4 digits
        masked_account = '****' + account_str[-4:] 

        print((f"{self.full_name} \n"
         f"Account Number.: {masked_account} \n"
         f" Balance: {self.balance} "))
# need to format balance when it prints and maybe set as float?

# Then define the following methods for the BankAccount class:

#     The add_interest method adds interest to the users balance. The annual interest rate is 1% (i.e. 0.083% per month). Thus, the monthly interest is calculated by the following equation: interest = balance *  0.00083 .



# Outside of the BankAccount class, define 3 different bank account examples using the BankAccount() object.

#     Your examples should show you using the different methods above to demonstrate them working.

# Include example code to do the following:

#     Create a new bank account instance: user: "Mitchell", account number: 03141592.
#     Deposit $400,000 into "Mitchell's" account.
#     Print a statement
#     Add interest to the account
#     Print a statement
#     Make a withdrawl of $150 (Mitchell needs some Yeezy's)
#     Print a statement

mitchell = BankAccount("Mitchell", "03141592")
mitchell.deposit(400000)
mitchell.print_statement()

