class Cart:
    def __init__(self):
        self.items=[]
#adding product to Cart
    def add_product(self,product,quantity):
        self.items.append((product,quantity))
        print(product.name,"added to cart")
    def calculate_total(self):
        total=0
        for product,quantity in self.items:
            total+=product.get_price()*quantity
        return total

