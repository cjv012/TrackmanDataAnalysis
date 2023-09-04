import matplotlib.pyplot as plt
import csv
from pitcher import Pitcher
from pitch import Pitch
import numpy as np
import matplotlib.patches as mpatches

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
      #print(str(player) + "\n" + str(player.avgFastball()) + "\n" + str(player.avgChangeup()) + "\n"+ str(player.avgCurveball()) + "\n"+ str(player.avgSlider()) + "\n"+ str(player.avgSplitter()) + "\n" + str(player.avgCutter()) + "\n" + str(player.avgSinker()) + "\n" + str(player.avgTwoSeam()) + "\n")

def pltPitches(Player): 
  xFast = []
  yFast = []

  xChup = []
  yChup = []

  xSplit = []
  ySplit = []

  xSlid = []
  ySlid = []

  xCurv = []
  yCurv = []

  xSink = []
  ySink = []

  xTsea = []
  yTsea = []

  xCutt = []
  yCutt = []

  for pitch in Player.pitches:
      if pitch.ptype == "Fastball":
        xFast.append(float(pitch.plside))
        yFast.append(float(pitch.plheight))
      elif pitch.ptype == "ChangeUp":
        xChup.append(float(pitch.plside))
        yChup.append(float(pitch.plheight))
      elif pitch.ptype == "Splitter":
        xSplit.append(float(pitch.plside))
        ySplit.append(float(pitch.plheight))
      elif pitch.ptype == "Slider":
        xSlid.append(float(pitch.plside))
        ySlid.append(float(pitch.plheight))
      elif pitch.ptype == "Curveball":
        xCurv.append(float(pitch.plside))
        yCurv.append(float(pitch.plheight))
      elif pitch.ptype == "Sinker":
        xSink.append(float(pitch.plside))
        ySink.append(float(pitch.plheight))
      elif pitch.ptype == "TwoSeamFastball":
        xTsea.append(float(pitch.plside))
        yTsea.append(float(pitch.plheight))
      elif pitch.ptype == "Cutter":
        xCutt.append(float(pitch.plside))
        yCutt.append(float(pitch.plheight))

  rect=mpatches.Rectangle((-.8,1.3),1.6,2.2, fill = False, color = "purple", linewidth = 2)    
  plt.gca().add_patch(rect)
  plt.scatter(xFast, yFast, label= "Fastballs", c= "blue", marker= ".")
  plt.scatter(xChup, yChup, label= "Changeups", c= "red", marker= ".")
  plt.scatter(xSplit, ySplit, label= "Splitters", c= "green", marker= ".")
  plt.scatter(xSlid, ySlid, label= "Sliders", c= "orange", marker= ".")
  plt.scatter(xCurv, yCurv, label= "Curveballs", c= "purple", marker= ".")
  plt.scatter(xCutt, yCutt, label= "Cutters", c= "yellow", marker= ".")
  plt.scatter(xSink, ySink, label= "Sinkers", c= "pink", marker= ".")
  plt.scatter(xTsea, yTsea, label= "TwoSeams", c= "brown", marker= ".")
  #fig, ax = plt.subplots()   
  plt.xlabel('Pitch Width (ft)')

  plt.ylabel('Pitch Height (ft)')

  #ax.add_patch(Rectangle((1, 1), -1, 1, edgecolor = 'blue', facecolor = 'blue', fill=False, lw=5))
  plt.title(" Location")

  plt.legend()
  plt.show()
  plt.savefig((str(Player.name) + 'Pitches.png'))
  plt.clf()

for players in pitchers:
  pltPitches(players)
writePitcherData()