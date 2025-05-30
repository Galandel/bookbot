from stats import (get_num_words, 
                   get_char_count,
                   sort_char_counts)

book_path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = get_char_count(book_text)
    sorted_char_counts = sort_char_counts(char_counts)

    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {book_path}...")
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('--------- Character Count -------')
    for char_dict in sorted_char_counts:
        print(f"{char_dict['char']}: {char_dict['num']}")

main()