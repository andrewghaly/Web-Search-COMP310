from bs4 import BeautifulSoup
import urllib2
import re
from Tkinter import *
import Tkinter as tk

urls = []
history = []

set_of_links = set()


class StartPage(tk.Frame):

    def __init__(self, master=None):
            Frame.__init__(self, master)
            self.root = master
            self.master.title("WebCrawler")
            self.pack()
            self.create_widgets(self)

    def scan_link(self):
        try:
            link = entry1.get()
            site_load = urllib2.urlopen(link)
            text.insert("\nScraping link: ", link.split("http://")[1])

            current_link = BeautifulSoup(site_load)
            text.insert(current_link.html.head.title.string)
            for link in current_link.findAll('a', attrs={'href': re.compile("^http://")}):
                if link.get('href') not in urls:
                    urls.append(link.get('href'))
        except Exception :
                text.insert("")

        a = self.entry1.get()
        scan_link(a)

    while urls:
        for x in urls:
            text.insert(x)
        # print len(urls)

            text.insert(len(urls), "URLs in stack")
            text.insert(len(history), "URLs in history")

            scan_link(x)
            urls.pop(0)
            if x not in history:
                history.append(x)

    def create_widgets(self, scan_link):
        label = tk.Label(self, text="Please Enter in a website url to parse")
        label.grid(row=0, columnspan=2)
        entry1 = tk.Entry(self)
        entry1.grid(row=1, column=0, sticky="e")
        button = tk.Button(self, text="  GO  ", command=scan_link)
        button.grid(row=1, column=1, sticky="w")
        text = tk.Text(self)
        text.grid(row=2, columnspan=2)

app = StartPage()
app.mainloop()

