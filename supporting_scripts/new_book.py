"""
This script is used to create Books.csv (if it does not already exist) and enter a new book into it.
"""


from os.path import exists  # check to see if file exists
import csv


def main():
    # Add a new book, Title, Author, Number, Pages, Completed
    book_title = input("Book Title: ").title()      # Book Title
    book_author = input("Book Author: ").title()    # Book Author

    is_int = False
    while not is_int:   # Book number
        try:
            book_number = int(input('Book Number (if book is not a part of a series, enter "1"): '))
        except ValueError:
            print("Please enter an integer")
        else:
            is_int = True

    is_int = False
    while not is_int:   # Pages
        try:
            total_pages = int(input('Number of pages: '))
        except ValueError:
            print("Please enter an integer")
        else:
            is_int = True

    is_int = False
    while not is_int:  # Pages
        try:
            current_page = int(input('What page are you on?: '))
        except ValueError:
            print("Please enter an integer")
        else:
            is_int = True

    book_status = input("Have you finished this book? (Y/N): ").upper()

    # Write to csv
    if exists("Books.csv"):
        with open("Books.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([book_title, book_author, book_number, total_pages, current_page, book_status])
    else:
        with open("Books.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Author", "Book Number", "Total Pages", "Current Page", "Completed"])
            writer.writerow([book_title, book_author, book_number, total_pages, current_page, book_status])


if __name__ == "__main__":
    main()
