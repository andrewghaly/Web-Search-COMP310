from bs4 import BeautifulSoup
import urllib2
import re

urls = []
history = []

set_of_links = set()


def scan_link(link):
    try:
        site_load = urllib2.urlopen(link)
        print "\nScraping link: ", link.split("http://")[1]

        current_link = BeautifulSoup(site_load)
        print current_link.html.head.title.string
        for link in current_link.findAll('a', attrs={'href': re.compile("^http://")}):
            if link.get('href') not in urls:
                urls.append(link.get('href'))
    except Exception:
        print ""

scan_link("http://www.wit.edu")

while urls:
    for x in urls:
        print x
        #print len(urls)

        print len(urls), "URLs in stack"
        print len(history), "URLs in history"

        scan_link(x)
        urls.pop(0)
        if x not in history:
            history.append(x)