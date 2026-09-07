#Write a Python program to create a Budget Calculator. The program should:
#1.	Ask the user to enter their name.
#2.	Ask for their income.
#3.	Ask for the number of days for which the budget needs to be calculated.
#4.	Take the user's rent, travel, and food expenses as input.
#5.	Calculate the total expenses and remaining balance for each day.
#6.	Calculate the user's total savings over the given number of days.
#7.	Use conditional statements to display different messages based on the balance:
#o	If the balance is ≤ -5000, display a financial-crisis message.
#o	If the balance is ≤ -2000, display a deficit message.
#o	If the balance is 0, display a balanced-budget message.
#o	If the balance is > 2000, display a savings message.
#o	If the balance is > 5000, display a rich/surplus message.
#o	Otherwise, display a default message.
#8.	Finally, display the total amount saved after the calculation period.
#Concepts Used:
#input(), variables, float(), int(), arithmetic operators, for loop, if-elif-else conditions, and formatted output.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

username = input("Enter your name👧🏽: ")

print("***Welcome", username, "to the Budget Calculator***")

income = float(input("Enter your income💰: "))
days = int(input("Enter the number of days to calculate for📅: "))

# expenses
rent = float(input("Enter your rent🏠: "))
travel = float(input("Enter your travel🛺: "))
food = float(input("Enter your food😋: "))

savings = 0

for days in range(1, days+1):
    
    #formula
    total_expenses = rent + travel + food
    balance = income - total_expenses
    
    savings = savings + balance  

    #conditionals
    if balance > 5000:
        print('Rich kid spotted!!')

    elif balance > 2000:
        print('well done you saved, balance')

    elif balance == 0:
        print('Broked but balanced, ur the one called as balancing buddha')

    elif balance <= -2000:
        print('Deficit!, surviving on maggi!!!')

    elif balance <= -5000:
        print('Your so broke, ur wallet is in financial coma, even rbi cant help up!!!')

    else:
        print('.........')

print('....yo dude, u saved', savings , '......')                            
