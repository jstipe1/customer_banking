"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    balance = float(balance)
    interest_rate = float(interest_rate)
    months = int(months)
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
savings = Account(15000, 0)

new_balance = float(input("Please enter your initial savings account balance. "))
interest_rate = float(input("Please enter your interest rate. "))
months = int(input("Please enter the number of months to calculate interest. "))

# Pass the updated account information from the user to the setter method you created above.
savings.set_balance(new_balance)

       # Calculate interest earned
     # ADD YOUR CODE HERE
interest_earned = new_balance * (interest_rate/100 * months/12)
print("You have earned $",interest_earned, " in interest", round(interest_earned, 2))                   
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

updated_balance = new_balance+interest_earned
print("Your updated balance after earned interest is $", updated_balance, round(updated_balance, 2))
    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE 

class SavingsAccount:
    """Creating an SavingsAccount class with methods"""
    def __init__(self, savings_balance, savings_interest):
        self.savings_balance = savings_balance
        self.savings_interest = savings_interest

        SavingsAccount.savings_balance = updated_balance
        SavingsAccount.savings_interest = interest_earned

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE

    def get_savings_balance(self):
         return self.savings_balance

    def get_savings_interest(self):
        return self.savings_interest
