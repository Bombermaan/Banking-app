import decimal
import json
class Account:
    def __init__(self, username, password, bal) -> None:
        self.username = username
        self.password = password
        self.balance = bal
    def addBalance(self,amount):
        self.balance += amount
        return f"Balance added to account. Amount added: {amount}, current balance: {self.balance}"
    def withdrawBalance(self,amount):
        self.balance -= amount
        return f"Withdrew {amount} from account. Your new balance is: {self.balance}"
    def addInterest(self):
        self.balance += self.balance*self.interest
        return f"Interest added! New account balance is: {self.balance}"
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
        with open('accountInfo.json', "w") as f:
            f.write(json_object)
        print("Done!")
    def __str__(self) -> str:
        return f"You have a {self.account_type} account. Your interest rate is therefore {decimal.Decimal(round(self.interest,2))*decimal.Decimal(round(100,2))}% and your balance is {self.balance}"
class childAccount(Account):
    def __init__(self, username, password, bal) -> None:
        super().__init__(username, password, bal)
        self.account_type = "child"
        self.interest = 0.03
class savingsAccount(Account):
    def __init__(self, username, password, bal) -> None:
        super().__init__(username, password, bal)
        self.account_type = "savings"
        self.interest = 0.04
class checkingAccount(Account):
    def __init__(self, username, password, bal) -> None:
        super().__init__(username, password, bal)
        self.account_type = "checking"
        self.interest = 0.02
class brokerageAccount(Account):
    def __init__(self, username, password, bal) -> None:
        super().__init__(username, password, bal)
        self.account_type = "brokerage"
        self.interest = 0.05