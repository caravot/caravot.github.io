#!/bin/python

import httplib
import urllib
from bs4 import BeautifulSoup

for volume in range(1, 15):
    print volume
    volume = str(volume)
    conn = httplib.HTTPConnection("m.mangafox.me")
    if volume < 10:
        conn.request("GET", "/manga/love_hina/v0" + volume + "/c000/1.html")
    else:
        conn.request("GET", "/manga/love_hina/v" + volume + "/c000/1.html")
    r = conn.getresponse()
    soup = BeautifulSoup(str(r.read()), "html.parser")
    select = soup.find("select", attrs={"class": "mangaread-page"})
    values = list(select.stripped_strings)
    last_page = int(values[-1])
    print last_page
    conn.close()

    for i in range(1, last_page):
        conn = httplib.HTTPConnection("m.mangafox.me")
        strI = str(i)
        if volume < 10:
            conn.request("GET", "/manga/love_hina/v0" + volume + "/c000/" + strI + ".html")
        else:
            conn.request("GET", "/manga/love_hina/v" + volume + "/c000/" + strI + ".html")
        r = conn.getresponse()
        soup = BeautifulSoup(str(r.read()), "html.parser")
        mydivs = soup.find_all("img", attrs={"id": "image"})
        imgsrc = mydivs[0].get('src')
        print i

        if i < 10:
            urllib.urlretrieve(imgsrc, "images/" + volume + "/0000" + strI + ".jpg")
        else:
            urllib.urlretrieve(imgsrc, "images/" + volume + "/000" + strI + ".jpg")

        conn.close()
