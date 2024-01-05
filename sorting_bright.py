import csv
data = []

with open("bright_stars.csv") as a:
    csvReader = csv.reader(a)

    for row in csvReader:
        data.append(row)

header = data[0]

stars_data = data[1:]

for row in stars_data:
    row[1] = row[1].lower()

stars_data.sort(key = lambda stars_data: stars_data[1])

with open("bright_stars_sorted.csv", "w", newline = "") as e:
    csvWriter = csv.writer(e)
    csvWriter.writerow(header)
    csvWriter.writerows(stars_data)