import csv
from pitcher import Pitcher
from pitch import Pitch

def readPitch(arr):
  pitch = Pitch(arr[1], arr[19], arr[28], arr[21], arr[31], arr[38], arr[39], arr[33], arr[34], arr[35], arr[35], arr[40], arr[41])
  return pitch


pitchers = []

def readCSV(csvfileString):
  with open(csvfileString, 'r') as file:
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

readCSV("20230829-DepewField-Private-2_unverified.csv")
readCSV("20230830-DepewField-Private-1_unverified.csv")
readCSV("20230830-DepewField-Private-2_unverified.csv")

def writePitcherData():
  with open('pitcherData.txt', 'w') as f:
    for player in pitchers:
      pitcherString = (str(player) + "\n" + str(player.avgFastball()) + "\n" + str(player.avgChangeup()) + "\n"+ str(player.avgCurveball()) + "\n"+ str(player.avgSlider()) + "\n"+ str(player.avgSplitter()) + "\n" + str(player.avgCutter()) + "\n" + str(player.avgSinker()) + "\n" + str(player.avgTwoSeam()) + "\n")
      f.write(pitcherString)
      print(str(player) + "\n" + str(player.avgFastball()) + "\n" + str(player.avgChangeup()) + "\n"+ str(player.avgCurveball()) + "\n"+ str(player.avgSlider()) + "\n"+ str(player.avgSplitter()) + "\n" + str(player.avgCutter()) + "\n" + str(player.avgSinker()) + "\n" + str(player.avgTwoSeam()) + "\n")

writePitcherData()