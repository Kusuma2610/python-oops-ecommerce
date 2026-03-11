from models.user import PrimeUser
from models.product import Product
from models.cart import Cart
from models.order import Order
from payments.payment import CardPayment,UPIPayment
user1=PrimeUser("kussuma","kusuma@gmail.com","Active")
laptop=Product("Laptop",5000)
mouse=Product("Mouse",800)
cart1=Cart()
cart1.add_product(laptop,1)
cart1.add_product(mouse,2)
order1=Order(user1,cart1)
total_amount=order1.place_order()
payment_method=UPIPayment()
payment_method.pay(total_amount)
