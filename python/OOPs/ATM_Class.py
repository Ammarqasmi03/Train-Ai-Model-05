class Atm:

    # Constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0.0
        self.menu()

    def menu(self):
        user_input = input("""
            Welcome to the ATM!
            press 1 to check balance
            press 2 to deposit
            press 3 to withdraw
            press 4 to create pin
            press 5 to change pin
            press anything else to exit
        """)

        if user_input == '1':
          # Check balance
          self.check_balance()
        elif user_input == '2':
          # Deposit
          self.deposit()
        elif user_input == '3':
          # Withdraw
          self.withdraw()
        elif user_input == '4':
          # Create pin
          self.create_pin()
        elif user_input == '5':
          # Change pin
          self.change_pin()
        else:
          print("Thank you for using the ATM. Goodbye!") 
          exit()


    def check_balance(self):
        user_pin = input("Enter your PIN to check balance:")
        if user_pin == self.pin:
            print("Your BALANCE is : ", self.balance)
        else:
            print("Incorrect PIN. Please try again.")
        self.menu()

    def create_pin(self):
        new_pin = input("Enter a new 4-digit PIN:")
        self.pin = new_pin
        print("PIN created successfully!")
        self.menu()

    def change_pin(self):
        current_pin = input("Enter your current PIN:")
        if current_pin == self.pin:
            new_pin = input("Enter a new 4-digit PIN:")
            self.pin = new_pin
            print("PIN changed successfully!")
            
        else:
            print("Incorrect PIN. Please try again.")
        self.menu()

    def deposit(self):
        amount = float(input("Enter the amount to deposit:"))
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")
        self.menu()

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw:"))
        if amount > self.balance:
            print("Insufficient funds. Please try again.")
        elif amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        self.menu()


obj1 = Atm()
obj1.menu()