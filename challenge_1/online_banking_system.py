#1. Create an online banking system with the following features:

#* Users must be able to log in with a username and password.
#* If the user enters the wrong credentials three times, the system must lock them out.
#* The initial balance in the bank account is $2000.
#* The system must allow users to deposit, withdraw, view, and transfer money.
#* The system must display a menu for users to perform transactions.
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class log_in():
    
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.hashed = False
        self.balance = 2000
        self.login_attempts = 0
        
    def set_security_password(self, password) -> None:
        self.password = pwd_context.hash(password)
        
    def verify_password(self, password) -> bool:
        if pwd_context.verify(password, self.password):
            self.login_attempts = 0
            return True
        else:
            self.login_attempts += 1
            if self.login_attempts >= 3:
                return False #after this, i have to locked it, creating self.locked 
            
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
    