from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    inventory_quantity = Column(Integer, default=0)
    shipments = relationship('Shipment', back_populates='product')

    def __init__(self, name, inventory_quantity):
        self.name = name
        self.inventory_quantity = inventory_quantity


class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    products = relationship('Product', secondary='supplier_product')

    def __init__(self, name):
        self.name = name


supplier_product = Table(
    'supplier_product',
    Base.metadata,
    Column('supplier_id', Integer, ForeignKey('suppliers.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    tasks = relationship('Task', order_by='Task.id', back_populates='employee')

    def __init__(self, name):
        self.name = name


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    employee = relationship('Employee', back_populates='tasks')

    def __init__(self, description, employee):
        self.description = description
        self.employee = employee


class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', back_populates='shipments')
    quantity = Column(Integer, nullable=False)

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


engine = create_engine('sqlite:///lib/db/warehouse.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()