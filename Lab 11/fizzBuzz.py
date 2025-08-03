# Ash Bhuiyan                  08-01-2025
# Lab #11 - This program prints numbers from 1 to n, replacing multiples of 3 with "Fizz",
# multiples of 5 with "Buzz", multiples of 7 with "Bazz", and combinations accordingly.
# It includes both a modulus-based version and a dictionary-based version.

def fizzBuzzModulus(n):
    result = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
            output += "Bazz"
        if output == "":
            output = str(i)
        result.append(output)
    return result

def fizzBuzzDict(n):
    rules = {
        3: "Fizz",
        5: "Buzz",
        7: "Bazz"
    }
    result = []
    for i in range(1, n + 1):
        output = ""
        for key in rules:
            if i % key == 0:
                output += rules[key]
        if output == "":
            output = str(i)
        result.append(output)
    return result

def main():
    userInput = input("Enter a positive integer: ")
    if userInput.isdigit():
        n = int(userInput)
        if n < 1:
            print("Number must be positive.")
            return
    else:
        print("That's not a valid integer.")
        return

    print("\n--- FizzBuzz using Modulus ---")
    print(fizzBuzzModulus(n))

    print("\n--- FizzBuzz using Dictionary ---")
    print(fizzBuzzDict(n))

if __name__ == "__main__":
    main()
