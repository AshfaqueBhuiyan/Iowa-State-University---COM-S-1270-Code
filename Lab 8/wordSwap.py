# Ash Bhuiyan                              07-19-2025
# Lab 8 - Randomly swaps words in a sentence.

import random

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    unique_words = list(set(words))
    
    mapping = {}
    for word in unique_words:
        mapping[word] = random.choice(words)

    print("Swap Dictionary:", mapping)

    new_sentence = ' '.join([mapping[word] for word in words])
    print("New Sentence:", new_sentence)

if __name__ == "__main__":
    main()
