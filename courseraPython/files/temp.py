import csv

fhand = open('whc-sites-2018-clean.csv')
reader = csv.reader(fhand)
# next(reader)  # Advance past the header
i = 50
for row in reader:
    print(row)
