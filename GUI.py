from Tkinter import *
from WebScrape import run

master = Tk()


label = Label(text="Enter website to start from")

entry = Entry()

title = master.title("Web Crawl")

def call():
    #run(entry) where entry is link entered as paramater to WebScrape
    run(entry.get())

button = Button(master, text="GO", command=call)

label.pack()

entry.pack()
button.pack()

mainloop()

