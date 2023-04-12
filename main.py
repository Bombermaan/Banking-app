from account import *
import math


def main():
    
    print("Hello and welcome to the Very Cool Banking App™. Do you want to log in to an existing account or create a new one?")
    while True:
        user_login_choice = (int(input("Press 1 to login(in development), press 2 to create account: ")))
        if(user_login_choice == 1):
            #Add account migration from file here
            #Use a dictionary to match key to value (username to password) for verification.
            login_username = input("Enter your username: ")
            login_password = input("Enter password: ")
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
                print("The account types you can open are: 1. Savings, 2. Checking, 3. Child, 4. Brokerage")
                user_choice = int(input("Enter the type of account you want to open (1 for savings, 2 for checking etc.)."))
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
            print("Finally, create a nickname for your account:")
            while True:
                nickname = input("Input nickname: ")
                if(nickname != ""):
                    break
                else:
                    print("Error! Check nickname!")
            nickname = Account(user_name, password, user_account_type, balance)
            print(nickname)
            nickname.saveAccountState()
            break
        else:
            error = f"Invalid value! Please press only 1 or 2. your input was {user_login_choice}"
            print(error)
            continue

    

main()