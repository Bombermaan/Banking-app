#filename: account.py
#Authors: Mattila Teemu, Hahko Riina, Lehtovaara Maija
#Description: A simple banking app that has account creation and account management

from account import *
import math
import json
import time
from datetime import datetime

account = ""

def main():

    #This code checks if the current month has passed and a new one began, and if so, adds interest to account

    def checkInterest(current_month,month):
        
        while True:
            if current_month > month:
                print(account.addInterest())
                time.sleep(0.5)
                month += 1
                break
            else:
                continue    
      
    #A debug function to display how the interest works. 
    #This code forcibly advances one month and calls the checkInterest function to add interest to account
            
    def debugAddInterest():
        month = datetime.now().month
        current_month = month + 1
        checkInterest(current_month, month)
        return f"Interest added! Your new balance is {account.balance}!"
    
    def accountMenu():
    
    #Giving user options for their next action.
    #1 = deposit, 2 = withdraw, 3 = add interest, 4 = check account info and input empty = quit app.
    
            while True:
                print("Do you want to deposit or withdraw money or add interest(debug) or check account information?")
                try:
                    account_using_choice = int(input("Press 1 to deposit money, press 2 to withdraw money, press 3 to add interest, press 4 to check account information. Alternatively, leave the field empty to exit app: "))
                    if(account_using_choice == 1):
                        deposit_amount = int(input("Enter deposit amount: "))
                        account.addBalance(deposit_amount)
                        print(f"Done! Your new balance is: {account.balance}")
                        time.sleep(0.5)
                        account.saveAccountState()
                        break
                    
                    #Withdraw amount cannot cross the account balance. 
                    #If account balance is crossed, user is given the choice to choose action again.
    
                    elif(account_using_choice == 2):
                        withdraw_amount = int(input("Enter withdraw amount: "))
                        if withdraw_amount > account.balance:
                            print("Error! Account balance is crossed.")
                            time.sleep(0.5)
                            account.saveAccountState()
                            continue
                        account.withdrawBalance(withdraw_amount)
                        print (f"Current account balance is: {account.balance}")
                        print(0.5)
                        account.saveAccountState()
                        break
                    elif(account_using_choice == 3):
                        debugAddInterest()
                        account.accountStatement()
                    elif(account_using_choice == 4):
                        print (f"Your account balance is {account.balance} and your interest rate is {account.interest}")
                        time.sleep(0.5)
                        account.accountStatement()
                        accountMenu()
                    else: 
                        print("Error! Choose a number between 1 to 4.")
                        time.sleep(1)
                    continue
                except ValueError:
                    try:
                        print("Empty input detected. Do you want to exit app? Y/N")
                        exit_choice = input()
                        if exit_choice == "Y" or exit_choice == "y":
                            print("Exiting the Very Cool Banking App™. See you next time!")
                            time.sleep(2)
                            return 0
                        elif exit_choice == "N" or exit_choice == "n":
                            print("You have decided to continue operations in the app. Welcome back!")
                            time.sleep(1)
                            continue
                        else:
                            print("Input error! Check your input!")
                            time.sleep(0.5)
                            continue
                    except ValueError:
                        print("Empty input!")
                    
               
    print("Hello and welcome to the Very Cool Banking App™. Do you want to log in to an existing account or create a new one?")

    #If users chose 1, login into a account;opens a json file with the account information.
    #Checks if the username or/and password are correct, if incorrect gives an Error for the user.

    while True:
        user_login_choice = (int(input("Press 1 to login, press 2 to create account: ")))
        if(user_login_choice == 1):
            login_username = input("Enter your username: ")
            login_password = input("Enter password: ")
            try:
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
                    time.sleep(1)
                    account.saveAccountState()
                    accountMenu()
                else:
                    print("Error")
                    continue

            except FileNotFoundError:
                print("Error! Account not found!")
                continue
            break
        
        #If user chose 2, create account; create a username and password, confirm password.
        #If passwords do not match, Error and try again.

        elif(user_login_choice == 2):
            print("Create your account here!")
            while True:
                user_name = input("Enter your username: ")
                password = input("Enter password: ")
                password_confirm = input("Confirm password: ")
                if(password == password_confirm):
                    break
                else:
                    print("Error! Passwords did not match, try again!")
                    continue
                    
            #Choose account type, gives 4 choices to choose from.
            #Creates account depending on user choice; Error if not input value is not 1 to 4.
            #If Error user is made to choose again; if chosen correctly informs the user what account they created.

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

            #Asking the amount user is wanting to deposit to the account when created. 
            #Deposit needs to be 100 or higher, if not Error and asks user to adjust amount.

            default_balance = 100
            print("How much money will you put into this account? The minimum is 100.")
            time.sleep(0.4)
            print("If you leave the space empty, it will assume the 100 and put that into the account.")
            time.sleep(0.4)
            try:
                balance = int(input("Please input the amount you will put into the account: "))
                if balance < 100:
                    print("Added balance too low, adjusting amount to 100")
                    time.sleep(0.3)
                    balance = 100
            except ValueError:
                print("Input empty, assuming default value of 100.")
                time.sleep(0.3)
                balance = default_balance

            #Asking the user if they want the account to be created or aborted.
            #If user chose 1, create account.
            #if user chose 2, abort creating the account.
            #If input is invalid, Error and choice is given again.

            print("Do you want to create the account with the following information?")
            time.sleep(0.2)
            print ("Username: " + user_name + "\nPassword: " + password + "\nBalance: " + str(balance))
            while True:
                create_choice = int(input("Press 1 to create, press 2 to abort creation "))
                if create_choice == 1:
                    class_caller_name = (str(user_account_type)+"Account")
                    myclass = globals()[class_caller_name]
                    account = myclass(user_name,password,balance)
                    print(account)
                    account.saveAccountState()
                    accountMenu()
                else:
                    print("Aborting account creation, returning to main menu:")
                    time.sleep(2)
                    main()
            break
        else:
            error = f"Invalid value! Please press only 1 or 2. your input was {user_login_choice}"
            print(error)
            time.sleep(0.4)
            continue


    

    
main()


    