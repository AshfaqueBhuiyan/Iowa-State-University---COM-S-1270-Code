# Ash Bhuiyan                              07-19-2025
# Lab 8 - Removes non-ASCII characters from a file and saves a clean version.

def readFile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def removeNonASCII(text):
    clean = ""
    for char in text:
        if ord(char) < 128:
            clean += char
    return clean

def writeCleanFile(cleanedText, filename):
    new_filename = filename[:-4] + "_clean.txt"
    with open(new_filename, 'w') as file:
        file.write(cleanedText)

def main():
    filename = input("Enter the filename")
    contents = readFile(filename)
    cleaned = removeNonASCII(contents)
    writeCleanFile(cleaned, filename)

if __name__ == "__main__":
    main()
