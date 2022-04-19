#!/usr/bin/python3
import csv
import operator


data = csv.reader(open("Archiv_literatura.csv"), delimiter=",")
sortedlist = sorted(data, key=operator.itemgetter(0), reverse=False)

with open("sorted_literatura.csv", 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',dialect='unix', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Name", "Title", "Town", "Publisher", "Date"])
    for i in sortedlist:
        name, title, town, publisher, date = i
        filewriter.writerow([name, title, town, publisher, date])
