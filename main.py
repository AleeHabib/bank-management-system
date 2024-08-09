import time


class PinCodeLengthError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ChoiceOutOfRangeError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class Account:
    def __init__(self, acc_no: int, owner: str, pin: int, balance=0.0):
        self.acc_no = acc_no
        self.owner = owner
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nTRANSACTION STATUS: {amount} deposited to {self.owner}'s account.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(
                f"TRANSACTION STATUS: {amount} withdrawn from {self.owner}'s account."
            )
        else:
            print("\nWARNING: Insufficient balance!")

    def show_balance(self):
        print(f"Rupees {self.balance}")

    def get_pin(self):
        return int(self.pin)


accounts = {}


def menu():

    print("\n-----------| BANKING SYSTEM |----------\n")

    print("1. Create a new account.")
    print("2. Deposit.")
    print("3. Withdraw.")
    print("4. Show Balance.")
    print("5. Exit.")

    print("\n-----------| BANKING SYSTEM |----------\n")

    while True:
        try:
            choice = int(input("What do you want to do?: "))
            if not 0 < choice <= 5:
                raise ChoiceOutOfRangeError("Choice must be between 1 and 5, try again")
            break
        except ValueError:
            print("Choice must be an integer, try again")
        except ChoiceOutOfRangeError as e:
            print(e)

    if choice == 1:

        print("\n< CREATING A NEW ACCOUNT >")
        acc_no = int(input("\nEnter account number: "))
        owner = input("Enter your name: ")

        while True:
            try:
                pin_list = []
                pin = input("Enter a pin code: ")
                for num in pin:
                    pin_list.append(num)
                if len(pin_list) != 4:
                    raise PinCodeLengthError(
                        "\n< ERROR: Pin code must be of 4 digits >\n"
                    )
                break
            except PinCodeLengthError as e:
                print(e)

        if acc_no not in accounts:
            accounts[acc_no] = Account(acc_no, owner, pin)
            print("\n< STATUS: Account successfully created >")

            menu_option = input("\nPress 'M' to go back: ")
            if menu_option.upper() == "M":
                menu()
        else:
            print("\n< WARNING: Account already exists >")

            menu_option = input("\nPress 'M' to go back: ")
            if menu_option.upper() == "M":
                menu()

    elif choice == 2:

        print("\n< DEPOSITING CASH >")
        acc_no = int(input("\nEnter account number: "))

        if acc_no not in accounts:
            print("\n< WARNING: Account does not exist >")

            menu_option = input("\nPress 'M' to go back: ")
            if menu_option.upper() == "M":
                menu()
        else:

            amount = float(input("Enter the amount you want to deposit: "))

            if amount <= 0:
                print("\n< WARNING: Invalid amount! >")

                menu_option = input("\nPress 'M' to go back: ")
                if menu_option.upper() == "M":
                    menu()

            else:
                acc = accounts[acc_no]
                acc.deposit(amount)

                menu_option = input("\nPress 'M' to go back: ")
                if menu_option.upper() == "M":
                    menu()

    elif choice == 3:

        print("\n< WITHDRAWING CASH >")
        acc_no = int(input("\nEnter account number: "))

        if acc_no not in accounts:
            print("\n< WARNING: Account does not exist >")

            menu_option = input("\nPress 'M' to go back: ")
            if menu_option.upper() == "M":
                menu()
        else:

            pin = int(input("Enter pin code: "))
            acc = accounts[acc_no]
            if pin == acc.get_pin():
                amount = float(input("Enter the amount you want to withdraw: "))

                acc.withdraw(amount)

                menu_option = input("\nPress 'M' to go back: ")
                if menu_option.upper() == "M":
                    menu()
            else:
                print("\n< WARNING: Pin code does not match! >")

                menu_option = input("\nPress 'M' to go back: ")
                if menu_option.upper() == "M":
                    menu()

    elif choice == 4:

        print("\n< BALANCE CHECKER >")
        acc_no = int(input("\nEnter account number: "))

        if acc_no not in accounts:
            print("\n< WARNING: Account does not exist >")

            menu_option = input("\nPress 'M' to go back: ")
            if menu_option.upper() == "M":
                menu()
        else:
            acc = accounts[acc_no]
            print("")
            acc.show_balance()

            menu_option = input("\nPress 'M' to go back: ")
            if menu_option.upper() == "M":
                menu()

    else:
        print("Exiting..")
        time.sleep(1)


if __name__ == "__main__":
    menu()
