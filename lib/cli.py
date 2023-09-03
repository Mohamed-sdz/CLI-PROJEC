import click
import inquirer
from helpers import (
    add_product, add_employee, list_products, list_employees, list_tasks,
    add_supplier, list_suppliers, add_shipment, list_shipments,
    update_product, update_employee, update_shipment,
    delete_product, delete_employee, delete_supplier, delete_shipment,
    search_products_by_name, search_employees_by_name, filter_products_low_inventory
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    click.echo("Welcome to my Warehouse Inventory CLI")

engine = create_engine('sqlite:///warehouse.db')
Session = sessionmaker(bind=engine)
session = Session()