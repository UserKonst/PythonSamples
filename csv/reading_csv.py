import csv

link = ''
with open("find_the_link.csv", encoding="utf-8") as file:
    csv_file = csv.reader(file)
    lines = list(csv_file)

    for i in range(0, len(lines)):
        link += lines[i][i]

print(link)
