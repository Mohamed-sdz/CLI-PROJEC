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

while True:
    questions = [
        inquirer.List(
            'choice',
            message="Select an option:",
            choices=[
                'Add Product',
                'Update Product',
                'Search Products',  
                'Delete Product',
                'Filter Products',
                'Add Employee',
                'Update Employee',
                'Delete Employee',
                'Search Employees',
                'Add Supplier',  
                'Delete Supplier',  
                'Add Shipment',
                'Update Shipment', 
                'Delete Shipment', 
                'List Products',
                'List Employees',
                'List Tasks',
                'List Suppliers',  
                'List Shipments',  
                'Exit',
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    choice = answers['choice']
    if choice == 'Add Product':
        name = click.prompt('Enter product name')
        inventory_quantity = click.prompt('Enter inventory quantity', type=int)
        success, message = add_product(session, name, inventory_quantity)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Update Product':  # Corrected indentation
        product_id = click.prompt('Enter product ID', type=int)
        name = click.prompt('Enter new product name (leave blank to keep the current name)', default='', show_default=False)
        inventory_quantity = click.prompt('Enter new inventory quantity (leave blank to keep the current quantity)', default='', show_default=False)
    elif choice == 'Search Products':  # New option
        name = click.prompt('Enter product name to search')
        products = search_products_by_name(session, name)
        if products:
            list_products(products)
        else:
            click.echo("No products found.")
        success, message = update_product(session, product_id, name=name or None, inventory_quantity=int(inventory_quantity) if inventory_quantity else None)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Delete Product':  # New option
        product_id = click.prompt('Enter product ID to delete', type=int)
        success, message = delete_product(session, product_id)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Filter Products':  # New option
        threshold = click.prompt('Enter inventory threshold to filter products', type=int)
        products = filter_products_low_inventory(session, threshold)
        if products:
            list_products(products)
        else:
            click.echo("No products found.")


    elif choice == 'Add Employee':
        name = click.prompt('Enter employee name')
        success, message = add_employee(session, name)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Update Employee':  # New option
        employee_id = click.prompt('Enter employee ID', type=int)
        name = click.prompt('Enter new employee name (leave blank to keep the current name)', default='', show_default=False)
        success, message = update_employee(session, employee_id, name=name or None)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Delete Employee':  # New option
        employee_id = click.prompt('Enter employee ID to delete', type=int)
        success, message = delete_employee(session, employee_id)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Search Employees':  # New option
        name = click.prompt('Enter employee name to search')
        employees = search_employees_by_name(session, name)
        if employees:
            list_employees(employees)
        else:
            click.echo("No employees found.")

    elif choice == 'Add Supplier':
        name = click.prompt('Enter supplier name')
        success, message = add_supplier(session, name)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Delete Supplier':  # New option
        supplier_id = click.prompt('Enter supplier ID to delete', type=int)
        success, message = delete_supplier(session, supplier_id)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")

    elif choice == 'Add Shipment':
        quantity = click.prompt('Enter shipment quantity', type=int)
        success, message = add_shipment(session, quantity)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Update Shipment':  # New option
        shipment_id = click.prompt('Enter shipment ID', type=int)
        quantity = click.prompt('Enter new shipment quantity (leave blank to keep the current quantity)', default='', show_default=False)
        success, message = update_shipment(session, shipment_id, quantity=int(quantity) if quantity else None)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'Delete Shipment':  # New option
        shipment_id = click.prompt('Enter shipment ID to delete', type=int)
        success, message = delete_shipment(session, shipment_id)
        if success:
            click.echo(message)
        else:
            click.echo(f"Error: {message}")
    elif choice == 'List Products':
        list_products(session)
    elif choice == 'List Employees':
        list_employees(session)
    elif choice == 'List Tasks':
        list_tasks(session)
    elif choice == 'List Suppliers':
        list_suppliers(session)
    elif choice == 'List Shipments':
        list_shipments(session)
    elif choice == 'Exit':
      click.echo("Thank you for using my Warehouse Inventory CLI") 
      break
    if __name__ == '__main__':
         main()


