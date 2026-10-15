"""
Temperature Conversion Program
Purpose: Demonstrate Celsius and Fahrenheit temperature conversions.
"""

def temperature_conversion():
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit"""
        return celsius * 9/5 + 32

    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5/9

    while True:
        print("\n====== Temperature Conversion ======")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Bidirectional Conversion")
        print("0. Exit")

        choice = input("Select an option (0-3): ")

        if choice == "1":
            print("\n[Option 1] Celsius to Fahrenheit:")
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is {fahrenheit:.2f}°F")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "2":
            print("\n[Option 2] Fahrenheit to Celsius:")
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is {celsius:.2f}°C")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "3":
            print("\n[Option 3] Bidirectional Conversion:")
            try:
                temp = float(input("Enter temperature: "))
                unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").strip().upper()
                if unit == "C":
                    print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
                elif unit == "F":
                    print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
                else:
                    print("Unit must be 'C' or 'F'!")
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    temperature_conversion()