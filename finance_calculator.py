import math

#Request user choose between investment & bond calculation
calc_type = input("Enter either 'investment' or 'bond' from the menu below to indicate your desired calculation:\n Investment\t- To calculate the total amount of money you'll earn from your investment.\n Bond\t\t- To calculate the amount you'll have to pay on a home loan.\n ")


#Store possible user options as variables to be used in conditional statements.
user_invest = "investment"
user_bond = "bond"

#Calculate return on investment if user chooses 'investment'.
if calc_type.lower() == user_invest :
    #Obtain required information from user.
    #Assign relevant user inputs to respective variables, including necessary conversions.
    inv_amount = float(input("Enter the amount you are depositing in Rands.\n"))
    user_interest = float(input("Enter the applicable interest rate, correct to the nearest 2 decimal places.\n Please do not enter the '%' sign. (e.g. Enter only 8, not 8%).\n"))
    inv_interest = float(user_interest / 100)
    inv_term = float(input("Over how many years would you like to invest?\n"))
    interest = input("Enter the applicable method of calculating interest.\n Choose by typing 'simple' or 'compound'.\n")
    if interest.lower() == "simple" :
        return_inv = round((inv_amount * (1 + inv_interest * inv_term)), 2)
        print()
        print("The return on your R{} investment, calculated over {} years at an annual simple interest rate of {}% will be R{}.\n".format(inv_amount, inv_term, inv_interest, return_inv))
    elif interest.lower() == "compound" :
        return_inv = round((inv_amount * math.pow(1 + inv_interest, inv_term)), 2)
        print()
        print("The return on your R{} investment, calculated over {} years at an annual compound interest rate of {}% will be R{}.\n".format(inv_amount, inv_term, inv_interest, return_inv))
    else :
        print("You have entered an incorrect answer.\n To proceed, please enter the word 'simple' or 'compound' to indicate your preferred method of calculating the interest on your Investment.")

#Calculate home loan repayment if user chooses 'bond'.
elif calc_type.lower() == user_bond :
    pres_houseval = float(input("Enter the current value of the house in Rands.\n"))
    HL_interest = float(input("Enter the annual interest rate to the nearest 2 decimal places.\n Please do not enter the '%' symbol. (e.g. 8% = 8).\n"))
    bond_interest = float((HL_interest /100) / 12)             #Divide interest rate by 12 because formula requires MONTHLY INTEREST.
    bond_term = float(input("Enter your repayment period in months.\n"))
    loan_repay = round(float((bond_interest * pres_houseval) / (1 - (bond_interest + 1) ** -bond_term)), 2)
    print()
    print("For a home worth R{} which is financed at {} percent interest annually, to be repaid over {} months:\n The monthly repayment amount will be R{}.".format(pres_houseval, HL_interest, bond_term, loan_repay))

else :
    print("You have entered an incorrect answer.\n Please enter the word 'investment' or 'bond' to proceed.")