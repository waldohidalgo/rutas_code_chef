class BankAccount :
    __accountNumber = None
    __accountHolder = None
    __balance = None
    
    def __init__(self, accountNumber, accountHolder): 
        BankAccount.__accountNumber = accountNumber
        BankAccount.__accountHolder = accountHolder
        BankAccount.__balance = 0
    
    def deposit(self , value): 
        BankAccount.__balance += value
        print(f"Deposited: ${value}")
        
    def withdraw(self , value): 
        BankAccount.__balance -= value
        print(f"Withdrawn: ${value}")

    def getAccountInfo(self):
        print(f"Account Number: {BankAccount.__accountNumber}");
        print(f"Account Holder: {BankAccount.__accountHolder}");
        print(f"Balance: ${BankAccount.__balance}"); 


# Write your code here
# Create a BankAccount object

# Perform deposits and withdrawals and display account info


# Display the final account information
