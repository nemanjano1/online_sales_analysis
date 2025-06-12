# main.py

from product import Product
from product_manager import ProductManager

pm = ProductManager()

# Dodavanje nekoliko proizvoda
pm.add_product(Product("Laptop", 1000, 5))
pm.add_product(Product("Phone", 500, 10))
pm.add_product(Product("Tablet", 300, 7))
pm.add_product(Product("Gaming Laptop", 1500, 3))
pm.add_product(Product("Smartphone", 600, 8))
pm.add_product(Product("E-Reader", 200, 12))


from cart import Cart
import random

# Inicijalizacija korpe
cart = Cart()

# Izbor 3 nasumična proizvoda iz liste
selected_products = random.sample(pm.products, 3)
for product in selected_products:
    cart.add_to_cart(product)

# Prikaz sadržaja korpe i ukupne vrednosti
cart.display_cart()
print("Total cart value:", cart.calculate_total())

