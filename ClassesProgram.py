import pickle

customers = {}
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance

def save_customers_to_file():
    with open("customers.pkl", "wb") as file:
        pickle.dump(customers, file)

def load_customers_from_file():
    global customers
    try:
        with open("customers.pkl", "rb") as file:
            customers = pickle.load(file)
    except (FileNotFoundError, EOFError):
        customers = {}

def add_customer():
    name = input("Enter Name [First - Last]: ")
    if name in customers:
        print("Customer already exists.")
    else:
        balance = float(input("Enter initial balance: "))
        # noinspection PyTypeChecker
        customers[name] = BankAccount(name, balance)
        print(f"{name} has ${customers[name].get_balance():,.2f} in their account.")
    save_customers_to_file()

def look_up_customer():
    name = input("Enter Name [First - Last] to look up: ")
    if name in customers:
        print(f"{name} has ${customers[name].get_balance():,.2f} in their account.")
    else:
        print("Customer not found.")

def edit_customer():
    name = input("Enter Name [First - Last] to edit: ")
    if name in customers:
        new_balance = float(input("Enter new balance: "))
        customers[name].balance = new_balance
        print(f"{name}'s balance updated to ${new_balance:,.2f}")
    else:
        print("Customer not found.")
    save_customers_to_file()

def deposit():
    name = input("Enter Name [First - Last]: ")
    if name in customers:
        amount = float(input("Enter amount to deposit: "))
        customers[name].deposit(amount)
        print(f"Deposited ${amount:,.2f} to {name}'s account.")
    else:
        print("Customer not found.")
    save_customers_to_file()

def withdraw():
    name = input("Enter Name [First - Last]: ")
    if name in customers:
        amount = float(input("Enter amount to withdraw: "))
        if customers[name].balance >= amount:
            customers[name].withdraw(amount)
            print(f"Withdrew ${amount:,.2f} from {name}'s account.")
        else:
            print("Insufficient balance.")
    else:
        print("Customer not found.")
    save_customers_to_file()

def delete_customer():
    name = input("Enter Name [First - Last] to delete: ")
    if name in customers:
        del customers[name]
        print(f"{name} has been deleted from the records.")
    else:
        print("Customer not found.")
    save_customers_to_file()

def main():
    load_customers_from_file()
    while True:
        print(
            "\nMenu:\n1. Add Customer\n2. Look up Customer\n3. Edit Customer\n4. Deposit\n5. Withdraw\n6. Delete\n7. Quit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_customer()
        elif choice == 2:
            look_up_customer()
        elif choice == 3:
            edit_customer()
        elif choice == 4:
            deposit()
        elif choice == 5:
            withdraw()
        elif choice == 6:
            delete_customer()
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()