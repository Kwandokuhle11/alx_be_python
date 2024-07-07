# Define global conversion factors using functions
def get_fahrenheit_to_celsius_factor():
    return 5 / 9

def get_celsius_to_fahrenheit_factor():
    return 9 / 5

# Conversion function: Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    fahrenheit_to_celsius_factor = get_fahrenheit_to_celsius_factor()
    celsius = (fahrenheit - 32) * fahrenheit_to_celsius_factor
    return celsius

# Conversion function: Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    celsius_to_fahrenheit_factor = get_celsius_to_fahrenheit_factor()
    fahrenheit = (celsius * celsius_to_fahrenheit_factor) + 32
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
