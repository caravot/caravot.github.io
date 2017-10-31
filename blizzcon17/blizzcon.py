#!/bin/python
import csv
from bs4 import BeautifulSoup

with open('data.txt') as file:
    sdata = file.readlines()

csvfile = open('output.csv', 'wb')
spamwriter = csv.writer(csvfile, delimiter='\t')

# second attempt
soup = BeautifulSoup(str(sdata), "html.parser")
mydivs = soup.find_all("div", class_="event-modal-container")

final = []
for div in mydivs:
        title = div.findChild('h1')
        times = div.findChildren('time')
        location = div.findChild('div', class_='event-stage')
        description = div.findChild('div', class_='event-description')

        event = []

        if title != None:
            #print title.get_text()
            event.append(title.get_text())

            #print str(location.get_text())
            event.append(location.get_text())

            #print str(times)
            if len(times) == 4:
                stime = div.find_all('time', itemprop='startTime')
                etime = div.find_all('time', itemprop='endTime')

                event.append(stime[0].attrs.get('datetime', ''))
                event.append(etime[0].attrs.get('datetime', ''))
                event.append(stime[1].attrs.get('datetime', ''))
                event.append(etime[1].attrs.get('datetime', ''))

            if description != None:
                #print str(description.get_text())
                event.append(description.get_text())

        final.append([str(line) for line in event])
        csvfile.write('\t'.join(event))
#f = open('output.csv', 'w')
#f.writelines([str(line) + '\n' for line in final])
# with open('output.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter='\t')
#     spamwriter.writerows([str(line) for line in final])
