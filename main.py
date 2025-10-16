import sys
from stats import get_book_text, total_chars
from report import gen_report
def main():
    book_path =""
    try:
        book_path=sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookText = get_book_text(book_path)
    bookList = bookText.split()
    bookCount = str(len(bookList))
    print("Found " + bookCount + " total words")
    dictionary = total_chars(bookText)
    print(dictionary)
    sorted_list = (gen_report(dictionary))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {bookCount} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()

