import csv

pitchers = {}

with open("20230830-DepewField-Private-2_unverified.csv", 'r') as file:
  csvreader = csv.reader(file)
  i = 0
  for row in csvreader:
    if row[5] not in pitchers and (i != 0):
       pitchers[(row[5])] = {'Pitches': 0, 'Fastballs': 0, 'Curveballs': 0, }
    if (i == 0):
      print(row)
    i += 1
print(pitchers)