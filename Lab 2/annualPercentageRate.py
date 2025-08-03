# Ash Bhuiyan                                       06-25-2025
# Lab 2 - Finding APR from charges, fees, loan amount & term days.

# CITATION - URL: https://www.investopedia.com/terms/a/apr.asp
# CITATION - Author: Jason Fernando
# CITATION - Date Updated: 06-03-2024
# CITATION - Date Accessed: 06-24-2025

interest_charges = int(input("Enter value 'interest charges': "))
fees = int(input("Enter value 'fees': "))
loan_amount = int(input("Enter value 'loan amount': "))
days_in_term = int(input("Enter value 'days in term': "))
apr = (((interest_charges + fees) / loan_amount) / days_in_term) * 100
print(f"The APR = {apr:.2f}% annually.")
