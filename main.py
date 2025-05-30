book_path = "books/frankenstein.txt"

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def main():
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    print(f"{num_words} words found in the document")

main()