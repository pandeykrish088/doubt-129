import csv
data1 = []

with open("dwarf_Stars_sorted.csv") as a:
    csvReader = csv.reader(a)

    for row in csvReader:
        data1.append(row)

data2 = []

with open("bright_stars_sorted.csv") as b:
    csvReader = csv.reader(b)

    for row in csvReader:
        data2.append(row)

header1 = data1[0]
header2 = data2[0]

dwarf_stars = data1[1:]
bright_stars = data2[1:]

data = []
for index, row in enumerate(dwarf_stars):
    data.append(dwarf_stars[index] + bright_stars[index])

header = header1 + header2

with open("merged_dataset.csv", "w", newline = "") as m:
    csvWriter = csv.writer(m)
    csvWriter.writerow(header)
    csvWriter.writerows(data)