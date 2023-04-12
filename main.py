from account import *


def main():
    
    print("Hello and welcome to the Very Cool Banking App™. Do you want to log in to an existing account or create a new one?")
    while True:
        userLoginChoice = (int(input("Press 1 to login(in development), press 2 to create account: ")))
        if(userLoginChoice == 1):
            #Add account migration from file here
            #Use a dictionary to match key to value (username to password) for verification.
            login_username = input("Enter your username: ")
            login_password = input("Enter password: ")
            break
        elif(userLoginChoice == 2):
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
            break
        else:
            error = f"Invalid value! Please press only 1 or 2. your input was {userLoginChoice}"
            print(error)
            continue

    

main()