# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion function: Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Conversion function: Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp} Celsius is {converted_temp:.2f} Fahrenheit.")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp} Fahrenheit is {converted_temp:.2f} Celsius.")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
