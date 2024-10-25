# Define a BankAccount class.
# A bank account should have the following attributes:

#     full_name - the full name of the bank account account owner.
#     account_number - randomly generated 8 digit number, unique per account.
#     balance - the balance of money in the account, should start at 0.
# Then define the following methods for the BankAccount class:

#     The deposit method will take one parameter amount and will add amount to the balance. Also, it will print the message: “Amount deposited: $X.XX new balance: $Y.YY”
#     The withdraw method will take one parameter amount and will subtract amount from the balance. Also, it will print a message, like “Amount withdrawn: $X.XX new balance: $Y.YY”. If the user tries to withdraw an amount that is greater than the current balance, print ”Insufficient funds.” and charge them with an overdraft fee of $10
#     The get_balance method will print a user-friendly message with the account balance and then also return the current balance of the account.
#     The add_interest method adds interest to the users balance. The annual interest rate is 1% (i.e. 0.083% per month). Thus, the monthly interest is calculated by the following equation: interest = balance *  0.00083 .
#     The print_statement method prints a message with the account name, account number, and balance like this:

# Joi Anderson
# Account No.: ****5678
# Balance: $100.00

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

