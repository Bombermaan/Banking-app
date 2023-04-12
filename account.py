class Account:
    def __init__(self, username, password, acctype, bal) -> None:
        self.username = username
        self.password = password
        self.account_type = acctype
        self.balance = bal
        self.interest = 0
        if(self.account_type == "savings"):
            self.interest = 0.04
        elif(self.account_type == "checking"):
            self.interest = 0.02
        elif(self.account_type == "child"):
            self.interest = 0.03
        elif(self.account_type == "brokerage"):
            self.interest = 0.0045
    def addBalance(self,amt):
        self.balance += amt
        return f"Balance added to account. Amount added: {amt}, current balance: {self.balance}"
    def withdrawBalance(self,amt):
        self.balance -= amt
        return f"Withdrew {amt} from account. Your new balance is: {self.balance}"
    def addInterest(self):
        self.balance += self.balance*self.interest
        return f"Interest added! New account balance is: {self.balance}"
    def saveAccountState(self):
        print("Saving account information...")
        with open('accountInfo.txt', "w") as f:
            f.write('Username: ' + self.username + '\nPassword: ' + self.password + '\nAccount type: ' + self.account_type + '\nBalance: ' + str(self.balance) + '\nInterest rate: ' + str(self.interest))
        print("Done!")
    def __str__(self) -> str:
        return f"You have a {self.account_type} account. Your interest rate is therefore {self.interest*100}% and your balance is {self.balance}"