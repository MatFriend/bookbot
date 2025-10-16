from stats import get_book_text, total_chars, report
def main():
    bookText = get_book_text("books/frankenstein.txt")
    bookList = bookText.split()
    bookCount = len(bookList)
    print("Found " + str(bookCount) + " total words")
    dictionary = total_chars(bookText)
    print(dictionary)
    print(report(dictionary))

    
main()

