def count_letters(book):
    lower_book = book.lower()
    characters = {}
    for char in lower_book:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    for char in characters:
        print(f"The '{char}' character was found {characters[char]} times.")
    


def get_book_text(path) -> str:
    with open(path) as f:
        return f.read()

def count(book) -> int:
    words = book.split()
    return len(words)

def main() -> int: 
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count(file_contents)
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {word_count} words in the book")
    print("The letter count for the book is:")
    count_letters(file_contents)
    print("--- End Report ---")
    return 0

main()