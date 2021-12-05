import tkinter as tk
import tkinter.font as tkFont
import RRmain
from supporting_scripts import find_book
from supporting_scripts import new_book


# ADD_BOOK WINDOW
def add_book_command(): # call RRmain.add_book
    print("cmd went through")
    root = tk.Tk()  # Create window
    root.title("Ryan's Reads")  # Name Window
    root.minsize(width=600, height=500)
    root.config(bg="#22223b")

    # title
    title = tk.Label(text="Get a list of books by filter")
    title.pack()
    
    # frame
    add_book_screen = tk.Frame(root, bg="#23344a")
    add_book_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    bfont = tkFont.Font(size=12, weight="bold")
    
    # buttons
    author_list = tk.Button(add_book_screen, text="Get a list by author name", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=find_book.get_book_author)
    uncompleted_list = tk.Button(add_book_screen, text="Get a list by uncompleted books", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=find_book.get_uncompleted_books)
    completed_list = tk.Button(add_book_screen, text="Get a list by completed books", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=find_book.get_completed_books)

    author_list.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15)
    uncompleted_list.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=0.4)
    completed_list.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=.8)


# HOMESCREEN
def title_screen():
    root = tk.Tk()  # Create window
    root.title("Ryan's Reads")  # Name Window
    root.minsize(width=600, height=500)
    root.config(bg="#22223b")
    
    # title
    title = tk.Label(root, text="Welcome to Ryan's Reads!", font=(16), bg="#22223b", fg="#ffffff")
    title.pack()

    # buttons
    home_screen = tk.Frame(root, bg="#23344a")
    home_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    bfont = tkFont.Font(size=12, weight="bold")

    add_book = tk.Button(home_screen, text="Add a new book", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=lambda:[add_book_command(), root.destroy()])
    list_books = tk.Button(home_screen, text="Get a list of books by title or author", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff")
    edit = tk.Button(home_screen, text="Edit information on an existing book", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff")
    quit = tk.Button(home_screen, text="Exit", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=root.destroy)
    
    add_book.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15)
    list_books.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=0.26)
    edit.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=.53)
    quit.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=.8)

title_screen()


if __name__ == '__main__':
    tk.mainloop()
