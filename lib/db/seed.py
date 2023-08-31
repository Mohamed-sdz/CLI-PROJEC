from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product, Supplier, Employee, Task, Shipment

# Create the engine and session
engine = create_engine('sqlite:///warehouse.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
def seed_data():
    # Create suppliers
    supplier1 = Supplier(name='Supplier 1')
    supplier2 = Supplier(name='Supplier 2')

    # Create products
    product1 = Product(name='Product 1', inventory_quantity=10)
    product2 = Product(name='Product 2', inventory_quantity=5)
    product3 = Product(name='Product 3', inventory_quantity=8)

    # Associate products with suppliers
    supplier1.products.extend([product1, product2])
    supplier2.products.append(product3)

    # Create employees
    employee1 = Employee(name='Employee 1')
    employee2 = Employee(name='Employee 2')

    # Create tasks for employees
    task1 = Task(description='Task 1', employee=employee1)
    task2 = Task(description='Task 2', employee=employee1)
    task3 = Task(description='Task 3', employee=employee2)

    # Create shipments
    shipment1 = Shipment(product=product1, quantity=3)
    shipment2 = Shipment(product=product2, quantity=2)
    shipment3 = Shipment(product=product3, quantity=4)

    # Add objects to the session
    session.add_all([supplier1, supplier2, product1, product2, product3,
                     employee1, employee2, task1, task2, task3,
                     shipment1, shipment2, shipment3])

    # Commit the changes
    session.commit()
    
    print("Sample data seeded successfully.")

if __name__ == '__main__':
    seed_data()