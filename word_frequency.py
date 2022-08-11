from collections import defaultdict
import math
import re


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

MAX_STARS = 20
MAX_WORD_LEN = 20


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    # find the word frequencies and filter out the common words
    freq = [x for x in read_word_freq(file).items() if x[0] not in STOP_WORDS]
    
    # sort the words by their frequency
    freq = sorted(freq,
        key=lambda tuple: tuple[1],
        reverse=True)
    
    # find the longest word's length
    max_len = min(max(len(x[0]) for x in freq), MAX_WORD_LEN)
    
    # find the highest frequency
    max_freq = freq[0][1]
    
    # find the highest frequency's length
    max_digits = len(str(max_freq))
    
    # print the words
    for k, v in freq:
        num_stars = v
        if max_freq > MAX_STARS:
            num_stars = math.ceil(num_stars / (max_freq / MAX_STARS))
        if len(k) > MAX_WORD_LEN:
            k = k[slice(MAX_WORD_LEN - 3)] + "..."
        print(f"{k.rjust(max_len)} = {str(v).rjust(max_digits)} {''.rjust(num_stars, '*')}")


def read_word_freq(path):
    """Read in `file` and tally the frequency of words in that file."""
    
    freq = defaultdict(int)
    
    # open the target file
    file = open(path)
    
    # read lines until the end of the file
    # Python's .readline() returns '' only at EOF.
    # If there's another line, readline() will return a string that ends with '\n'.
    while line := file.readline():
        
        # split the current line into individual words
        for word in line.split():
            
            # normalize the word so that words containing punctuation
            # are grouped to a single entry
            word = normalize_word(word)
            
            # if the word is non-empty, increment the frequency dict
            if word: freq[word] += 1
    
    file.close()
    return freq


def normalize_word(word):
    """Normalize a word to lowercase, with no punctuation."""
    
    return re.sub('[^a-z]', '', word.lower())


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(2)   # ENOENT error code - no such file or directory
