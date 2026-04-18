class bank_account:
    def __init__(self,name,account_number,balance=0):
        self.__name = name  # __name Private attribute
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposit {amount} successful. New balance: {self.__balance}")

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrawal {amount} successful. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

# Example usage
account1 = bank_account("Alice", "123456789", 1000)
print(f"Initial balance: {account1.get_balance()}")
account1.deposit(500)
account1.withdraw(200)
print(f"Final balance: {account1.get_balance()}")