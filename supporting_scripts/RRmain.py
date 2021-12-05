#  Ryan Cutrone
#  CSCI 101-C
#  Create Project: Ryan's Reads

from supporting_scripts import new_book
from supporting_scripts import find_book


# Class to get parts of books after taking them out of CSV
class Books:

    def __init__(self, title, author, number, total_pages, current_page, completed):
        self.title = title
        self.author = author
        self.number = number
        self.total_pages = total_pages
        self.current_page = current_page
        self.completed = completed

    @classmethod
    def new_books(cls, book_info):
        title, author, book_number, total_pages, current_page, completed = book_info.split(",")
        return cls(title, author, book_number, total_pages, current_page, completed)

"""I am so sorry for the atrocious function titles, commented are what they should be. I don't have the will to change them everywhere they need to change"""
# Main program controller
def one():  # ADD NEW BOOK
    print("=======================================================\n")
    new_book.main()
    print("\n=======================================================\n")

def two_one(): # LIST BY AUTHOR
    print("=======================================================\n")
    name = input("Author name: ")
    print(f"Books found: {find_book.get_book_author(name)}")
    print("=======================================================\n")

def two_two(): # LIST BY UNFINISHED
    print("=======================================================\n")
    print(f"Unfinished books found: {find_book.get_uncompleted_books()}")
    print("\n=======================================================\n")

def two_three():  # LIST BY FINISHED
    print("=======================================================\n")
    print(f"Finished books found: {find_book.get_completed_books()}")
    print("\n=======================================================\n")


def three():  # display information on a book and choose to edit it
    title = input("Input title of book to display information on: ")
    book_info = find_book.book_info(title)

    try:
        book = Books(book_info[0], book_info[1], book_info[2], book_info[3], book_info[4], book_info[5])

        print(f"\nTitle: {book.title}")
        print(f"Author: {book.author}")
        print(f"Number in series: {book.number}")
        print(f"Number of pages: {book.total_pages}")
        print(f"Currently on page {book.current_page} ({100 * (int(book.current_page) / int(book.total_pages)):.2f}% progress)")
        print(f"Finished reading?: {book.completed}")

        choice = input("\nWould you like to edit any of this information? (Y/N): ").upper()
        if choice == "Y":
            edit_choice = input("What would you like to edit? [title (1), author (2), book number in series (3), total "
                                "number of pages (4), current page (5), completed status (6), delete book (7)]: ")
            """You can't choose which book you want to edit if they share a name, might fix that if I can"""
            edit_choices_dict = {   # provide index for choice to edit
                "1": 0,
                "2": 1,
                "3": 2,
                "4": 3,
                "5": 4,
                "6": 5,
                "7": 6,
            }

            find_book.book_edit(book.title, edit_choice, edit_choices_dict[edit_choice])
    except Exception:   # TODO consider making this error more specific -> nah
        print("ERROR An error occurred")

    print("\n=======================================================\n")
    

# TODO Use timestamps from time to determine rate at which user is reading, and return an estimate of how many hours they have left until they finish.
# - SQL structured query language, could use SQLite. 
# - ORM works in conjunction with a data layer (.csv, sql, sqlite) -> basically simplifies code