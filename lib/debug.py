from db.models import Base, Product, Supplier, Employee, Task, Shipment
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import ipdb

if __name__=='__main__':
    engine = create_engine('sqlite:///warehouse.db')
    
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()