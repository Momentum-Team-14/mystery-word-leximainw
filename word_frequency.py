import math
import re


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

MAX_STARS = 20


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    # find the word frequencies and filter out the common words
    freq = filter(lambda tuple: tuple[0] not in STOP_WORDS,
        read_word_freq(file).items())

    # sort the words by their frequency
    freq = sorted(freq,
        key=lambda tuple: tuple[1],
        reverse=True)

    # find the longest word's length
    max_len = max(map(lambda tuple: len(tuple[0]), freq))

    # find the highest frequency
    max_freq = freq[0][1]

    # find the highest frequency's length
    max_digits = len(str(max_freq))

    # print the words
    for k, v in freq:
        num_stars = v
        if max_freq > MAX_STARS:
            num_stars = math.ceil(num_stars / (max_freq / MAX_STARS))
        print(f"{k.rjust(max_len)} = {str(v).rjust(max_digits)} {''.rjust(num_stars, '*')}")


def read_word_freq(path):
    file = open(path)
    freq = {}
    while line := file.readline():
        for word in line.split():
            word = normalize_word(word)
            if word:
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
    return freq


def normalize_word(word):
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
