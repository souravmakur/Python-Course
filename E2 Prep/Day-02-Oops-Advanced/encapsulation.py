# FOUR PILLARS OF OOPS:
# 1. Encapsulation
# Encapsulation means combining data and methods within a 
# class and controlling how data is accessed or modified.

# Python uses naming conventions to indicate access levels:
# Convention               #Meaning
# name                     #Public
# _name                    #Protected(convention)
# __name                   #Private(convention)

class BankAccount:
    def __init__(self,balance):
        self.__balance = balance  # Private attribute
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500