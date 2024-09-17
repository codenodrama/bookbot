def words_counter(text):
    words = text.split()
    return len(words)

def print_content(file_contents):
    print(file_contents)

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return sorted(chars.items(), key=lambda x:x[1], reverse=True)

def print_report(word_count, chars, filepath):
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document\n")
    for character in chars:
        print(f"The {character[0]} character was found {character[1]} times")
    print("--- End report ---\n")


def main():
    filepath = "books/frankenstein.txt"
    with open(filepath) as f:
        file_contents = f.read()
    word_count = words_counter(file_contents)
    chars = get_chars_dict(file_contents)
    print_report(word_count, chars, filepath)
    

main()