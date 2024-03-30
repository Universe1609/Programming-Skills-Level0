#2. Create a currency converter between CLP, ARS, USD, EUR, TRY, GBP with the following features:
#The user must choose their initial currency and the currency they want to exchange to.
#The user can choose whether or not to withdraw their funds. If they choose not to withdraw, it should return to the main menu.
#If the user decides to withdraw the funds, the system will charge a 1% commission.
#The system should ask the user if they want to perform another operation. If they choose to do so, it should restart the process; otherwise, the system should close.
#Set a minimum and maximum amount for each currency, it can be of your choice.

def main():
    while True:
        print("\nWelcome to the currency converter, Please choice between these currency")
        print("1. CLP")
        print("2. ARS")
        print("3. USD")
        print("4. EUR")
        print("5. TRY")
        print("6. GBP")
        initial_currency = input("Select initial currency: ")
        exchange_currency = input("Select currency you want to exchange to: ")
        amount = input("What is the amount you want to exchange: ")
  
            #this part is for change feature
        
        print("\nWhat do you want to do next?")
        print("1. Withdraw")
        print("2. Go to main menu")
        
            #feature for withdraw
            
        print("Do you want to make another operation? (Y/n): ")
        
            #Conditional

if __name__ == "__main__":
    main()