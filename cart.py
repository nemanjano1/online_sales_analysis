# cart.py

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def calculate_total(self):
        return sum(p.price * p.quantity for p in self.cart_items)

    def display_cart(self):
        print("Cart contents:")
        for product in self.cart_items:
            print(f"{product.name} - ${product.price} x {product.quantity}")