#Create a Python program to simulate a basic banking application.
#The program should:
#Start with a default account balance of ₹15,000
#Allow the user to perform: Deposit, Withdrawal, Balance Inquiry
#Run repeatedly until the user chooses to quit
#Use a global variable to store balance
#Validate withdrawal so balance never goes negative
#Required:
#A function for deposit
#A function for withdrawal
#A function to display balance
#A loop-based menu system
#Proper input validation and meaningful messages. 
#-------------------------------------------------------------------------------------------------------------------------------------------


# Global variable for account balance
balance = 15000

# Function to deposit money
def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("❌ Deposit amount must be greater than zero.")
        else:
            balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")

# Function to withdraw money
def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("❌ Insufficient balance! Withdrawal denied.")
        else:
            balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")

# Function to display balance
def display_balance():
    print(f"💰 Current Account Balance: ₹{balance}")

# Menu-driven program
while True:
    print("\n====== MINI BANKING MENU ======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Inquiry")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        deposit()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        display_balance()
    elif choice == '4':
        print("👋 Thank you for using the Mini Banking Program!")
        break
    else:
        print("❌ Invalid choice! Please select between 1 and 4.")
