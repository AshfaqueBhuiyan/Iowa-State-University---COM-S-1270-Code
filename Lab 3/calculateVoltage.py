# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of calculating voltage using Ohm's Law.

# CITATION - URL: https://www.electrical4u.com/ohms-law/
# CITATION - Author: Electrical4U
# CITATION - Date Updated: 04-30-2024
# CITATION - Date Accessed: 06-24-2025

def calculateVoltage(current, resistance):
    return current * resistance

def main():
    current = int(input("Enter value 'current': "))
    resistance = int(input("Enter value 'resistance': "))
    answer = calculateVoltage(current, resistance)
    print(f"Voltage = {answer} volts.")

if __name__ == "__main__":
    main()
