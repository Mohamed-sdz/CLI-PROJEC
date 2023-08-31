

from helpers import add_product, add_employee

def main():
    print("Welcome to my Warehouse Inventory CLI")
    
    while True:
        print("\nSelect an option:")
        print("1. Add Product")
        print("2. Add Employee")
choice = input("Enter your choice: ")
        
if choice == "1":
            name = input("Enter product name: ")
            inventory_quantity = int(input("Enter inventory quantity: "))
            add_product(name, inventory_quantity)
            print("Product added successfully!")
elif choice == "2":
            name = input("Enter employee name: ")
            add_employee(name)
            print("Employee added successfully!")






      


if __name__ == "__main__":
    main()
