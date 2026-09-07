#Concepts Used: Functions, arithmetic operations, input validation, conditional logic, loops
#Task:
#Create a Python program that converts temperature values between Celsius and Fahrenheit #using the following formulas:
#To convert Celsius to Fahrenheit:
#F = (C × 1.8) + 32
#To convert Fahrenheit to Celsius:
#C = (F − 32) × 0.5556
#Program Requirements:
#The program must allow the user to perform multiple conversions until they choose to stop.
#Ensure that the temperature entered by the user is numeric. If not, show an error message #and ask again.
#Create and use a function named:
#Temperature converter (mode, temperature)
#where mode indicates the type of conversion (C→F or F→C). 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to convert temperature
def temperature_converter(mode, temperature):
    if mode == "C":
        # Celsius to Fahrenheit
        return (temperature * 1.8) + 32
    elif mode == "F":
        # Fahrenheit to Celsius
        return (temperature - 32) * 0.5556
    else:
        return None

# Main program loop
while True:
    print("\n====== TEMPERATURE CONVERSION MENU ======")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '3':
        print("👋 Program terminated. Thank you!")
        break

    elif choice == '1' or choice == '2':
        while True:
            temp_input = input("Enter temperature value: ")

            try:
                temperature = float(temp_input)
                break
            except ValueError:
                print("❌ Invalid input! Please enter a numeric value.")

        if choice == '1':
            result = temperature_converter("C", temperature)
            print(f"🌡️ {temperature}°C = {result:.2f}°F")

        elif choice == '2':
            result = temperature_converter("F", temperature)
            print(f"🌡️ {temperature}°F = {result:.2f}°C")

    else:
        print("❌ Invalid choice! Please select between 1 and 3.")
