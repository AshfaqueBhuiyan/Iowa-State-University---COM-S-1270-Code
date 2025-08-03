# Ash Bhuiyan                          07-02-2025
# Lab 4 - Finding if a given year is a leap year.

def findLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    print()
    year = int(input("Enter a year: "))
    answer = findLeapYear(year)
    if answer:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
