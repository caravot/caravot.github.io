#!/bin/python
import os
import sys
from bs4 import BeautifulSoup

with open('data.txt') as file:
    sdata = file.readlines()

# first attempt
soup = BeautifulSoup(str(sdata), "html.parser")
mydivs = soup.find_all("article")

final = []
for div in mydivs:
        title = div.findChild('h1')
        times = div.findChildren('time')
        location = div.findChild('div', class_='event-stage')
        if title != None:
            final.append(title)
            print title
            print '----'
            print str(location)
            print '----'
            print str(times)
            print '====='

f = open('output.txt', 'w')
f.writelines([str(line) + "\n" for line in final])

# second attempt
soup = BeautifulSoup(str(sdata), "html.parser")
mydivs = soup.find_all("div", class_="event-modal-container")

final = []
for div in mydivs:
        title = div.findChild('h1')
        times = div.findChildren('time')
        location = div.findChild('div', class_='event-stage')
        description = div.findChild('div', class_='event-description')
        if title != None:
            final.append(title)
            print title
            print '----'
            print str(location)
            print '----'
            print str(times)
            print '----'
            print str(description)
            print '====='

f = open('output.txt', 'w')
f.writelines([str(line) + "\n" for line in final])
