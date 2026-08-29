inventory = {}

def add_product():
    name = input("Enter product name: ").strip().lower()
    if name in inventory:
        print("Product already exists. Use update instead.")
        return
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    inventory[name] = {"price": price, "quantity": quantity}
    print(f"Product '{name}' added.")

def update_product():
    name = input("Enter product name to update: ").strip().lower()
    if name in inventory:
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))
        inventory[name] = {"price": price, "quantity": quantity}
        print("Product updated.")
    else:
        print("Product not found.")

def remove_product():
    name = input("Enter product name to remove: ").strip().lower()
    if name in inventory:
        inventory.pop(name)
        print(f"Product '{name}' removed.")
    else:
        print("Product not found.")

def check_low_stock(threshold=2):
    print("\n--- Low Stock Products ---")
    found = False
    for name, details in inventory.items():
        if details["quantity"] <= threshold:
            print(f"{name}: {details['quantity']} left")
            found = True
    if not found:
        print("All products are sufficiently stocked.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n--- Inventory List ---")
    for name, details in inventory.items():
        print(f"{name}: Price = ${details['price']:.2f}, Quantity = {details['quantity']}")

def inventory_menu():
    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Product\n2. Update Product\n3. Remove Product\n4. View Inventory\n5. Check Low Stock\n6. Exit")
        choice = input("Choose (1-6): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            check_low_stock()
        elif choice == "6":
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid choice.")

inventory_menu()
