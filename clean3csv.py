#!/usr/bin/python3
import csv

data = csv.reader(open("sorted_literatura.csv"), delimiter=",")

with open("clean3_literatura.csv", 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',dialect='unix', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Name", "Title", "Town", "Publisher", "Date"])
    for i in data:
        name, title, town, publisher, date = i
        if name == "Name" and title == "Title" and town == "Town" and  publisher == "Publisher" and date == "Date":
            continue
        if name == "" and title == "" and town == "" and  publisher == "" and date == "":
            continue
        name = name.replace("[", "").replace("]", "").replace("/", ";").replace("  ", " ").title()
        title = title.replace("[", "").replace("]", "").replace("  ", " ").strip()
        town = town.replace("[", "").replace("]", "").title()
        publisher = publisher.replace("[", "").replace("]", "").title()
        if not title:
            title, town = town, ""
        if title == "Praha" and town == "":
            title, town = "", title
        if title == "None":
            title = ""
        if town == "None":
            town = ""
        if publisher == "None":
            publisher = ""
        if date == "None":
            date = ""

        #date = date.replace("[", "").replace("]", "")
        #print(name, title, town, publisher, date)


        filewriter.writerow([name, title, town, publisher, date])

