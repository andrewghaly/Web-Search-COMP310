from Tkinter import *
from WebScrape import run

master = Tk()
master.geometry("200x80")
master.maxsize(200, 80)
master.minsize(200, 80)

label = Label(text="Enter website to start from")
http = Label(text="http://")

entry = Entry()

title = master.title("Web Crawl")


def call():
    #run(entry) where entry is link entered as paramater to WebScrape
    run(entry.get())
    def exit():
        sys.exit()
    exit = Button(text="EXIT", command=exit)
    exit.grid(row=2, columnspan=2)



go = Button(text="GO", command=call)


label.grid(columnspan=2)
http.grid(row=1, column=0, sticky="e")

entry.grid(row=1, column=1)

go.grid(row=2, columnspan=3)


mainloop()

