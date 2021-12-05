"""
This script is used any time Books.csv needs to be accessed to read or edit existing data
"""

import csv

# get a list of all books
def get_all_books():
    found_books = []
    
    try:
        with open(r"Books.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            
            next(reader)  # header
            for row in reader:
                found_books.append(row[0])

        if found_books == []:
            print("No books found")
        else:
            print("Books found:",", ".join(found_books))
    
    except FileNotFoundError:
        print("ERROR You have not entered any books")
    
    
# Find book by its title
def get_uncompleted_books():
    found_books = []

    try:
        with open("Books.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)

            next(reader)
            for row in reader:
                if row[5] !="Y" and row[4] < row[3]:   # if marked finished or read pages == total pages
                    found_books.append(row[0])

        if found_books == []:
            return "No books found"
        else:
            print(", ".join(found_books))
            return ", ".join(found_books)

    except FileNotFoundError:
        return "ERROR You have not entered any books"


def get_completed_books():
    found_books = []

    try:
        with open("Books.csv", "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)

            next(reader)
            for row in reader:
                if row[5] == "Y" or row[4] == row[3]:   # if marked finished or read pages == total pages
                    found_books.append(row[0])

        if found_books == []:
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
        with open("Books.csv", "r", encoding="utf-8") as csvfile:
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
        print("ERROR You have not entered any books")
        return "ERROR You have not entered any books"

# get a book and return it to RyanReads.py
def book_info(book_title):
    try:
        with open("Books.csv", "r", encoding="utf-8") as csvfile:
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
    temp_file = []

    if edit_choice != "7":
        new_text = input(f"New input for {edit_choice}: ")
        with open("Books.csv", "r") as f_in:
            reader = csv.reader(f_in)

            for row in reader:
                if row[0] == book:
                    row[edit_index] = new_text
                temp_file.append(row)

        with open("Books.csv", "w", newline="", encoding="utf-8") as f_out:
            writer = csv.writer(f_out)
            writer.writerows(temp_file)
    else:
        deleted = False
        with open("Books.csv", "r", encoding="utf-8") as f_in:
            reader = csv.reader(f_in)
            for row in reader:
                if row[0] == book and deleted != True:
                    deleted = True
                else:
                    temp_file.append(row)
            
        with open("Books.csv", "w", newline="", encoding="utf-8") as f_out:
            writer = csv.writer(f_out)
            for row in temp_file:
                writer.writerow(row)