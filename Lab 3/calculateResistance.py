# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of calculating resistance using Ohm's Law.

# CITATION - URL: https://www.electrical4u.com/ohms-law/
# CITATION - Author: Electrical4U
# CITATION - Date Updated: 04-30-2024
# CITATION - Date Accessed: 06-24-2025

def calculateResistance(voltage, current):
    return voltage / current

def main():
    voltage = int(input("Enter value 'voltage': "))
    current = int(input("Enter value 'current': "))
    answer = calculateResistance(voltage, current)
    print(f"Resistance = {answer} ohms.")

if __name__ == "__main__":
    main()
