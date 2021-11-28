"""
This script is used any time Books.csv needs to be accessed to read or edit existing data
"""

import csv


# Find book by its title
def get_book_title(book_name):
    found_books = []

    try:
        with open("Books.csv", "r") as csvfile:
            reader = csv.reader(csvfile)

            next(reader)
            for row in reader:
                if book_name in row[0]:
                    found_books.append(row[0])
        
        if found_books == False:
            return "No books found"
        else:
            return ", ".join(found_books)

    except FileNotFoundError:
        return "ERROR You have not entered any books"


# find book by its author
def get_book_author(author_name):
    found_books = []
    author_name = author_name.title()

    try:
        with open("Books.csv", "r") as csvfile:
            reader = csv.reader(csvfile)

            next(reader)
            for row in reader:
                if author_name in row[1]:
                    found_books.append(row[0])

        if found_books == False:
            return "No books found"
        else:
            return ", ".join(found_books)

    except FileNotFoundError:
        return "ERROR You have not entered any books"

# get a book and return it to RyanReads.py
def book_info(book_title):
    try:
        with open("Books.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            book_title = book_title.title()

            next(reader)
            for row in reader:
                if book_title in row[0]:
                    return row

    except FileNotFoundError:
        print("ERROR You have not entered any books")

# edit information on a book in Books.csv
def book_edit(book, edit_choice, edit_index):
    new_text = input(f"New input for {edit_choice}: ")
    temp_file = []

    with open("Books.csv", "r") as f_in:
        reader = csv.reader(f_in)

        for row in reader:
            if row[0] == book:
                row[edit_index] = new_text
            temp_file.append(row)

    with open("Books.csv", "w", newline="") as f_out:
        writer = csv.writer(f_out)
        writer.writerows(temp_file)