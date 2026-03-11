from abc import ABC, abstractmethod
class Payment:
    @abstractmethod
    def pay(self,amount):
        pass
class CardPayment(Payment):
    def pay(self,amount):
        print("paid",amount,"using card")
class UPIPayment(Payment):
    def pay(self,amount):
        print("paid",amount,"using UPI")