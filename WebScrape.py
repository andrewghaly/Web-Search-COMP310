from bs4 import BeautifulSoup
import urllib2
import re

def run(start_link):
    urls = []
    history = set()

    set_of_links = set()


    def scan_link(link):
        try:
            #link = "http://" + link
            site_load = urllib2.urlopen(link)
            print "\nScraping link: ", link.split("http://")[1]

            current_link = BeautifulSoup(site_load)
            print current_link.html.head.title.string
            for link in current_link.findAll('a'):
                if link.get('href') not in urls:
                    urls.append(link.get('href'))
        except Exception:
            print ""

    scan_link("http://" + start_link)

    while urls:
        for x in urls:
            print x
            #print len(urls)

            print len(urls), "URLs in stack"
            print len(history), "URLs in history"

            scan_link(x)
            urls.pop()
            if x not in history:
                history.add(x)

