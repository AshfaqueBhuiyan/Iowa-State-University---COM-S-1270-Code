# Ash Bhuiyan                                                   07-01-2025
# Lab 4 - The main program for calculating shapes, physics, Ohm's law, and finance modules.

import myShapes
import myPhysics
import myOhmsLaw
import myFinances

def main():
    running = True
    while running:
        print("\nChoose a function to run:")
        print("[AOR] Area of Rectangle")
        print("[POR] Perimeter of Rectangle")
        print("[AOC] Area of Circle")
        print("[COC] Circumference of Circle")
        print("[DIST] Distance")
        print("[FV] Final Velocity")
        print("[CV] Calculate Voltage")
        print("[CR] Calculate Resistance")
        print("[CC] Calculate Current")
        print("[APR] Annual Percentage Rate (APR)")
        print("[CA] Compound Amount")
        print("[Q]uit")

        choice = input("Enter your choice: ")

        if choice == "AOR":
            base = int(input("Enter base: "))
            height = int(input("Enter height: "))
            print("Area =", myShapes.areaOfRectangle(base, height))

        elif choice == "POR":
            length = int(input("Enter length: "))
            width = int(input("Enter width: "))
            print("Perimeter =", myShapes.rectanglePerimeter(length, width))

        elif choice == "AOC":
            radius = int(input("Enter value 'radius': "))
            print("Area =", myShapes.areaOfCircle(radius))

        elif choice == "COC":
            radius = int(input("Enter value 'radius': "))
            print("Circumference =", myShapes.circleCircumference(radius))

        elif choice == "DIST":
            speed = int(input("Enter speed: "))
            time = int(input("Enter time: "))
            print("Distance =", myPhysics.distanceSpeedTime(speed, time))

        elif choice == "FV":
            initial_velocity = int(input("Initial velocity: "))
            acceleration = int(input("Acceleration: "))
            time = int(input("Time: "))
            print("Final velocity =", myPhysics.velocityAccelerationTime(initial_velocity, acceleration, time))

        elif choice == "CV":
            current = int(input("Enter current: "))
            resistance = int(input("Enter resistance: "))
            print("Voltage =", myOhmsLaw.calculateVoltage(current, resistance))

        elif choice == "CR":
            voltage = int(input("Enter voltage: "))
            current = int(input("Enter current: "))
            print("Resistance =", myOhmsLaw.calculateResistance(voltage, current))

        elif choice == "CC":
            voltage = int(input("Enter voltage: "))
            resistance = int(input("Enter resistance: "))
            print("Current =", myOhmsLaw.calculateCurrent(voltage, resistance))

        elif choice == "APR":
            interest = int(input("Interest charges: "))
            fees = int(input("Fees: "))
            loan = int(input("Loan amount: "))
            days = int(input("Days in term: "))
            print("APR =", myFinances.annualPercentageRate(interest, fees, loan, days))

        elif choice == "CA":
            p = int(input("Principal: "))
            r = int(input("Annual rate %: "))
            n = int(input("Times compounded per year: "))
            t = int(input("Time in years: "))
            print("Compound amount =", myFinances.compoundAmount(p, r, n, t))

        elif choice == "Q":
            print("Goodbye!")
            running = False
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
