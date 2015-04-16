from Tkinter import *
from WebScrape import run

master = Tk()
master.geometry("200x80")
master.maxsize(200, 80)
master.minsize(200, 80)


def exit():
    sys.exit()


def about():
    about_window = Toplevel()
    about_window.title("About")
    about_window.maxsize(200, 100)
    about_window.minsize(200, 100)
    message = Message(about_window, text="WebCrawler by: Andrew Ghaly, Albert Saunders, Thomas DeMarco")

    message.pack()

    button = Button(about_window, text="OK", command=about_window.destroy)
    button.pack()

label = Label(text="Enter website to start from")
http = Label(text="http://")

menu = Menu(master, tearoff=0)
master.config(menu=menu)
sub_menu = Menu(menu)
sub_menu.add_command(label="About", command=about)
sub_menu.add_separator()
sub_menu.add_command(label="Exit", command=exit)
menu.add_cascade(label="File", menu=sub_menu)


entry = Entry()

textbox = Text()

title = master.title("Web Crawl")


def call():
    #run(entry) where entry is link entered as paramater to WebScrape
    run(entry.get())


go = Button(text="GO", command=call)


label.grid(columnspan=2)
http.grid(row=1, column=0, sticky="e")

entry.grid(row=1, column=1)

go.grid(row=2, columnspan=3)


mainloop()

