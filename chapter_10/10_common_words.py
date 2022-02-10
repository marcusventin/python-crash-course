def word_counter(word, filename):
    try:
        with open(filename) as f:
            words = f.read().lower()
    except FileNotFoundError:
        print(f"{filename} could not be found.")
    else:
        word_count = words.count(f" {word.lower()} ")
        print(f"The word '{word}' appeared {word_count} times in this file.")

word_counter('the', 'chapter_10/pg67363.txt')