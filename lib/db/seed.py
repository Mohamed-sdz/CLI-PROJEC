from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Supplier, Product, Employee, Shipment, Task

# Define the database engine
engine = create_engine('sqlite:///warehouse.db')

# Create a session for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()

# Seed data for Suppliers
suppliers_data = [
    {"name": "Supplier A"},
    {"name": "Supplier B"},
    {"name": "Supplier C"},
]

# Seed data for Products, including inventory_quantity
products_data = [
    {"name": "Product 1", "inventory_quantity": 100},
    {"name": "Product 2", "inventory_quantity": 50},
    {"name": "Product 3", "inventory_quantity": 75},
]

# Seed data for Employees
employees_data = [
    {"name": "Employee 1"},
    {"name": "Employee 2"},
    {"name": "Employee 3"},
]

# Seed data for Shipments
shipments_data = [
    {"quantity": 100},
    {"quantity": 200},
    {"quantity": 150},
]

# Seed data for Tasks
tasks_data = [
    {"description": "Task 1", "employee": Employee(name="Employee 1")},
    {"description": "Task 2", "employee": Employee(name="Employee 2")},
    {"description": "Task 3", "employee": Employee(name="Employee 3")},
]

# Populate the database with seeded data

# Seed Suppliers
for supplier_info in suppliers_data:
    supplier = Supplier(**supplier_info)
    session.add(supplier)

# Seed Products
for product_info in products_data:
    product = Product(**product_info)
    session.add(product)

# Seed Employees
for employee_info in employees_data:
    employee = Employee(**employee_info)
    session.add(employee)

# Seed Shipments
for shipment_info in shipments_data:
    shipment = Shipment(**shipment_info)
    session.add(shipment)

# Seed Tasks
for task_info in tasks_data:
    task = Task(**task_info)
    session.add(task)

# Commit the changes to the database
session.commit()

# Close the session
session.close()

# Print a message to indicate successful seeding
print("Sample data seeded successfully.")
