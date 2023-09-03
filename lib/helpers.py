from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Product, Supplier, Employee, Task, Shipment
from tabulate import tabulate

# Connect to the database
engine = create_engine('sqlite:///warehouse.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_product(session, name, inventory_quantity):
    try:
        product = Product(name=name, inventory_quantity=inventory_quantity)
        session.add(product)
        session.commit()
        return True, "Product added successfully!"
    except Exception as e:
        session.rollback()
        return False, str(e)
    
def add_employee(session, name):
    try:
        employee = Employee(name=name)
        session.add(employee)
        session.commit()
        return True, "Employee added successfully!"
    except Exception as e:
        session.rollback()
        return False, str(e)

def list_products(session):
    products = session.query(Product).all()
    if products:
        product_data = [(product.id, product.name, product.inventory_quantity) for product in products]
        headers = ["ID", "Name", "Inventory Quantity"]
        table = tabulate(product_data, headers, tablefmt="grid")
        print(table)
    else:
        print("No products found.")
