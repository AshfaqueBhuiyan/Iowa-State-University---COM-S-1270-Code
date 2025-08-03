# Ash Bhuiyan                              07-19-2025
# Lab 8 - Analyzes a book text and outputs word frequencies.

def analyzeBook(filename):
    f = open(filename, 'r')
    count = {}

    for line in f:
        for word in line.split():

            # remove punctuation
            word = word.replace('_', '').replace('"', '').replace('.', '').replace(',', '')
            word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
            word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
            word = word.replace(']', '').replace(';', '')

            # ignore case
            word = word.lower()

            # ignore numbers
            if word.isalpha():
                if word in count:
                    count[word] = count[word] + 1
                else:
                    count[word] = 1

    return count

def outputAnalysis(count, filename):
    base = filename[:-4]
    output_filename = base + "_analysis.txt"
    with open(output_filename, 'w') as out:
        for word in sorted(count.keys()):
            out.write(f"{word} {count[word]}\n")

def main():
    filename = input("Enter the filename")
    counts = analyzeBook(filename)
    outputAnalysis(counts, filename)

if __name__ == "__main__":
    main()