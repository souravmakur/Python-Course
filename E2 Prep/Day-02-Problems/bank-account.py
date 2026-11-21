# BANK ACCOUNT
class BankAccount:
  def __init__(self, initial_balance):
    if initial_balance >= 0:
      self.__balance = float(initial_balance)
    else:
      print("Initial balance cannot be negative. Setting balance to 0.0")
      self.__balance = 0.0

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      print(f"Deposited: {amount}")
    else:
      print("Invalid deposit amount. Amount must be greater than 0.")

  def withdraw(self, amount):
    if amount <= 0:
      print("Invalid withdrawl amount, Withdrawl amount should be more than 0.0")
    elif amount > self.__balance:
      print(f"Insufficient funds! Cannot withdraw {amount}")
    else:
      self.__balance -= amount
      print(f"Withdraw: {amount}")

  def get_balance(self):
    return self.__balance


if __name__ == "__main__":
    account = BankAccount(10000.0)
    print(f"Initial Balance: {account.get_balance()}")

    account.deposit(500)
    print(f"After Deposit: {account.get_balance()}")

    account.withdraw(200)
    print(f"After Withdrawal: {account.get_balance()}")

    # Test exceeding available balance
    account.withdraw(15000)
    print(f"Final Balance: {account.get_balance()}")