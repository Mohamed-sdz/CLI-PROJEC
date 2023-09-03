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

def list_suppliers(session):
    suppliers = session.query(Supplier).all()
    if suppliers:
        supplier_data = [(supplier.id, supplier.name) for supplier in suppliers]
        headers = ["ID", "Name"]
        table = tabulate(supplier_data, headers, tablefmt="grid")
        print(table)
    else:
        print("No suppliers found.")

def add_shipment(session, quantity):
    try:
        shipment = Shipment(quantity=quantity)
        session.add(shipment)
        session.commit()
        return True, "Shipment added successfully!"
    except Exception as e:
        session.rollback()
        return False, str(e)

def list_shipments(session):
    shipments = session.query(Shipment).all()
    if shipments:
        shipment_data = [(shipment.id, shipment.quantity) for shipment in shipments]
        headers = ["ID", "Quantity"]
        table = tabulate(shipment_data, headers, tablefmt="grid")
        print(table)
    else:
        print("No shipments found.")

def update_product(session, product_id, name=None, inventory_quantity=None):
    try:
        product = session.query(Product).filter_by(id=product_id).first()
        if not product:
            return False, "Product not found."

        if name:
            product.name = name
        if inventory_quantity is not None:
            product.inventory_quantity = inventory_quantity

        session.commit()
        return True, "Product information updated successfully."
    except Exception as e:
        session.rollback()
        return False, str(e)

def update_employee(session, employee_id, name=None):
    try:
        employee = session.query(Employee).filter_by(id=employee_id).first()
        if not employee:
            return False, "Employee not found."

        if name is not None:
            employee.name = name

        session.commit()
        return True, "Employee information updated successfully."
    except Exception as e:
        session.rollback()
        return False, str(e)

def update_shipment(session, shipment_id, quantity=None):
    try:
        shipment = session.query(Shipment).filter_by(id=shipment_id).first()
        if not shipment:
            return False, "Shipment not found."

        if quantity is not None:
            shipment.quantity = quantity

        session.commit()
        return True, "Shipment information updated successfully."
    except Exception as e:
        session.rollback()
        return False, str(e)

def delete_product(session, product_id):
    try:
        product = session.query(Product).filter_by(id=product_id).first()
        if not product:
            return False, "Product not found."

        product.suppliers.clear()
        product.employees.clear()
        product.shipments.clear()

        session.delete(product)
        session.commit()
        return True, "Product deleted successfully."
    except Exception as e:
        session.rollback()
        return False, str(e)

def delete_employee(session, employee_id):
    try:
        employee = session.query(Employee).filter_by(id=employee_id).first()
        if not employee:
            return False, "Employee not found."

        for product in employee.products:
            product.employees.remove(employee)

        session.delete(employee)
        session.commit()
        return True, "Employee deleted successfully."
    except Exception as e:
        session.rollback()
        return False, str(e)

def delete_supplier(session, supplier_id):
    try:
        supplier = session.query(Supplier).filter_by(id=supplier_id).first()
        if not supplier:
            return False, "Supplier not found."

        for product in supplier.products:
            product.suppliers.remove(supplier)

        session.delete(supplier)
        session.commit()
        return True, "Supplier deleted successfully."
    except Exception as e:
        session.rollback()
        return False, str(e)

def delete_shipment(session, shipment_id):
    try:
        shipment = session.query(Shipment).filter_by(id=shipment_id).first()
        if not shipment:
            return False, "Shipment not found."

        for product in shipment.products:
            product.shipments.remove(shipment)

        session.delete(shipment)
        session.commit()
        return True, "Shipment deleted successfully."
    except Exception as e:
        session.rollback()
        return False, str(e)

