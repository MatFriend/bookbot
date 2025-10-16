def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def total_chars(book_text):
    book_text = book_text.lower()
    char_count = {}
    for char in book_text:
        char_count[char] = char_count.get(char, 0) + 1
    return(char_count)

def report(dictionary):
    dictionary.sort(reverse=true, key=sort_on)

