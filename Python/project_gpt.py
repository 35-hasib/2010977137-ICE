import csv

class Restaurant:
    def __init__(self, menu_file="menu.csv"):
        self.menu_file = menu_file  # CSV file to store menu items
        self.menu = {}  # Dictionary to store menu items and prices
        self.order = {}  # Dictionary to store orders
        self.load_menu()  # Load menu from CSV on initialization

    def load_menu(self):
        """Load the menu from the CSV file."""
        try:
            with open(self.menu_file, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    item_name, price, quantity = row
                    self.menu[item_name] = [float(price), int(quantity)]
        except FileNotFoundError:
            print(f"{self.menu_file} not found. Starting with an empty menu.")

    def save_menu(self):
        """Save the menu to the CSV file."""
        with open(self.menu_file, mode="w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Item Name", "Price", "Quantity"])  # Writing header
            for item, pq in self.menu.items():
                writer.writerow([item, pq[0], pq[1]])

    def manage_menu(self):
        while True:
            print("\nMenu Management:")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Item Price")
            print("4. View Menu")
            print("5. Save and Exit Management")
            
            try:
                choice = int(input("Enter your choice: "))
                
                if choice == 1:  # Add Item
                    item_name = input("Enter item name: ").strip().title()
                    if item_name in self.menu:
                        print("Item already exists in the menu!")
                        continue
                    price = float(input("Enter item price: "))
                    quantity = int(input("Enter item quantity: "))
                    self.menu[item_name] = [price,quantity]
                    print(f"Item '{item_name}' added successfully!")

                elif choice == 2:  # Remove Item
                    item_name = input("Enter item name to remove: ").strip().title()
                    if item_name in self.menu:
                        del self.menu[item_name]
                        print(f"Item '{item_name}' removed successfully!")
                    else:
                        print(f"Error: Item '{item_name}' not found in the menu.")

                elif choice == 3:  # Update Item Price and quantity
                    item_name = input("Enter item name to update: ").strip().title()
                    if item_name in self.menu:
                        price = float(input(f"Enter new price for '{item_name}': "))
                        quantity = int(input(f"Enter new quantity for '{item_name}': "))
                        self.menu[item_name] = [price, quantity]
                        print(f"Price and quantity of '{item_name}' updated successfully!")
                    else:
                        print(f"Error: Item '{item_name}' not found in the menu.")

                elif choice == 4:  # View Menu
                    if not self.menu:
                        print("The menu is empty!")
                    else:
                        print("\nCurrent Menu:")
                        for item, pq in self.menu.items():
                            print(f"{item}: ${pq[0]:.2f}: {pq[1]}")
                
                elif choice == 5:  # Save and Exit Management
                    self.save_menu()  # Save changes to CSV before exiting
                    break

                else:
                    print("Invalid choice. Please try again.")
            
            except ValueError:
                print("Error: Please enter a valid number.")

    def take_order(self):
        if not self.menu:
            print("The menu is empty. Please add items before taking orders.")
            return
        
        print("\nCurrent Menu:")
        for item, pq in self.menu.items():
            print(f"{item}: ${pq[0]:.2f}: {pq[1]}")
        
        while True:
            try:
                item_name = input("Enter item name to order (or 'done' to finish): ").strip().title()
                if item_name.lower() == 'done':
                    break
                
                if item_name not in self.menu:
                    print(f"Error: '{item_name}' is not available on the menu.")
                    continue
                
                quantity = int(input(f"Enter quantity for '{item_name}': "))
                if quantity > self.menu[item_name][1]:
                    print(f"Error: Only {self.menu[item_name][1]} of '{item_name}' are available.")
                    continue
                
                self.menu[item_name][1] -= quantity  # Reduce the quantity in stock
                if item_name in self.order:
                    self.order[item_name] += quantity
                else:
                    self.order[item_name] = quantity
                print(f"'{item_name}' x {quantity} added to the order.")
            
            except ValueError:
                print("Error: Please enter a valid number for quantity.")

    def calculate_bill(self):
        if not self.order:
            print("No items in the order. Please take an order first.")
            return
        
        print("\nOrder Summary:")
        subtotal = 0
        for item, quantity in self.order.items():
            price = self.menu[item][0]  # Corrected access to price
            item_total = price * quantity
            subtotal += item_total
            print(f"{item} x {quantity} = ${item_total:.2f}")
        
        # Calculate tax and service charge
        tax = subtotal * 0.05
        service_charge = subtotal * 0.10
        total = subtotal + tax + service_charge
        
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Tax (5%): ${tax:.2f}")
        print(f"Service Charge (10%): ${service_charge:.2f}")
        print(f"Total: ${total:.2f}")
        
        # Clear the order after calculating the bill
        self.order.clear()

    def run(self):
        while True:
            print("\nRestaurant System:")
            print("1. Manage Menu")
            print("2. Take Order")
            print("3. Calculate Bill")
            print("4. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.manage_menu()
                elif choice == 2:
                    self.take_order()
                elif choice == 3:
                    self.calculate_bill()
                elif choice == 4:
                    print("Exiting... Thank you!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Error: Please enter a valid number.")

if __name__ == "__main__":
    restaurant = Restaurant()
    restaurant.run()
