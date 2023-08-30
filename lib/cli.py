from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.helpers import (
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

 