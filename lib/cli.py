

from helpers import add_product

def main():
    print("Welcome to my Warehouse Inventory CLI")
    
    while True:
        print("\nSelect an option:")
        print("1. Add Product")
choice = input("Enter your choice: ")
        
if choice == "1":
            name = input("Enter product name: ")
            inventory_quantity = int(input("Enter inventory quantity: "))
            add_product(name, inventory_quantity)
            print("Product added successfully!")





      


if __name__ == "__main__":
    main()
