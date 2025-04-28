#!/usr/bin/env python3
import sys

def reducer():
    current_word = None
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        word, count = line.split('\t', 1)
        count = int(count)

        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(f"{current_word}\t{current_count}")
            current_word = word
            current_count = count

    # Print the last word
    if current_word:
        print(f"{current_word}\t{current_count}")

if __name__ == "__main__":
    reducer()