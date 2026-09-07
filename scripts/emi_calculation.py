# Loan EMI Calculator

#Create a Python program that calculates the Equated Monthly Installment (EMI) for a loan.

#The program should ask the user to enter:

#- Loan amount
#- Loan tenure in years
#- Annual interest rate in percentage

#The program must:

#- Convert the annual interest rate into a monthly interest rate.
#- Convert the loan tenure from years into months.
#- Calculate the monthly EMI using the standard EMI formula.
#- Handle a 0% interest rate correctly.
#- Calculate the total amount payable and total interest payable.
#- Display all results clearly, formatted to two decimal places.

#Use variables, `input()`, type conversion, conditional statements, arithmetic operators, and formatted output.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Taking inputs
loan_amount = float(input("Enter loan amount (₹): "))
tenure_years = float(input("Enter loan tenure (years): "))
annual_interest_rate = float(input("Enter annual interest rate (%): "))

# Convert annual interest rate to monthly interest rate
monthly_interest_rate = annual_interest_rate / (12 * 100)

# Convert tenure from years to months
tenure_months = int(tenure_years * 12)

# Calculate EMI
if monthly_interest_rate == 0:
    emi = loan_amount / tenure_months
else:
    emi = (
        loan_amount
        * monthly_interest_rate
        * (1 + monthly_interest_rate) ** tenure_months
        / ((1 + monthly_interest_rate) ** tenure_months - 1)
    )

# Calculate total amount and total interest
total_payment = emi * tenure_months
total_interest = total_payment - loan_amount

# Display results
print("\n----- LOAN EMI CALCULATOR -----")
print(f"Loan Amount: ₹{loan_amount:,.2f}")
print(f"Tenure: {tenure_years:g} years ({tenure_months} months)")
print(f"Annual Interest Rate: {annual_interest_rate:.2f}%")
print(f"Monthly EMI: ₹{emi:,.2f}")
print(f"Total Interest Payable: ₹{total_interest:,.2f}")
print(f"Total Amount Payable: ₹{total_payment:,.2f}")

