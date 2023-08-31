from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Product, Supplier, Employee, Task, Shipment

# Connect to the database
engine = create_engine('sqlite:///warehouse.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_product(name, inventory_quantity):
    new_product = Product(name=name, inventory_quantity=inventory_quantity)
    session.add(new_product)
    session.commit()
