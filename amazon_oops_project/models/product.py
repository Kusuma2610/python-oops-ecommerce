class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    def get_price(self):
        return self.__price
    def display_product(self):
        print("product:",self.name)
        print("price:",self.__price)

