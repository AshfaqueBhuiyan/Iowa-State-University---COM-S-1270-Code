# Ash Bhuiyan                                     07-16-2025
# Lab #7 - This program rotates a list left or right based on user input.

def listInput():
    inputList = []
    while True:
        user_input = input("Enter an integer (* to stop): ")
        if user_input == "*":
            break
        inputList.append(int(user_input))
    return inputList

def rotateList(lst, rot):
    n = len(lst)
    rot = rot % n
    return lst[-rot:] + lst[:-rot] if rot else lst

def main():
    intList = listInput()
    rot = int(input("Enter number of rotations (positive=right, negative=left): "))
    rot = rot % len(intList)
    if rot < 0:
        rot = len(intList) + rot
    print("Rotated list:", rotateList(intList, rot))

if __name__ == "__main__":
    main()
