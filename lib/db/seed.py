from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models import Base, Product, Supplier, Employee

engine = create_engine('sqlite:///db/warehouse_inventory.db')  
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine) 

 