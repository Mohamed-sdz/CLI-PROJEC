# Warehouse Inventory CLI

Welcome to the Warehouse Inventory CLI, a command-line tool for managing product, employee, supplier, and shipment , task , information in your warehouse.

## VIDEO DEMO:  <https://clipchamp.com/watch/HvE8g0t11IC>

## Features

1- Add new products with their inventory quantities.
2- Add and manage employees.
3- Add and manage suppliers.
4- Add and manage shipments.
5- Update product, employee, and shipment information.
6- Delete products, employees, suppliers, and shipments.
7- Search for products and employees by name.
8- Filter products by low inventory.

## Prerequisites

Before using this CLI, make sure you have the following tools and Python packages installed:

- Python 3.8 or higher
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Tabulate](https://pypi.org/project/tabulate/)
- [Click](https://click.palletsprojects.com/en/8.0.x/)
- [Inquirer](https://pypi.org/project/inquirer/)
- [ipdb](https://pypi.org/project/ipdb/)

## Installation

1. Clone this repository:
 git clone <https://github.com/Mohamed-sdz/CLI-PROJEC.git>
   cd warehouse-inventory-cli

1.Install the required Python packages using Pipenv:
    "pipenv install"
2.Create the database and run Alembic migrations:
    "pipenv shell"
    alembic upgrade head
3.Usage
    To start the Warehouse Inventory CLI, run the following command:
     "pipenv run python cli.py"

 You will be presented with a menu where you can select various options to manage your warehouse inventory.

 **Options**
**Add Product: Add a new product with its name and inventory quantity.
** Update Product: Update product information, including name and inventory quantity.
**Search Products: Search for products by name.
** Delete Product: Delete a product by its ID.
**Filter Products: Filter products by a specified inventory threshold.
** Add Employee: Add a new employee with their name.
**Update Employee: Update employee information, including name.
** Delete Employee: Delete an employee by their ID.
**Search Employees: Search for employees by name.
** Add Supplier: Add a new supplier with their name.
**Delete Supplier: Delete a supplier by their ID.
** Add Shipment: Add a new shipment with a specified quantity.
**Update Shipment: Update shipment information, including quantity.
** Delete Shipment: Delete a shipment by its ID.
**List Products: List all products in the warehouse.
** List Employees: List all employees in the warehouse.
**List Tasks: List all tasks in the warehouse.
** List Suppliers: List all suppliers in the warehouse.
**List Shipments: List all shipments in the warehouse.
** Exit: Exit the Warehouse Inventory CLI.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Thank you for using the Warehouse Inventory CLI! If you have any questions or need assistance, feel free to contact me at [didi.mousedidi@outlook.com].
