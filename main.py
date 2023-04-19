from account import *
import math
import json
import time
from datetime import datetime




def main():

    def checkInterest(current_month,month):
        
        while True:
            if current_month > month:
                print(account.addInterest())
                month += 1
                break
            else:
                continue    
            
    def debugAddInterest():
        month = datetime.now().month
        current_month = month + 1
        checkInterest(current_month, month)
        return f"Interest added! Your new balance is {account.balance}!"
    
    print("Hello and welcome to the Very Cool Banking App™. Do you want to log in to an existing account or create a new one?")
    while True:
        user_login_choice = (int(input("Press 1 to login(in development), press 2 to create account: ")))
        if(user_login_choice == 1):
            #Add account migration from file here
            #Use a dictionary to match key to value (username to password) for verification.
            login_username = input("Enter your username: ")
            login_password = input("Enter password: ")
            with open('accountInfo.json') as f:
                data = json.load(f)

            username = data['Username:']
            password = data['Password:']
            account_type = data['Account type:']
            balance = data['Balance:']
            if login_username == username and login_password == password:
                print("Success")
                class_caller_name = (str(account_type)+"Account")
                myclass = globals()[class_caller_name]
                account = myclass(username,password,balance)
                print(account)
                account.saveAccountState()
            else:
                print("Error")
                continue
            break
        elif(user_login_choice == 2):
            #Add account creation here
            print("Create your account here!")
            while True:
                user_name = input("Enter your username: ")
                password = input("Enter password: ")
                password_confirm = input("Confirm password: ")
                if(password == password_confirm):
                    break
                else:
                    print("Error! passwords did not match, try again!")
                    continue
            while True:
                print("The account types you can open are: 1. Savings, 2. Checking, 3. Child, 4. Brokerage ")
                user_choice = int(input("Enter the type of account you want to open (1 for savings, 2 for checking etc.). "))
                user_account_type = ""
                if(user_choice == 1):
                    user_account_type = "savings"
                    break
                elif(user_choice == 2):
                    user_account_type = "checking"
                    break
                elif(user_choice == 3):
                    user_account_type = "child"
                    break
                elif(user_choice == 4):
                    user_account_type = "brokerage"
                    break
                else:
                    error = f"Error! Check input value! Please type a number from 1 to 4. Your value was {user_choice}."
                    continue
            print(f"You have chosen a {user_account_type} account.")
            default_balance = 100
            print("How much money will you put into this account? The minimum is 100.")
            print("If you leave the space empty, it will assume the 100 and put that into the account.")
            try:
                balance = int(input("Please input the amount you will put into the account: "))
                if balance < 100:
                    print("Added balance too low, adjusting amount to 100")
                    balance = 100
            except ValueError:
                print("Input empty, assuming default value of 100.")
                balance = default_balance
            print("Do you want to create the account with the following information?")
            print ("Username:" + user_name + "\nPassword:" + password + "\nBalance:" + str(balance))
            while True:
                create_choice = int(input("Press 1 to create, press 2 to abort creation "))
                if create_choice == 1:
                    class_caller_name = (str(user_account_type)+"Account")
                    myclass = globals()[class_caller_name]
                    account = myclass(user_name,password,balance)
                    print(account)
                    account.saveAccountState()
                    break
                else:
                    print("Aborting account creation, returning to main menu:")
                    time.sleep(2)
                    main()
            break
        else:
            error = f"Invalid value! Please press only 1 or 2. your input was {user_login_choice}"
            print(error)
            continue
    
    while True:
        print("Do you want to deposit or withdraw money or add interest(debug)?")
        try: 
            account_using_choice = int(input("Press 1 to deposit money, press 2 to withdraw money, press 3 to add interest: "))
        
            if(account_using_choice == 1):
                deposit_amount = int(input("Enter deposit amount: "))
                account.addBalance(deposit_amount)
                print(account.balance)
                account.saveAccountState()
                break
            elif(account_using_choice == 2):
                withdraw_amount = int(input("Enter withdraw amount: "))
                if withdraw_amount > account.balance:
                    print("Error! Account balance is crossed.")
                    account.saveAccountState()
                    continue
                account.withdrawBalance(withdraw_amount)
                print (f"Current account balance is: {account.balance}")
                account.saveAccountState()
                break
            elif(account_using_choice == 3):
                 debugAddInterest()
                 account.saveAccountState()
            else: 
                print("Error! Choose 1 or 2")
            continue
        except ValueError:
            print("Input empty!")
            continue

    #Näytä korko kuukausittain joka balanceen on lisääntyy.
    
main()


    