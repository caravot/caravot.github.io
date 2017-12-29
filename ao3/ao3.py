#!/bin/python
import csv
import re
import httplib
import urllib
from pprint import pprint
from bs4 import BeautifulSoup

for category in [
    'Movies',
    'Theater',
    'Anime%20*a*%20Manga',
    'Cartoons%20*a*%20Comics%20*a*%20Graphic%20Novels',
    'TV%20Shows',
    'Books%20*a*%20Literature',
    'Music%20*a*%20Bands',
    'Video%20Games',
    'Uncategorized%20Fandoms',
    'Other%20Media'
]:
    print category
    conn = httplib.HTTPConnection("archiveofourown.org")
    conn.request("GET", "/media/" + category + "/fandoms")
    r = conn.getresponse()
    soup = BeautifulSoup(str(r.read()), "html.parser")
    conn.close()

    containers = soup.find_all("ul", class_="tags")

    final = []
    for container in containers:
        items = container.findChildren('li')

        for item in items:
            title = item.a.text

            unwanted = item.a
            unwanted.extract()

            txt = item.text.replace('\s', '')
            num = re.findall(r'\(\d*\)', txt)[0].replace('(', '').replace(')', '')

            final.append([title.encode('utf-8'), num])

    final = sorted(final, key=lambda x: int(x[1]), reverse=True)

    finalname = re.sub(r'[^A-Za-z]', '', category)
    csvfile = open(finalname + '.csv', 'wb')
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerows(final)
