#!/usr/bin/python3
import csv

data = csv.reader(open("old/clean3_literatura.csv"), delimiter=",")

with open("clean4_literatura.csv", 'w', newline='') as csvfile:
    header_list = ["Name", "Title", "Town", "Publisher", "Date"]
    dw = csv.DictWriter(csvfile, delimiter=',', dialect='unix', fieldnames=header_list, quoting=csv.QUOTE_MINIMAL)
    dw.writeheader()
    filewriter = csv.writer(csvfile, delimiter=',', dialect='unix', quoting=csv.QUOTE_MINIMAL)
    for i in data:
        name, title, town, publisher, date = i
        if name == "Name" and title == "Title" and town == "Town" and  publisher == "Publisher" and date == "Date":
            continue
        if name and not title and not town and not  publisher and not date:
            *name, date = name.split(" ")
            date = date.replace(".", "")
            if len(date) == 4:
                date = date
            else:
                date = date.split(",")
                if len(date) > 1 :
                    *pub, date = date
                    for i in pub:
                        name.append(i)
            try:
                *name, publisher = name
            except ValueError:
                name = name
            try:
                if int(publisher):
                    publisher, date = date, publisher
            except:
                pass
            #####
            try:
                *name, town = name
            except ValueError:
                name = name
            town = town.replace(".", "").replace(",", "")
            try:
                if int(town):
                    town, date = date, town
            except:
                pass
            try:
                *name, title = name
                title.replace(".", "").replace(",", "")
            except ValueError:
                name = name
            try:
                if name[-1] == "Praha":
                        pub = publisher
                        tow = town
                        town = name[-1]
                        publisher = tow
                        print(name, title, town, publisher, date)
            except IndexError:
                pass
            name = " ".join(name)


            #print("-"*20)
            #print(title)
            #print(name)
            #print(name, title, town, publisher, date)

            filewriter.writerow([name, title, town, publisher, date])
        else:
            filewriter.writerow([name, title, town, publisher, date])
            continue




