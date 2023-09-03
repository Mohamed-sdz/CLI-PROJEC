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

def add_task(session, description, employee_id):
    try:
        task = Task(description=description, employee_id=employee_id)
        session.add(task)
        session.commit()
        return True, "Task added successfully!"
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

def list_employees(session):
    employees = session.query(Employee).all()
    if employees:
        employee_data = [(employee.id, employee.name) for employee in employees]
        headers = ["ID", "Name"]
        table = tabulate(employee_data, headers, tablefmt="grid")
        print(table)
    else:
        print("No employees found.")

def list_tasks(session):
    tasks = session.query(Task).all()
    if tasks:
        task_data = [(task.id, task.description, task.employee_id) for task in tasks]
        headers = ["ID", "Description", "Employee ID"]
        table = tabulate(task_data, headers, tablefmt="grid")
        print(table)
    else:
        print("No tasks found.")

def add_supplier(session, name):
    try:
        supplier = Supplier(name=name)
        session.add(supplier)
        session.commit()
        return True, "Supplier added successfully!"
    except Exception as e:
        session.rollback()
        return False, str(e)

