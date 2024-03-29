#1. Create an online banking system with the following features:

#* Users must be able to log in with a username and password.
#* If the user enters the wrong credentials three times, the system must lock them out.
#* The initial balance in the bank account is $2000.
#* The system must allow users to deposit, withdraw, view, and transfer money.
#* The system must display a menu for users to perform transactions.
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Account():
    
    def __init__(self, username, password) -> None:
        self.username = username
        self.set_security_password(password)
        #self.hashed = False
        self.balance = 2000
        self.login_attempts = 0
        self.locked = False
                
    def set_security_password(self, password) -> None:
        self.password = pwd_context.hash(password)
        
    def verify_password(self, password) -> bool:
        if self.locked:
            print("Account is locked")
            return False
        
        if pwd_context.verify(password, self.password):
            self.login_attempts = 0
            return True
        
        else:
            self.login_attempts += 1
            if self.login_attempts >= 3:
                self.locked = True
                print("Failed 3 times or more, Account Locked")
                return False 
            
        return pwd_context.verify(password, self.password)
    
    #In this features, i have to managed balance or amount = 0
    def deposit(self,deposit) -> None:
        self.balance += deposit
        print("Your deposit was sucesfully")
    
    def withdraw(self,withdraw) -> None:
        self.balance -= withdraw
        print("Amount retired")
    
    def view(self) -> None:
        print(f"Your balance is ${self.balance}")
    
    def transfer(self, account, amount):
        self.balance -= amount
        account.balance += amount
        print("The Transfer was succesfully")


def main():
    accounts = {} # Store accounts (maybe a little db)
    
    current_account = None
    
    while True:
        print("\nWelcome to the Online Banking System")
        print("1. Login / Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Transfer Money")
        print("6. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            username = input("Username: " )
            password = input("Password: ")
            
            if username in accounts:
                if accounts[username].verify_password(password):
                    current_account = accounts[username]
                    print("Login Successful.")
            else:
                accounts[username] = Account(username, password)
                current_account = accounts[username]
                print("Account created and logged")
        elif choice == '2':
            if current_account:
                amount = float(input("Please enter amount to deposit: "))
                current_account.deposit(amount)
            else:
                print("Please be logged")
        elif choice == '3':
            if current_account:
                amount = float(input("Please enter amount to withdraw: "))
                current_account.withdraw(amount)
            else:
                print("Please be logged")
        elif choice == '4':
            if current_account:
                #amount = float(input("Please enter amount to withdraw: "))
                current_account.view()
            else:
                print("Please be logged")
        elif choice == '5':
            if current_account:
                amount = float(input("Please enter amount to transfer: "))
                second_account = input("Please enter the account to transfer: ")
                if second_account in accounts:
                    current_account.transfer(accounts[second_account], amount)
                else:
                    print("Not account Found")
            else:
                print("Please be logged")

        elif choice == '6':
            print("Exit")
            break

        else:
            print("Invalid option, try again.")
    
    #Testing if password is correctly hashed
    #print(accounts[username].username)
    #print(accounts[username].password)
            
if __name__ == "__main__":
    main()