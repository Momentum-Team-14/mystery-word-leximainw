import re


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    freq = read_word_freq(file)
    for k, v in freq.items():
        if k not in STOP_WORDS:
            print(f"{k} = {v}")


def read_word_freq(path):
    file = open(path)
    freq = {}
    while line := file.readline():
        for word in line.split():
            if word:
                word = normalize_word(word)
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
