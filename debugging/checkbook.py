class Checkbook:
    """
    Checkbook - A simple class to represent a checkbook with basic deposit, withdrawal, and balance operations.
     @self.balance: Stores the current balance in the checkbook.
    """

    def __init__(self):
        """
        __init__ - Initializes a new checkbook instance with a starting balance of zero.
         @self: Reference to the current instance of Checkbook.
         Returns: None.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        deposit - Adds a specified amount to the current checkbook balance.
         @self: Reference to the current instance of Checkbook.
         @amount: The amount of money to be deposited.
         Returns: None. Prints the deposit amount and updated balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        withdraw - Deducts a specified amount from the checkbook balance if there are sufficient funds.
         @self: Reference to the current instance of Checkbook.
         @amount: The amount of money to be withdrawn.
         Returns: None. Prints a message if there are insufficient funds or upon successful withdrawal.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        get_balance - Prints the current balance of the checkbook.
         @self: Reference to the current instance of Checkbook.
         Returns: None. Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    main - Interacts with the user to perform various checkbook operations.
     @None.
     Returns: None. Continuously asks the user for an action until 'exit' is selected.
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                # Try to get a valid amount from the user
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                # Handle invalid input (non-numeric)
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            try:
                # Try to get a valid amount for withdrawal
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                # Handle invalid input (non-numeric)
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    """
    __main__ - Entry point of the script, runs the main function.
     @None.
     Returns: None.
    """
    main()
