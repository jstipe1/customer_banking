# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    new_balance = float(input("Please enter your initial savings account balance. "))
    interest_rate = float(input("Please enter your interest rate. "))
    months = int(input("Please enter the number of months to calculate interest. "))

    # Call the create_savings_account function and pass the variables from the user.
    #updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    create_savings_account(new_balance, interest_rate, months)

    interest_earned = new_balance * (interest_rate/100 * months/12)
    updated_savings_balance = new_balance+interest_earned

     # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Your savings account has earned $",interest_earned, " in interest", round(interest_earned, 2))    
    print("Your updated savings balance after earned interest is $", updated_savings_balance, round(updated_savings_balance, 2))
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    new_balance = float(input("Please enter your initial CD balance. "))
    interest_rate = float(input("Please enter your interest rate on your CD. "))
    months = int(input("Please enter the number of months to calculate interest. "))

    # Call the create_cd_account function and pass the variables from the user.
    #updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    create_cd_account(CD_balance, CD_interest_rate, CD_months)

    CD_interest_earned = CD_balance * (CD_interest_rate/100 * CD_months/12)
    updated_CD_balance = CD_balance+CD_interest_earned

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Your CD account has earned $",CD_interest_earned, " in interest", round(CD_interest_earned, 2)) 
    print("Your updated CD account balance after earned interest is $", updated_CD_balance, round(updated_CD_balance, 2))

if __name__ == "__main__":
    # Call the main function.
    main()