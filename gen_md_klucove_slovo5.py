#!/usr/bin/python3
import csv

key_w = input("Daj klúčove slovo:\n> ")
data = csv.reader(open("clean4_literatura.csv"), delimiter=",")

nlist = []
for i in data:
    formi = " ".join(i).strip()
    if key_w in " ".join(i).lower():

        nlist.append(formi)

with open(f'{key_w}.md', 'w') as f:
    bulet_list = ["* {}".format(i) for i in nlist]
    f.write(f"# Knihy obsahujuce slovo {key_w}\n\n")
    for i in bulet_list:
        f.write(f'{i}\n')



