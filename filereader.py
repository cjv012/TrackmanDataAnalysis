import csv
from pitcher import Pitcher
from pitch import Pitch

def readPitch(arr):
  pitch = Pitch(arr[1], arr[19], arr[28], arr[21], arr[31], arr[38], arr[39], arr[33], arr[34], arr[35], arr[35], arr[40], arr[41])
  return pitch


pitchers = []

with open("20230830-DepewField-Private-2_unverified.csv", 'r') as file:
  csvreader = csv.reader(file)
  i = 0
  for row in csvreader:
    nameIn = 1
    pitcherLoc = 0
    for x in range(len(pitchers)):
      if pitchers[x].name == row[5]:
        nameIn = 0
        pitcherLoc = x
    if (nameIn == 1) and (i != 0):
       thrower = Pitcher(row[5], row[7])
       pitchers.append(thrower)
       pitcherLoc = len(pitchers) - 1
    if (i != 0):
      pitchers[pitcherLoc].insertPitch(readPitch(row))
      
    i += 1
for player in pitchers:
  print(str(player) + "\n" + str(player.pitches[0]))