import sys

from stats import (
    chars_dict_to_sorted_list,
    get_book_char_count,
    get_book_text,
    get_book_word_count,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_book_word_count(text)
    characters = get_book_char_count(text)
    sorted_chars = chars_dict_to_sorted_list(characters)


    print_report(book_path, num_words, sorted_chars)


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for ch, count in sorted_chars:
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")

main()
