#  Ryan Cutrone
#  CSCI 101-C
#  Create Project: Ryan's Reads

import new_book
import find_book


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


# Program Header
print("=============== Ryan's Reads ===============")
print("Please read the readme!")

# Main program controller
run = ""
while run != "quit":
    print('\nInput 1 to add a new book\nInput 2 to find a book\nInput 3 to obtain available information/edit an entered'
          ' book (must enter title exactly)\nInput "quit" to quit\n')

    run = input("Input: ").lower()

    if run == "1":   # Add a new book
        new_book.main()

    elif run == "2":   # Search for a book
        choice = input("Input 1 to search by author, 2 to search by title, or 3 to quit: ")

        if choice == "1":
            name = input("Author name: ")
            print(f"Books found: {find_book.get_book_author(name)}")

        elif choice == "2":
            name = input("Book name (or part of book name): ")
            print(f"Books found: {find_book.get_book_title(name)}")

    elif run == "3":   # display information on a book and choose to edit it

        title = input("Input title of book to display information on: ")
        book_info = find_book.book_info(title)

        book = Books(book_info[0], book_info[1], book_info[2], book_info[3], book_info[4], book_info[5])

        print(f"\nTitle: {book.title}")
        print(f"Author: {book.author}")
        print(f"Number in series: {book.number}")
        print(f"Number of pages: {book.total_pages}")
        print(f"Currently on page {book.current_page} ({100 * (int(book.current_page) / int(book.total_pages)):.2f}% progress)")
        print(f"Finished reading?: {book.completed}")

        choice = input("\nWould you like to any of this information? (Y/N): ").upper()
        if choice == "Y":
            edit_choice = input("What would you like to edit? [title (1), author (2), book number in series (3), total "
                                "number of pages (4), current page (5), completed status (6)]: ")

            edit_choices_dict = {   # provide index for choice to edit
                "1": 0,
                "2": 1,
                "3": 2,
                "4": 3,
                "5": 4,
                "6": 5
            }

            find_book.book_edit(book.title, edit_choice, edit_choices_dict[edit_choice])
