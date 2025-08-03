# Ash Bhuiyan                                       06-25-2025
# Lab 2 - Calculating final velocity.

# CITATION - URL: https://www.omnicalculator.com/physics/velocity
# CITATION - Author: Mateusz Mucha and Dominik Czernia
# CITATION - Date Updated: 03-07-2025
# CITATION - Date Accessed: 06-24-2025

initial_velocity = int(input("Enter value 'initial velocity': "))
acceleration = int(input("Enter value 'acceleration': "))
time = int(input("Enter value 'time': "))
final_velocity = initial_velocity + (acceleration * time)
print(f"Final velocity = {final_velocity} m/s.")
