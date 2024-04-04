"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
def create_cd_account(CD_balance, CD_interest_rate, CD_months):
    CD_balance = float(CD_balance)
    CD_interest_rate = float(CD_interest_rate)
    CD_months = int(CD_months)

    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
cd_account = Account(15000, 0)

CD_balance = float(input("Please enter your initial CD balance. "))
CD_interest_rate = float(input("Please enter your interest rate on your CD. "))
CD_months = int(input("Please enter the number of months to calculate interest. "))

cd_account.set_balance(CD_balance)
    # Calculate interest earned
    # ADD YOUR CODE HERE
CD_interest_earned = CD_balance * (CD_interest_rate/100 * CD_months/12)
print("You have earned $",CD_interest_earned, " in interest", round(CD_interest_earned, 2)) 

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE

updated_CD_balance = CD_balance+CD_interest_earned
print("Your updated balance after earned interest is $", updated_CD_balance, round(updated_CD_balance, 2))

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
 
class CDAccount:
    """Creating an CDAccount class with methods"""
    def __init__(self, CD_balance, CD_interest):
        self.CD_balance = CD_balance
        self.CD_interest = CD_interest

        CDAccount.CD_balance = updated_CD_balance
        CDAccount.CD_interest = CD_interest_earned

    # Return the updated balance and interest earned.
# ADD YOUR CODE HERE

    def get_CD_balance(self):
         return self.CD_balance

    def get_CD_interest(self):
        return self.CD_interest