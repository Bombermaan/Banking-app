#filename: account.py
#Authors: Mattila Teemu, Hahko Riina, Lehtovaara Maija
#Description: File that contains all classes and their methods related to accounts

import decimal
import json
import time

class Account:

    #Initializes the object's attributes with the values passed as arguments.
    def __init__(self, username, password, bal) -> None:
        self.username = username
        self.password = password
        self.balance = bal

    #Takes an argument amount and adds it to the balance attribute of the account.
    #Returns a message that informs the user of the amount added and the current balance.
    def addBalance(self,amount):
        self.balance += amount
        return f"Balance added to account. Amount added: {amount}, current balance: {self.balance}"
    
    #Takes an argument amount and subtracts it from the balance attribute of the account.
    #Returns a message that informs the user of the amount withdrawn and the new balance.
    def withdrawBalance(self,amount):
        self.balance -= amount
        return f"Withdrew {amount} from account. Your new balance is: {self.balance}"
    
    #Calculates the interest on the account balance and adds it to the balance attribute of the account.
    #Returns a message that informs the user of the new balance.
    def addInterest(self):
        self.balance += self.balance*self.interest
        return f"Interest added! New account balance is: {self.balance}"
    
    #Returns a message that provides the current account balance and the interest rate.
    def accountStatement(self):
        return f"Your account balance is {self.balance} and your interest rate is {self.interest}"
    
    #Creates a dictionary with the account information and converts it to JSON format.
    #Saves the JSON object to a file named accountInfo.json.
    def saveAccountState(self):
        dictionary = {
            "Username:": self.username,
            "Password:": self.password,
            "Account type:": self.account_type,
            "Balance:": self.balance,
            "Interest rate:": self.interest
        }
        json_object = json.dumps(dictionary, indent=4)
        print("Saving account information...")
        time.sleep(1) 
        with open('accountInfo.json', "w") as f:
            f.write(json_object)
        print("Done!")
    
    #Returns a message that provides the account type, interest rate, and balance.
    def __str__(self) -> str:
        return f"You have a {self.account_type} account. Your interest rate is therefore {decimal.Decimal(round(self.interest,2))*decimal.Decimal(round(100,2))}% and your balance is {self.balance}"

#Calls the __init__ method of the parent class using super(), passes the arguments username, password, and bal.
#Sets the account_type attribute to "child" and the interest attribute to 0.03.
class childAccount(Account):
    def __init__(self, username, password, bal) -> None:
        super().__init__(username, password, bal)
        self.account_type = "child"
        self.interest = 0.03

#Calls the __init__ method of the parent class using super() and passes the arguments username, password, and bal.
#Sets the account_type attribute to "savings" and the interest attribute to 0.04.
class savingsAccount(Account):
    def __init__(self, username, password, bal) -> None:
        super().__init__(username, password, bal)
        self.account_type = "savings"
        self.interest = 0.04

#Calls the __init__ method of the parent class using super() and passes the arguments username, password, and bal.
#Sets the account_type attribute to "checking" and the interest attribute to 0.02.
class checkingAccount(Account):
    def __init__(self, username, password, bal) -> None:
        super().__init__(username, password, bal)
        self.account_type = "checking"
        self.interest = 0.02

#Calls the __init__ method of the parent class using super() and passes the arguments username, password, and bal.
#Sets the account_type attribute to "brokerage" and the interest attribute to 0.05.
class brokerageAccount(Account):
    def __init__(self, username, password, bal) -> None:
        super().__init__(username, password, bal)
        self.account_type = "brokerage"
        self.interest = 0.05