class InsufficientFundsException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient funds. Withdrawal not allowed.")
        self.balance -= amount


try:
    account1 = BankAccount(1001, "Alice", 1000.0)
    
    account1.withdraw(2000.0)  # Successful withdrawal
    
    # Print updated balances
    print("Account 1 Balance:", account1.get_balance())
except InsufficientFundsException as ex:
    print("Exception:", ex)

