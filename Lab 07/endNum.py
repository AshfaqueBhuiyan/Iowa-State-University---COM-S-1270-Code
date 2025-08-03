# Ash Bhuiyan                                    07-16-2025
# Lab #7 - This program moves all occurrences of a specified number to the end of a list.

def listInput():
    inputList = []
    while True:
        user_input = input("Enter an integer (* to stop): ")
        if user_input == "*":
            break
        inputList.append(int(user_input))
    return inputList

def endNum(lst, num):
    result = []
    count = 0
    for x in lst:
        if x == num:
            count += 1
        else:
            result.append(x)
    result.extend([num] * count)
    return result

def main():
    intList = listInput()
    num = int(input("Enter number to move to end: "))
    print("Modified list:", endNum(intList, num))

if __name__ == "__main__":
    main()
