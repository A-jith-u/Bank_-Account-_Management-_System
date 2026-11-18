from abc import ABC, abstractmethod
#from curses.ascii import isalpha

class BankAccount(ABC):                      #Create an abstract class BankAccount with an abstract method calculate_interest and a property balance. The class should also have methods to display the balance, deposit money, and withdraw money. The balance property should have a setter that raises a ValueError if the balance is set to a negative or zero value.
    def __init__(self,balance,):
        self.__balance=balance               #create a private attribute __balance to store the balance of the account

    @abstractmethod                          #create an abstract method calculate_interest that will be implemented by the subclasses
    def calculate_interest(self):
        pass

    @property                                #create a property balance that will return the balance of the account so as to access the private attribute __balance
    def balance(self):
        return self.__balance
    
    @balance.setter                          #create a setter for the balance property that will raise a ValueError if the balance is set to a negative or zero value
    def balance(self,value):
        if value<=0:
            raise ValueError("Balance cannot be negative or zero")
        self.__balance=value


    def display_balance(self):               #create a method display_balance that will print the balance of the account
        print("The account balance is:",self.__balance)


    def deposit(self,deposit_amount):        #create a method deposit that will add the deposit_amount to the balance of the account. The method should raise a ValueError if the deposit_amount is negative or zero.
        try:
         if deposit_amount<=0 :
            raise "Deposit amount cannot be negative, zero or a string"
         self.__balance+=deposit_amount
         print(f"Your deposit of {deposit_amount} has been successful. Your new balance is {self.__balance}")
        except TypeError:
            print("Re-enter a valid deposit amount")


    def withdraw(self,withdraw_amount):      #create a method withdraw that will subtract the withdraw_amount from the balance of the account. The method should raise a if the withdraw_amount is greater than the balance.
        try:
         if withdraw_amount>self.balance:
            raise "Insufficient balance"
         self.__balance-=withdraw_amount
         print(f"Withdrawal of {withdraw_amount} has been succesful. Your new balance is {self.__balance} ")
        except TypeError:
           print("Re-enter a valid withdraw amount")

        

          