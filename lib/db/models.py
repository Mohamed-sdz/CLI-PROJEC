from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)

    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

 
class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)

    products = relationship('Product', backref='supplier')

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String) 
 
class Shipment(Base):
    __tablename__ = 'shipments'

    id = Column(Integer, primary_key=True)
    shipping_date = Column(String)
    delivery_date = Column(String)

    employees = relationship('Employee', secondary='shipment_employees')

class ShipmentEmployee(Base):
    __tablename__ = 'shipment_employees'

    id = Column(Integer, primary_key=True)
    shipment_id = Column(Integer, ForeignKey('shipments.id'))
    employee_id = Column(Integer, ForeignKey('employees.id'))

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    assignee_id = Column(Integer, ForeignKey('employees.id'))

    assignee = relationship('Employee')
    