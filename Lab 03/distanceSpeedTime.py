# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of calculating distance from speed and time.

# CITATION - URL: https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php
# CITATION - Author: CalculatorSoup
# CITATION - Date Updated: 08-21-2023
# CITATION - Date Accessed: 06-24-2025

def distanceSpeedTime(speed, time):
    return speed * time

def main():
    speed = int(input("Enter value 'speed': "))
    time = int(input("Enter value 'time': "))
    answer = distanceSpeedTime(speed, time)
    print(f"Distance traveled = {answer} meters.")

if __name__ == "__main__":
    main()
