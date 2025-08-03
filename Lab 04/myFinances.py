# Ash Bhuiyan               07-01-2025
# Lab 4 - myFinances module

def annualPercentageRate(interest_charges, fees, loan_amount, days_in_term):
    return (((interest_charges + fees) / loan_amount) / days_in_term) * 100

def compoundAmount(principal, rate, number_compounds, time):
    return principal * (1 + (rate / 100) / number_compounds) ** (number_compounds * time)
