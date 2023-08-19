items = []

def add_item():
    item_id = input("Enter item ID: ")
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))

    with open("items.txt", "a") as file:
        file.write(f"{item_id},{name},{price},{quantity}\n")

    print("Item added successfully.")

def search_item():
    search_id = input("Enter item ID to search: ")

    with open("items.txt", "r") as file:
        for line in file:
            item = line.strip().split(",")
            if item[0] == search_id:
                print("Item found:")
                print("ID:", item[0])
                print("Name:", item[1])
                print("Price:", item[2])
                print("Quantity:", item[3])
                return

    print("Item not found.")

def edit_item():
    edit_id = input("Enter item ID to edit: ")
    updated_items = []

    with open("items.txt", "r") as file:
        for line in file:
            item = line.strip().split(",")
            if item[0] == edit_id:
                name = input("Enter new name: ")
                price = float(input("Enter new price: "))
                quantity = int(input("Enter new quantity: "))
                item = [item[0], name, price, quantity]
                print("Item edited successfully.")
            updated_items.append(item)

    with open("items.txt", "w") as file:
        for item in updated_items:
            file.write(",".join(str(i) for i in item) + "\n")

    print("Item not found.") 
    

def delete_item():
    delete_id = input("Enter item ID to delete: ")
    deleted = False

    with open("items.txt", "r") as file:
        lines = file.readlines()

    with open("items.txt", "w") as file:
        for line in lines:
            item = line.strip().split(",")
            if item[0] != delete_id:
                file.write("\n" + line)
            else:
                deleted = True

    if deleted:
        print("Item deleted successfully.")
    else:
        print("Item not found.")

def show_items():
    items.clear()
    with open("items.txt", "r") as file:
        for line in file:
            product = line.split(",")
            dic = {"ID:": product[0], "Name:": product[1], "Price:": product[2], "Quantity:": product[3]}
            items.append(dic)
    print("Items in storage:")
    for obj in items:
        print(obj)

def exit_app():
    print("Exiting the app...")
    exit()

# Main loop
while True:
    print("Menu:")
    print("1. Add item")
    print("2. Search item")
    print("3. Edit item")
    print("4. Delete item")
    print("5. Show items")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        search_item()
    elif choice == '3':
        edit_item()
    elif choice == '4':
        delete_item()
    elif choice == '5':
        show_items()
    elif choice == '6':
        exit_app()
    else:
        print("Invalid choice. Please try again.")
