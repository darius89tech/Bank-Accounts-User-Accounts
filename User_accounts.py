# BankAccount class represents a bank account with basic functionalities.
class BankAccount:
    # Constructor to initialize interest rate and balance. Defaults are provided.
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    # Deposit method increases the balance by the specified amount.
    def deposit(self, amount):
        self.balance += amount
        return self

    # Withdraw method decreases the balance by the specified amount.
    # It checks for sufficient balance before withdrawal.
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    # This method displays the current balance of the account.
    def display_account_info(self):
        print(f"Balance: ${self.balance}")

    # If the account has a positive balance, interest is added based on the interest rate.
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


# The User class represents a bank client with one or more bank accounts.
class User:
    # Constructor initializes the user's name, email, and a default bank account.
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {'default': BankAccount(int_rate=0.02, balance=0)}

    # This method allows the user to deposit to a specified account.
    def make_deposit(self, amount, account_name='default'):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"No account found with name: {account_name}")
        return self

    # This method allows the user to withdraw from a specified account.
    def make_withdrawal(self, amount, account_name='default'):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"No account found with name: {account_name}")
        return self

    # Displays the balance for a specified account.
    def display_user_balance(self, account_name='default'):
        if account_name in self.accounts:
            print(f"{self.name}'s balance for {account_name} account: ${self.accounts[account_name].balance}")
        else:
            print(f"No account found with name: {account_name}")


    #SENSEI BONUS
    # Allows the user to add more accounts with specified names.
    def add_account(self, account_name, int_rate=0.02, balance=0):
        if account_name not in self.accounts:
            self.accounts[account_name] = BankAccount(int_rate, balance)
        else:
            print(f"Account with name {account_name} already exists.")
        return self

    #SENPAI BONUS
    # Enables transferring money between different users and their specific accounts.
    def transfer_money(self, amount, other_user, account_name_from='default', account_name_to='default'):
        if account_name_from in self.accounts:
            if self.accounts[account_name_from].balance >= amount:
                self.make_withdrawal(amount, account_name_from)
                other_user.make_deposit(amount, account_name_to)
            else:
                print(f"Insufficient funds in {self.name}'s {account_name_from} account.")
        else:
            print(f"No account found with name: {account_name_from}")
        return self


# The main function demonstrates the usage of the User and BankAccount classes.
def main():
    # Two users, Alan and Amber, are created.
    print("Creating two users: Alan and Amber")
    alan = User("Alan", "alan@email.com")
    amber = User("Amber", "amber@email.com")

    # Initial account balances are displayed.
    print("\nInitial balances:")
    alan.display_user_balance()
    amber.display_user_balance()

    # Deposits are made to both users' accounts.
    print("\nDepositing $500 into Alan's account and $300 into Amber's account")
    alan.make_deposit(500)
    amber.make_deposit(300)
    # Updated account balances are displayed.
    print("\nBalances after deposits:")
    alan.display_user_balance()
    amber.display_user_balance()

    # Withdrawals are made from both users' accounts.
    print("\nWithdrawing $200 from Alan's account and $100 from Amber's account")
    alan.make_withdrawal(200)
    amber.make_withdrawal(100)
    # Updated account balances are displayed.
    print("\nBalances after withdrawals:")
    alan.display_user_balance()
    amber.display_user_balance()

    # Alan adds multiple accounts.
    print("\nAdding multiple accounts for Alan: 'savings' and 'business'")
    alan.add_account("savings", 0.03, 1000)
    alan.add_account("business", 0.04, 2000)
    # Balances in Alan's new accounts are displayed.
    print("\nBalances in Alan's new accounts:")
    alan.display_user_balance("savings")
    alan.display_user_balance("business")

    # Transactions are made on Alan's specific accounts.
    print("\nDepositing $200 into Alan's 'savings' account and withdrawing $100 from his 'business' account")
    alan.make_deposit(200, "savings")
    alan.make_withdrawal(100, "business")
    # Updated balances are displayed.
    print("\nBalances after transactions on Alan's specific accounts:")
    alan.display_user_balance("savings")
    alan.display_user_balance("business")

    # Alan transfers money to Amber.
    print("\nAlan transfers $150 to Amber")
    alan.transfer_money(150, amber)
    # Updated balances are displayed.
    print("\nBalances after transfer:")
    alan.display_user_balance()
    amber.display_user_balance()

    # Alan transfers money from a specific account to Amber's default account.
    print("\nAlan transfers $100 from his 'savings' account to Amber's default account")
    alan.transfer_money(100, amber, "savings", "default")
    # Updated balances are displayed.
    print("\nBalances after transfer from specific accounts:")
    alan.display_user_balance("savings")
    amber.display_user_balance()

if __name__ == "__main__":
    main()
