import tkinter as tk
import tkinter.font as tkFont
from supporting_scripts import RRmain
from supporting_scripts import find_book


# LIST_BOOK WINDOW
def list_book_window(): # DONE
    root = tk.Tk()  # Create window
    root.title("Ryan's Reads")  # Name Window
    root.minsize(width=600, height=500)
    root.config(bg="#22223b")

    # title
    title = tk.Label(text="Get a list of books by filter")
    title.pack()
    
    # frame
    list_book_screen = tk.Frame(root, bg="#23344a")
    list_book_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    bfont = tkFont.Font(size=12, weight="bold")
    
    # buttons THIS IS WHERE THE STUPID TITLES FROM RRmain.py ARE USED
    author_list = tk.Button(list_book_screen, text="Get a list by author name", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=lambda:[RRmain.two_one()])
    uncompleted_list = tk.Button(list_book_screen, text="Get a list by uncompleted books", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=lambda:[RRmain.two_two()])
    completed_list = tk.Button(list_book_screen, text="Get a list by completed books", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=lambda:[RRmain.two_three()])
    all_books = tk.Button(list_book_screen, text="Get a list of all books", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=lambda:[find_book.get_all_books()])
    go_to_start = tk.Button(list_book_screen, text="Return to homescreen", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=lambda:[title_screen(), root.destroy()])

    author_list.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15)
    uncompleted_list.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=0.2)
    completed_list.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=.4)
    all_books.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=.6)
    go_to_start.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=.8)


# HOMESCREEN
def title_screen(): # DONE
    root = tk.Tk()  # Create window
    root.title("Ryan's Reads")  # Name Window
    root.minsize(width=600, height=500)
    root.config(bg="#22223b")
    
    # title
    subtitle_font = tkFont.Font(size=12)
    title = tk.Label(root, text="Welcome to Ryan's Reads!", font=(16), bg="#22223b", fg="#ffffff")
    subtitle = tk.Label(root, text="Use the terminal to see complete inputs and see outputs!", font=subtitle_font, bg="#22223b", fg="#ffffff")
    title.pack()
    subtitle.pack()
    
    # buttons
    home_screen = tk.Frame(root, bg="#23344a")
    home_screen.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
    bfont = tkFont.Font(size=12, weight="bold")

    add_book = tk.Button(home_screen, text="Add a new book", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=RRmain.one)
    list_books = tk.Button(home_screen, text="Get a list of books by title or author", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=lambda:[list_book_window(), root.destroy()])
    edit = tk.Button(home_screen, text="Display information on an existing book", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=RRmain.three)
    quit = tk.Button(home_screen, text="Exit", font=bfont, bg="#38502a", activebackground="#393f2d", fg="#ffffff", command=root.destroy)
    
    add_book.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15)
    list_books.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=0.26)
    edit.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=.53)
    quit.place(bordermode="outside", relheight=0.2, relwidth=0.7, relx=0.15, rely=.8)

title_screen()


if __name__ == '__main__':
    tk.mainloop()
