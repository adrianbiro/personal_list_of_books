#!/usr/bin/python3
import csv
"""A try for the organization of a personal list of books."""
# TODO Clean-up of data to SQLite format for comfortable querying

with open("Archiv_literatura.csv", 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',dialect='unix', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Name", "Title", "Town", "Publisher", "Date"])
    with open("Archiv-literatúra.txt") as f:
        for i in f.readlines():
            i.replace("• ", "")
            name, *title = i.replace("•", "").strip().split(":")
            name = name.strip()  # name
            title = " ".join(title)
            title, *pub_date = title.split(",")
            *title, town = title.split(".")
            if not town:
                town = "None"
            town = town.strip()  # town
            title = " ".join(title)  # title
            try:
                publisher, *date = pub_date
            except ValueError:
                publisher, date  = title, "None"
            if not town:
                publisher = "None"
            publisher = publisher.strip()  # publisher
            date = " ".join(date).strip()
            if date == "N o n e":
                date = "None"  # date
            filewriter.writerow([name, title, town, publisher, date])
