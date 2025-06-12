# main.py

from product import Product
from product_manager import ProductManager

pm = ProductManager()

# Dodavanje nekoliko proizvoda
pm.add_product(Product("Laptop", 1000, 5))
pm.add_product(Product("Phone", 500, 10))
pm.add_product(Product("Tablet", 300, 7))

# Prikaz svih proizvoda
pm.display_all_products()

# Prikaz ukupne vrednosti inventara
print("Total Inventory Value:", pm.total_inventory_value())