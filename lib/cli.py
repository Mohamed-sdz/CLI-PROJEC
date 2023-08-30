from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.helpers import (
    confirm_and_add_product, list_products,
    confirm_and_add_supplier, confirm_and_assign_task,
    clear_screen, get_positive_integer_input
)

class WarehouseInventoryCLI:
    def __init__(self):
        self.engine = create_engine('sqlite:///db/warehouse_inventory.db')  
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.main_menu()

def main_menu(self):
        while True:
            clear_screen()
            print("Welcome to Warehouse Inventory Management CLI!")
            print("1. Add Product")
            print("2. List Products")
            print("3. Add Supplier")
            print("4. Assign Task")
            print("5. Exit")

# lib/db/helpers.py

from lib.db.models import Product, Supplier, Task
from lib.db import session
from ranges import Range
import tuples

def add_product(name, quantity_range, supplier_id):
  """Add a new product to the database"""

  # Use range for quantity
  quantity_range = Range.from_tuple(quantity_range)

  new_product = Product(name=name, quantity=quantity_range, supplier_id=supplier_id)

  session.add(new_product)
  session.commit()

def list_products():
  """List all products in the database"""

  # Use tuple for query results
  products = session.query(Product).all()

  results = [(product.id, product.name, product.quantity) for product in products]

  print(f"Found {len(results)} products:")

  for id, name, quantity in results:
    print(f"{id}: {name} - {quantity}")

def add_supplier(name, products):
  """Add a new supplier to the database"""

  # Tuple for initial products
  products = tuples.from_list(products)

  new_supplier = Supplier(name=name, products=products)

  session.add(new_supplier)
  session.commit()

def assign_task(employee_id, description):
  """Assign a new task to an employee"""

  new_task = Task(employee_id=employee_id, description=description)

  session.add(new_task)
  session.commit()