import time

class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited {amount}")
            print(f"✅ {amount} deposited successfully!")
        else:
            print("❌ Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")
            print(f"✅ {amount} withdrawn successfully!")
        else:
            print("❌ Insufficient balance or invalid amount.")

    def transfer(self, target_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.history.append(f"Transferred {amount} to {target_account.account_number}")
            target_account.history.append(f"Received {amount} from {self.account_number}")
            print(f"✅ {amount} transferred to {target_account.name}!")
        else:
            print("❌ Transfer failed. Check balance or amount.")

    def show_balance(self):
        print(f"💰 Balance for {self.name} (Acc {self.account_number}): {self.balance}")

    def show_history(self):
        print(f"\n📜 Transaction History for {self.name}:")
        if not self.history:
            print("No transactions yet.")
        else:
            for entry in self.history:
                print(f"- {entry}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_deposit=0):
        if account_number in self.accounts:
            print("❌ Account number already exists.")
        else:
            self.accounts[account_number] = Account(account_number, name, initial_deposit)
            print(f"✅ Account created for {name} with number {account_number}.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

def main():
    bank = Bank()
    print("🏦 Welcome to Python Bank System 🏦")

    while True:
        print("\nChoose an option:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Show Balance")
        print("6. Show History")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            acc_num = input("Enter new account number: ")
            name = input("Enter account holder name: ")
            deposit = float(input("Enter initial deposit: "))
            bank.create_account(acc_num, name, deposit)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("❌ Account not found.")

        elif choice == "3":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("❌ Account not found.")

        elif choice == "4":
            acc_num = input("Enter your account number: ")
            target_num = input("Enter target account number: ")
            account = bank.get_account(acc_num)
            target_account = bank.get_account(target_num)
            if account and target_account:
                amount = float(input("Enter transfer amount: "))
                account.transfer(target_account, amount)
            else:
                print("❌ One or both accounts not found.")

        elif choice == "5":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                account.show_balance()
            else:
                print("❌ Account not found.")

        elif choice == "6":
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                account.show_history()
            else:
                print("❌ Account not found.")

        elif choice == "7":
            print("👋 Thank you for using Python Bank. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

        time.sleep(1)

if __name__ == "__main__":
    main()
