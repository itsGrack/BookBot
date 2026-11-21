def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_book_word_count(file_contents):
    words = file_contents.split()
    word_count = len(words)

    return word_count

def get_book_char_count(file_contents):
    chars = {}

    words = file_contents.lower()

    for char in words:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(chars: tuple[str, int]) -> int:
    return chars[1]

def chars_dict_to_sorted_list(chars: dict[str, int]) -> list[tuple[str,int]]:
    new_list = []

    for char in chars:
        count = chars[char]
        new_list.append((char, count))

    sorted_list = sorted(new_list, reverse=True, key=sort_on)

    return sorted_list
