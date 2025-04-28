#!/usr/bin/env python3
import sys

def mapper():
    for line in sys.stdin:
        line = line.strip()  # Remove extra whitespace
        words = line.split() # Split into words
        for word in words:
            print(f"{word.lower()}\t1")  # Emit each word with count=1

if __name__ == "__main__":
    mapper()