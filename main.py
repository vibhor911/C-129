import csv

data = []

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers = data[0]
sun_data = data[1:]

#Converting all planet names to lower case
for data_point in sun_data:
    data_point[2] = data_point[2].lower()

#Sorting planet names in alphabetical order
sun_data.sort(key=lambda sun_data: sun_data[2])


with open("data_sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(sun_data)
