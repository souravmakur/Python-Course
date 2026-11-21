# D. Abstraction
# Abstraction means hiding implementation details and exposing only what is necessary.
# Python uses the abc module to implement formal abstraction through abstract classes.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")

p = UPI()
p.pay(500)

nb = NetBanking()
nb.pay(1000)