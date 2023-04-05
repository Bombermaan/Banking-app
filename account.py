class Account:
    def __init__(self, acctype, bal) -> None:
        self.account_type = acctype
        self.balance = bal
        self.interest = 0
        if(self.account_type == "savings"):
            self.interest = "4%"
        elif(self.account_type == "checking"):
            self.interest = "2%"
        elif(self.account_type == "child"):
            self.interest = "3%"
        elif(self.account_type == "brokerage"):
            self.interest = "0.45%"
    def addBalance(self,amt):
        self.balance += amt
        return f"Balance added to account. Amount added: {amt}, current balance: {self.balance}"
    def withdrawBalance(self,amt):
        self.balance -= amt
        return f"Withdrew {amt} from account. Your new balance is: {self.balance}"
    def __str__(self) -> str:
        return f"You have a {self.account_type} account. Your interest rate is therefore {self.interest} and your balance is {self.balance}"