
class ATM:
    """
    Represents a simple ATM account with basic banking operations.
    """

    def __init__(self) -> None:
        """Initialize the ATM with a zero balance."""
        self.balance: float = 0.0

    def check_balance(self) -> float:
        """
        Return the current account balance.

        Returns:
            float: Current balance
        """
        return self.balance

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.

        Args:
            amount (float): Amount to deposit

        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Withdraw money from the account.

        Args:
            amount (float): Amount to withdraw

        Raises:
            ValueError: If amount is not positive or exceeds balance
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount


class ATMController:
    """
    Controls user interaction and delegates operations to the ATM.
    """

    def __init__(self) -> None:
        """Initialize the ATM controller."""
        self.atm = ATM()

    def get_number(self, prompt: str) -> float:
        """
        Prompt the user for a numeric input.

        Args:
            prompt (str): Input prompt

        Returns:
            float: Valid numeric input
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")

    def display_menu(self) -> None:
        """Display the ATM menu."""
        print("\nWelcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self) -> None:
        """Display the current balance."""
        print(f"Your current balance is: ${self.atm.check_balance()}")

    def deposit(self) -> None:
        """Handle deposit operation."""
        while True:
            try:
                amount = self.get_number("Enter the amount to deposit: ")
                self.atm.deposit(amount)
                print(f"Successfully deposited ${amount}.")
                break
            except ValueError as error:
                print(error)

    def withdraw(self) -> None:
        """Handle withdrawal operation."""
        amount = self.get_number("Enter the amount to withdraw: ")

        try:
            self.atm.withdraw(amount)
            print(f"Successfully withdrew ${amount}.")
        except ValueError as error:
            print(error)

    def run(self) -> None:
        """Run the ATM application loop."""
        while True:
            self.display_menu()
            choice = input("Please choose an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please try again.")


def main() -> None:
    """Application entry point."""
    ATMController().run()


if __name__ == "__main__":
    main()
