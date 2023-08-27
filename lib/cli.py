from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.helpers import (
    confirm_and_add_product, list_products,
    confirm_and_add_supplier, confirm_and_assign_task,
    clear_screen, get_positive_integer_input
)

class WarehouseInventoryCLI:
    def __init__(self):
        self.engine = create_engine('sqlite:///db/warehouse_inventory.db')  # Update the path to your database
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.main_menu()
