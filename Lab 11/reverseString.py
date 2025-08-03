# Ash Bhuiyan                  08-02-2025
# Lab #11 - This program reverses a string using both an iterative approach and a recursive one.
# The recursive version avoids using loops or slicing.

def reverseIterative(s):
    reversedString = ""
    for i in range(len(s) - 1, -1, -1):
        reversedString += s[i]
    return reversedString

def reverseRecursive(s):

    if len(s) <= 1:
        return s

    return s[-1] + reverseRecursive(s[:-1])

def main():
    s = input("Enter a string to reverse: ")

    print("\n--- Iterative Reverse ---")
    reversedIter = reverseIterative(s)
    print("Result:", reversedIter)

    print("\n--- Recursive Reverse ---")
    reversedRecursive = reverseRecursive(s)
    print("Result:", reversedRecursive)

if __name__ == "__main__":
    main()
