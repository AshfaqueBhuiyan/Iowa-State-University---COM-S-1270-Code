# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of finding APR

# CITATION - URL: https://www.investopedia.com/terms/a/apr.asp
# CITATION - Author: Jason Fernando
# CITATION - Date Updated: 06-03-2024
# CITATION - Date Accessed: 06-24-2025

def annualPercentageRate(interest_charges, fees, loan_amount, days_in_term):
    return (((interest_charges + fees) / loan_amount) / days_in_term) * 100

def main():
    interest_charges = int(input("Enter value 'interest charges': "))
    fees = int(input("Enter value 'fees': "))
    loan_amount = int(input("Enter value 'loan amount': "))
    days_in_term = int(input("Enter value 'days in term': "))
    answer = annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)
    print(f"The APR = {answer:.2f}% annually.")

if __name__ == "__main__":
    main()
