# Ash Bhuiyan                                       06-25-2025
# Lab 2 - Calculating compound amount over time.

# CITATION - URL: https://www.investopedia.com/terms/c/compoundinterest.asp
# CITATION - Author: Jason Fernando
# CITATION - Date Updated: 06-14-2024
# CITATION - Date Accessed: 06-24-2025

principal = int(input("Enter value 'principal amount': "))
rate = int(input("Enter value 'annual interest rate': "))
number_compounds = int(input("Enter value 'number compounds': "))
time = int(input("Enter value 'time': "))
accrued_amount = principal * (1 + (rate / 100) / number_compounds) ** (number_compounds * time)
print(f"After {time} years, you will have ${accrued_amount:.2f} in total.")
