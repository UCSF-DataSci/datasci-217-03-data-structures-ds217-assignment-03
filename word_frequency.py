#!/usr/bin/env python3
"""
Word Frequency Counter

This script reads a text file and counts the frequency of each word, ignoring case.

Usage: python word_frequency.py <input_file>


Your task:
- Complete the word_frequency() function to count word frequencies sorted alphabetically
- Test your script on 'alice_in_wonderland.txt'

Hints:
- Use a dictionary to store word frequencies
- Consider using the lower() method to ignore case
- The split() method can be useful for splitting text into words
"""

import sys
import string

def word_frequency(text):
    # make dictionary
    frequencies = {}

    #open file and read into words
    text = open(sys.argv[1], 'r')
    words = text.read()
    text.close()
    #convert all words to lowercase and separate file contents into list of words
    words = words.lower()
    words = words.split()

    # repeat process until no words remain in text
    while len(words)>0:
        # take first word out of list and delete
        f = words.pop(0)
        f = f.strip(string.punctuation)
        # increase count if already in dictionary, otherwise add it in
        if f in frequencies: frequencies[f] = frequencies[f] + 1
        else: frequencies[f] = 1

    #alphebetize dictionary and print
    frequencies = dict(sorted(frequencies.items()))
    return frequencies

# Scaffold for opening a file and running word_frequency() on the contents
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_frequency.py <input_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            text = file.read() # Read the entire file into a string
        
        frequencies = word_frequency(text)
        
        # Print results
        for word, count in frequencies.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Word frequencies for '{filename}':")
    print(frequencies)