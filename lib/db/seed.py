from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product, Supplier, Employee

engine = create_engine('sqlite:///db/warehouse_inventory.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

apple = Supplier(name="Apple Inc.", location="CA, United States")
samsung = Supplier(name="Samsung Electronics", location="Seoul, South Korea")

iphone = Product(name="iPhone 12", description="Smartphone", price=799, supplier=apple)
galaxy = Product(name="Galaxy S21", description="Smartphone", price=899, supplier=samsung)

john = Employee(name="John Smith", department="Sales Manager")
jane = Employee(name="Jane Lee", department="Warehouse Worker")

session.add_all([apple, samsung, iphone, galaxy, john, jane])
session.commit()

print("Seeded database successfully")
