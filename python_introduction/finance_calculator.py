# finance_calculator.py

def main():
    # Prompt the user for their monthly income
    monthly_income = float(input("Enter your monthly income: "))
    
    # Ask for their total monthly expenses
    monthly_expenses = float(input("Enter your total monthly expenses: "))
    
    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses
    
    # Project annual savings with 5% interest
    annual_savings_without_interest = monthly_savings * 12
    projected_annual_savings = annual_savings_without_interest * 1.05
    
    # Output the results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")

if __name__ == "__main__":
    main()
