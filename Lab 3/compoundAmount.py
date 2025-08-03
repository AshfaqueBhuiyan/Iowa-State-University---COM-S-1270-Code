# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of calculating compound amount over time.

# CITATION - URL: https://www.investopedia.com/terms/c/compoundinterest.asp
# CITATION - Author: Jason Fernando
# CITATION - Date Updated: 06-14-2024
# CITATION - Date Accessed: 06-24-2025

def compoundAmount(principal, rate, number_compounds, time):
    return principal * (1 + (rate / 100) / number_compounds) ** (number_compounds * time)

def main():
    principal = int(input("Enter value 'principal amount': "))
    rate = int(input("Enter value 'annual interest rate': "))
    number_compounds = int(input("Enter value 'number compounds': "))
    time = int(input("Enter value 'time': "))
    answer = compoundAmount(principal, rate, number_compounds, time)
    print(f"After {time} years, you will have ${answer:.2f} in total.")

if __name__ == "__main__":
    main()
