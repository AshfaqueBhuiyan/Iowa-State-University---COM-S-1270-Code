# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of calculating current using Ohm's Law.

# CITATION - URL: https://www.electrical4u.com/ohms-law/
# CITATION - Author: Electrical4U
# CITATION - Date Updated: 04-30-2024
# CITATION - Date Accessed: 06-24-2025

def calculateCurrent(voltage, resistance):
    return voltage / resistance

def main():
    voltage = int(input("Enter value 'voltage': "))
    resistance = int(input("Enter value 'resistance': "))
    answer = calculateCurrent(voltage, resistance)
    print(f"The current flowing = {answer:.3f} amps.")

if __name__ == "__main__":
    main()