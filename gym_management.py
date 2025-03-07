import mysql.connector as sqm
from tabulate import tabulate

class GymManagement:
    def __init__(self):
        # Fill the entries according to your credentials
        self.db = sqm.connect(host="localhost", user="", passwd="", database="gymmanagement")
        self.cursor = self.db.cursor()

    def main_menu(self):
        while True:
            print("\nGYM MANAGEMENT SYSTEM\n")
            print("1. Customer Management")
            print("2. Trainer Management")
            print("3. Membership Plans")
            print("4. Payments & Finance")
            print("5. Exit\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.customer_menu()
            elif choice == "2":
                self.trainer_menu()
            elif choice == "3":
                self.membership_menu()
            elif choice == "4":
                self.payment_menu()
            elif choice == "5":
                print("Exiting system... Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")

    def customer_menu(self):
        while True:
            print("\nCUSTOMER MANAGEMENT\n")
            print("1. Add Customer")
            print("2. View Customers")
            print("3. Search Customer")
            print("4. Delete Customer")
            print("5. Back to Main Menu\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.view_customers()
            elif choice == "3":
                self.search_customer()
            elif choice == "4":
                self.delete_customer()
            elif choice == "5":
                break
            else:
                print("Invalid choice! Please try again.")

    def add_customer(self):
        name = input("Enter Name: ")
        while True:
            try:
                number = int(input("Enter mobile number (10 digits): "))
                if len(str(number)) == 10:
                    break
                else:
                    print("Invalid entry, please enter 10 digits.")
            except ValueError:
                print("Please enter a valid number.")
        
        address = input("Enter Address: ")
        plan = input("Enter Membership Plan: ")
        
        query = "INSERT INTO customers (Name, Number, Address, MembershipPlan) VALUES (%s, %s, %s, %s)"
        values = (name, number, address, plan)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Customer Successfully Added!")

    def view_customers(self):
        self.cursor.execute("SELECT * FROM customers")
        data = self.cursor.fetchall()
        print("\nCustomer List:")
        print(tabulate(data, headers=["ID", "Name", "Number", "Address", "Plan"], tablefmt="grid"))

    def search_customer(self):
        name = input("Enter Customer Name: ")
        query = "SELECT * FROM customers WHERE Name = %s"
        self.cursor.execute(query, (name,))
        data = self.cursor.fetchall()
        if data:
            print("\nCustomer Details:")
            print(tabulate(data, headers=["ID", "Name", "Number", "Address", "Plan"], tablefmt="grid"))
        else:
            print("No customer found with that name.")

    def delete_customer(self):
        name = input("Enter Customer Name to Delete: ")
        query = "DELETE FROM customers WHERE Name = %s"
        self.cursor.execute(query, (name,))
        self.db.commit()
        print("Customer Deleted Successfully.")

    def trainer_menu(self):
        while True:
            print("\nTRAINER MANAGEMENT\n")
            print("1. Add Trainer")
            print("2. View Trainers")
            print("3. Delete Trainer")
            print("4. Back to Main Menu\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_trainer()
            elif choice == "2":
                self.view_trainers()
            elif choice == "3":
                self.delete_trainer()
            elif choice == "4":
                break
            else:
                print("Invalid choice! Please try again.")

    def add_trainer(self):
        name = input("Enter Trainer's Name: ")
        while True:
            try:
                number = int(input("Enter mobile number (10 digits): "))
                if len(str(number)) == 10:
                    break
                else:
                    print("Invalid entry, please enter 10 digits.")
            except ValueError:
                print("Please enter a valid number.")

        address = input("Enter Address: ")
        query = "INSERT INTO trainers (Name, Number, Address) VALUES (%s, %s, %s)"
        values = (name, number, address)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Trainer Successfully Added!")

    def view_trainers(self):
        self.cursor.execute("SELECT * FROM trainers")
        data = self.cursor.fetchall()
        print("\nTrainer List:")
        print(tabulate(data, headers=["ID", "Name", "Number", "Address"], tablefmt="grid"))

    def delete_trainer(self):
        name = input("Enter Trainer Name to Delete: ")
        query = "DELETE FROM trainers WHERE Name = %s"
        self.cursor.execute(query, (name,))
        self.db.commit()
        print("Trainer Deleted Successfully.")

    def membership_menu(self):
        while True:
            print("\nMEMBERSHIP PLANS\n")
            print("1. Add Membership Plan")
            print("2. View Membership Plans")
            print("3. Delete Membership Plan")
            print("4. Back to Main Menu\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_membership()
            elif choice == "2":
                self.view_memberships()
            elif choice == "3":
                self.delete_membership()
            elif choice == "4":
                break
            else:
                print("Invalid choice! Please try again.")

    def add_membership(self):
        plan = input("Enter Plan Name: ")
        duration = input("Enter Duration (e.g., 3 months): ")
        price = input("Enter Price: ")
        query = "INSERT INTO membership (PlanName, Duration, Price) VALUES (%s, %s, %s)"
        values = (plan, duration, price)
        self.cursor.execute(query, values)
        self.db.commit()
        print("Membership Plan Added!")

    def view_memberships(self):
        self.cursor.execute("SELECT * FROM membership")
        data = self.cursor.fetchall()
        print("\nMembership Plans:")
        print(tabulate(data, headers=["ID", "Plan Name", "Duration", "Price"], tablefmt="grid"))

    def delete_membership(self):
        name = input("Enter Plan Name to Delete: ")
        query = "DELETE FROM membership WHERE PlanName = %s"
        self.cursor.execute(query, (name,))
        self.db.commit()
        print("Membership Plan Deleted Successfully.")

    def payment_menu(self):
        while True:
            print("\nPAYMENTS & FINANCE\n")
            print("1. Add Payment")
            print("2. View Payment History")
            print("3. View Pending Payments")
            print("4. Back to Main Menu\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_payment()
            elif choice == "2":
                self.view_payments()
            elif choice == "3":
                self.pending_payments()
            elif choice == "4":
                break
            else:
                print("Invalid choice! Please try again.")

    def add_payment(self):
        print("Payment Feature Coming Soon...")

    def view_payments(self):
        print("Payment History Feature Coming Soon...")

    def pending_payments(self):
        print("Pending Payments Feature Coming Soon...")

if __name__ == "__main__":
    gym = GymManagement()
    gym.main_menu()
