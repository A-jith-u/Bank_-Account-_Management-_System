from BankAccount import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self,balance):
        super().__init__(balance)
    def calculate_interest(self,interest_rate):
        try:
            if interest_rate<0:
                raise ValueError("Interest rate cannot be negative")
            interest= self.balance*(interest_rate/100)
            self.balance+=interest
            print(f"Interest of {interest_rate}% has been added to your account. Your new balance is {self.balance}")
        except ValueError:
            print("Invalid interest rate. Please enter a valid interest rate.")

