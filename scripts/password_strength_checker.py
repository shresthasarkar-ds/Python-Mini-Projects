#Concepts: String operations, conditions, functions
#Problem:
#Write a program that checks password strength:
#Rules:
#•	Length ≥ 8
#•	Must include at least one uppercase, one lowercase, one number, one special character
#Function: check_password(password) returns:
#•	"Strong"
#•	"Medium"
#•	"Weak"
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to check password strength
def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/"

    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    # Determine strength
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif len(password) >= 6 and (has_upper or has_lower) and (has_digit or has_special):
        return "Medium"
    else:
        return "Weak"

# Main program
password = input("Enter your password: ")
strength = check_password(password)

print("Password Strength:", strength)
