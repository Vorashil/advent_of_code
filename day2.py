import csv

with open('input_day2.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


print(data)
