from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models import Base, Product, Supplier, Employee

engine = create_engine('sqlite:///db/warehouse_inventory.db')  
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine) 

 # Products
iphone = Product(name="Galaxy 23", price=899)
macbook = Product(name="MacBook Pro 16", price=2399) 

# Suppliers            
apple = Supplier(name="Apple Inc.", email="sales@apple.com")
samsung = Supplier(name="Samsung Electronics", email="sales@samsung.com")

# Employees
john = Employee(name="John Smith", role="Sales Manager")
jane = Employee(name="Jane Lee", role="Sales Representative")

session.add_all([iphone, macbook, apple, samsung, john, jane])
session.commit()

print("Seeded database successfully")