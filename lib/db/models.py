from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from tabulate import tabulate

# Define the database engine
engine = create_engine('sqlite:///warehouse.db')

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the association table for the many-to-many relationship between Supplier and Product
supplier_product_association = Table(
    'supplier_product_association',

    Base.metadata,
    Column('supplier_id', Integer, ForeignKey('suppliers.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

# Define the association table for the many-to-many relationship between Employee and Product
employee_product_association = Table(
    'employee_product_association',
    Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

# Define the association table for the many-to-many relationship between Product and Shipment
product_shipment_association = Table(
    'product_shipment_association',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('shipment_id', Integer, ForeignKey('shipments.id'))
)

# Define the Supplier class
class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
        self.products = set()

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("product must be of type Product")

        self.products.add(product)
        product.suppliers.add(self)

    def list_products(self):
        return list(self.products)

# Define the Product class
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    inventory_quantity = Column(Integer, default=0)  # Add inventory_quantity with a default value

    def __init__(self, name, inventory_quantity=0):
        self.name = name
        self.inventory_quantity = inventory_quantity
        self.suppliers = set()
        self.employees = set()
        self.shipments = set()

    def add_supplier(self, supplier):
        if not isinstance(supplier, Supplier):
            raise TypeError("supplier must be of type Supplier")

        self.suppliers.add(supplier)
        supplier.products.add(self)

    def list_suppliers(self):
        return list(self.suppliers)

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("employee must be of type Employee")

        self.employees.add(employee)
        employee.products.add(self)

    def list_employees(self):
        return list(self.employees)

    def add_shipment(self, shipment):
        if not isinstance(shipment, Shipment):
            raise TypeError("shipment must be of type Shipment")

        self.shipments.add(shipment)
        shipment.products.add(self)

    def list_shipments(self):
        return list(self.shipments)

# Define the Employee class
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tasks = relationship('Task', back_populates='employee')

    def __init__(self, name):
        self.name = name
        self.products = set()

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("product must be of type Product")

        self.products.add(product)
        product.employees.add(self)

    def list_products(self):
        return list(self.products)

# Define the Shipment class
class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    def __init__(self, quantity):
        self.quantity = quantity
        self.products = set()

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("product must be of type Product")

        self.products.add(product)
        product.shipments.add(self)

    def list_products(self):
        return list(self.products)

# Define the Task class
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    employee = relationship('Employee', back_populates='tasks')

    def __init__(self, description, employee):
        self.description = description
        self.employee = employee

    def __repr__(self):
        return f'Task(id={self.id}, ' + \
            f'description="{self.description}", ' + \
            f'employee_id={self.employee_id})'

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session for interacting with the database
Session = sessionmaker(bind=engine)
session = Session()
