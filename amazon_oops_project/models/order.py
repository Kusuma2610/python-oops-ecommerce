class Order:
    def __init__(self,user,cart):
        self.user=user
        self.cart=cart
    def place_order(self):
     total=self.cart.calculate_total()
     print("order placed by:",self.user.name)
     print("order details:")
     for product,quantity in self.cart.items:
        print(f"{product.name}x{quantity}={product.get_price()*quantity}")
        total=self.cart.calculate_total()
        print("total amount:",total)
        return total