def main():

    frankenstein_path = "books/frankenstein.txt"
    frankenstein_text = get_text(frankenstein_path)
    num_words = word_count(frankenstein_text)
    letter_counter = letter_count(frankenstein_text)

    print(frankenstein_text)
    print(f"Letter count: {letter_counter}")
    report(letter_counter, num_words, frankenstein_path)

def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def letter_count(text):
    counter = {}

    for letter in text:
        lowered = letter.lower()
        if lowered in counter:
            counter[lowered] += 1
        else:
            counter[lowered] = 1
    return counter

def report(letter_counter, num_words, path):
    letters = [{k: v} for k, v in letter_counter.items()]
    
    letters.sort(reverse=True, key=lambda d: list(d.values())[0])

    print(f"--- Begin report of {path} ---\n{num_words} words found in the document\n")

    for letter in letters:
        count = list(letter.items())[0]
        if count[0].isalpha():
            print(f"The '{count[0]}' character was found {count[1]} times")
    
    print("--- End report ---")

main()