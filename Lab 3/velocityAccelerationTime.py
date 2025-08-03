# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of calculating final velocity.

# CITATION - URL: https://www.omnicalculator.com/physics/velocity
# CITATION - Author: Mateusz Mucha and Dominik Czernia
# CITATION - Date Updated: 03-07-2025
# CITATION - Date Accessed: 06-24-2025

def velocityAccelerationTime(initial_velocity, acceleration, time):
    return initial_velocity + (acceleration * time)

def main():
    initial_velocity = int(input("Enter value 'initial velocity': "))
    acceleration = int(input("Enter value 'acceleration': "))
    time = int(input("Enter value 'time': "))
    answer = velocityAccelerationTime(initial_velocity, acceleration, time)
    print(f"Final velocity = {answer} m/s.")

if __name__ == "__main__":
    main()
