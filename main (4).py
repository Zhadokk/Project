from datetime import datetime

class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

class Employee(Person):
    def __init__(self, name, contact, employee_id):
        super().__init__(name, contact)
        self.employee_id = employee_id

    def display_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Contact: {self.contact}"

class Manager(Employee):
    def create_menu_item(self, menu, name, price):
        menu.add_item(name, price)
        print(f"Menu item {name} added.")

class Chef(Employee):
    def prepare_order(self, order):
        print(f"Order with items {[item.name for item in order.items]} is being prepared.")

class Waiter(Employee):
    def take_order(self, customer, menu):
        print(f"Taking order for {customer.name}. Available items:")
        for item in menu.items:
            print(item)

class Customer(Person):
    pass

class Reservation:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, customer, time, people):
        self.reservations.append({'customer': customer, 'time': time, 'people': people})
        print(f"Reservation added for {customer.name} at {time} for {people} people.")

    def view_reservations(self):
        if not self.reservations:
            print("No reservations.")
        for res in self.reservations:
            print(f"Reservation for {res['customer'].name} at {res['time']} for {res['people']} people.")

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append(MenuItem(name, price))

    def display_menu(self):
        for item in self.items:
            print(item)

class Order:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item):
        self.items.append(item)
        self.total += item.price

    def receipt(self):
        receipt_lines = [f"{item.name}: ${item.price}" for item in self.items]
        receipt_lines.append(f"Total: ${self.total}")
        return "\n".join(receipt_lines)

class CLI:
    def __init__(self):
        self.menu = Menu()
        self.reservation_system = Reservation()
        self.manager = Manager("Zhadra", "874765364", 101)
        self.customers = [Customer("Marzhan", "12345678")]

    def get_input(self, prompt, type_=str, min_value=None, max_value=None):
        """Generic input function with error handling."""
        while True:
            try:
                value = type_(input(prompt))
                if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                    raise ValueError(f"Value must be between {min_value} and {max_value}.")
                return value
            except ValueError as e:
                print(f"Invalid input: {e}")

    def display_main_menu(self):
        options = "\n1. Add Menu Item\n2. Make a Reservation\n3. View Reservations\n4. Take an Order\n5. Exit"
        choice = self.get_input(options + "\nEnter choice: ", int, 1, 5)
        return choice

    def run(self):
        while True:
            choice = self.display_main_menu()
            if choice == 1:
                name = self.get_input("Enter menu item name: ", str)
                price = self.get_input("Enter price: ", float, 0)
                self.manager.create_menu_item(self.menu, name, price)
            elif choice == 2:
                customer_name = self.get_input("Enter customer name: ", str)
                time = self.get_input("Enter time of reservation (e.g., '7 PM'): ", str)
                people = self.get_input("Number of people: ", int, 1)
                customer = Customer(customer_name, "Unknown")
                self.reservation_system.add_reservation(customer, time, people)
            elif choice == 3:
                self.reservation_system.view_reservations()
            elif choice == 4:
                self.menu.display_menu()
                order = Order()
                while True:
                    item_index = self.get_input("Enter item index to add to order (or -1 to finish): ", int, -1, len(self.menu.items) - 1)
                    if item_index == -1:
                        break
                    order.add_item(self.menu.items[item_index])
                print(order.receipt())
            elif choice == 5:
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()
