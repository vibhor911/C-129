import csv

data1 = []
data2 = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data1.append(row)

with open("data_sorted.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data2.append(row)

headers_1 = data1[0]
sun_data_1 = data1[1:]

headers_2 = data2[0]
sun_data_2 = data2[1:]

headers = headers_1 + headers_2
sun_data = []
for index, data_row in enumerate(sun_data_1):
    sun_data.append(sun_data_1[index] + sun_data_2[index])

with open("data.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(sun_data)
