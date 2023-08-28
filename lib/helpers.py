import os
from collections import namedtuple
from lib.db.models import Product, Supplier, Task
from lib.db import session
from ranges import Range
import tuples

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Custom Tuple class
Tuple = namedtuple('Tuple', ['x', 'y'])

# Custom Range class
class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Function to get a positive integer input
def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid positive integer")

def add_product(name, quantity_range, supplier_id):
    quantity_range = Range(quantity_range[0], quantity_range[1])
    new_product = Product(name=name, quantity=quantity_range, supplier_id=supplier_id)
    session.add(new_product)
    session.commit()
def list_products():
    products = session.query(Product).all()
    results = [Tuple(product.id, product.name, product.quantity) for product in products]
    print(f"Found {len(results)} products:")
    for id, name, quantity in results:
        print(f"{id}: {name} - {quantity}")
def add_supplier(name, products):
    products = [Tuple(p[0], p[1]) for p in products]
    new_supplier = Supplier(name=name, products=products)
    session.add(new_supplier)
    session.commit()
def assign_task(employee_id, description):
    new_task = Task(employee_id=employee_id, description=description)
    session.add(new_task)
    session.commit()
def get_product(product_id):
    product = session.query(Product).get(product_id)
    return Tuple(product.id, product.name, product.quantity)
def update_product_quantity(product_id, new_quantity_range):
    product = session.query(Product).get(product_id)
    product.quantity = Range(new_quantity_range[0], new_quantity_range[1])
    session.commit()
def delete_product(product_id):
    session.query(Product).filter(Product.id == product_id).delete()
    session.commit()