from SavingAccount import SavingsAccount
from CurrentAccount import CurrentAccount

print("<<<<<<<<<<<<<<<<CURRENT ACCOUNT>>>>>>>>>>>>>>>>")    
current=CurrentAccount(1500)
current.display_balance()
current.deposit(500)
current.withdraw(200)
current.calculate_interest(0)

print("\n")
print("<<<<<<<<<<<<<<<<SAVINGS ACCOUNT>>>>>>>>>>>>>>>>")    
savings=SavingsAccount(2000)
savings.display_balance()
savings.deposit(1000)
savings.withdraw(500)
savings.calculate_interest(5)

