import matplotlib.pyplot as plt
import matplotlib.pyplot as fig
import matplotlib.pyplot as ax
import csv
from pitcher import Pitcher
from pitch import Pitch
from hitter import Hitter
from hit import Hit
import numpy as np
import matplotlib.patches as mpatches
import math

def compDates(beginDate, date, endDate):
  """Returns 1 if date is in the date range and 0 if it is not"""
  if int(beginDate[0]) == int(date[0]):
    if int(beginDate[1]) == int(date[1]):
      if int(beginDate[2]) == int(date[2]):
        return 1
  else:
    return 0

def readPitch(arr):
  """Reads a line from the trackman csv and documents it as a pitch object"""
  pitch = Pitch(arr[1], arr[19], arr[28], arr[21], arr[31], arr[38], arr[39], arr[32], arr[33], arr[34], arr[35], arr[35], arr[40], arr[41])
  return pitch

def readHit(arr):
  """Reads a line from the trackman csv and documents it as a pitch object"""
  if arr[21] == "InPlay":
    hit = Hit(arr[1], arr[47], arr[46], arr[24], arr[19], arr[53])
  else:
    hit = None
  return hit


pitchers = []
hitters = []

def readCSV(csvfileString):
  """Opens a CSV file and reads in the rows and attributes each pitch to a pitcher that is placed in the picher array as a pitcher object"""
  with open(csvfileString, 'r') as file:
    csvreader = csv.reader(file)
    i = 0
    for row in csvreader:
      PnameIn = 1
      HnameIn = 1
      pitcherLoc = 0
      hitterLoc = 0
      maxLen = 0
      if len(pitchers) > len(hitters):
        maxLen = len(pitchers)
      else:
        maxLen = len(hitters)
      for x in range(maxLen):
        if len(row) != 0:
          if x < len(pitchers):
            if pitchers[x].name.upper() == row[5].upper():
              PnameIn = 0
              pitcherLoc = x
          if x < len(hitters):
            if hitters[x].name.upper() == row[9].upper():
              hitterLoc = x
              HnameIn = 0
      if (PnameIn == 1) and (i != 0) and (len(row) != 0):
        thrower = Pitcher(row[5], row[7])
        pitchers.append(thrower)
        pitcherLoc = len(pitchers) - 1
      if (HnameIn == 1) and (i != 0) and (len(row) != 0):
        batter = Hitter(row[9], row[7])
        hitters.append(batter)
        hitterLoc = len(pitchers) - 1
      if (i != 0) and (len(row) != 0):
        pitchers[pitcherLoc].insertPitch(readPitch(row))
        if readHit(row) != None:
          hitters[hitterLoc].insertHit(readHit(row))
        if row[21] == "SwingingStrike":
            hitters[hitterLoc].swingingMiss()
        if row[21] == "SwingingStrike" and row[19] == "Fastball":
            hitters[hitterLoc].missFast()
        
      i += 1

#readCSV("20230829-DepewField-Private-2_unverified.csv")
#readCSV("20230830-DepewField-Private-1_unverified.csv")
#readCSV("20230830-DepewField-Private-2_unverified.csv")
#readCSV("20230909-DepewField-Private-1_unverified.csv")
#readCSV("20230916-DepewField-Private-2_unverified.csv")
#readCSV("20230917-DepewField-Private-1_unverified.csv")
readCSV("20230922-DepewField-Private-1_unverified.csv")
readCSV("20230923-DepewField-Private-2_unverified.csv")
readCSV("20231005-DepewField-Private-2_unverified.csv")
readCSV("20231001-DepewField-Private-1_unverified.csv")
#readCSV("20231003-DepewField-Private-1_unverified.csv")
readCSV("20231004-DepewField-Private-1_unverified.csv")

def writePitcherData(player):
  """Writes the averages of all of the pitchers data to a text document"""
  with open('pitcherData.txt', 'w') as f:
    pitcherString = (str(player) + "\n" + str(player.totStrike()) + "\n" + str(player.avgFastball()) + "\n" + str(player.avgChangeup()) + "\n"+ str(player.avgCurveball()) + "\n"+ str(player.avgSlider()) + "\n"+ str(player.avgSplitter()) + "\n" + str(player.avgCutter()) + "\n" + str(player.avgSinker()) + "\n" + str(player.avgTwoSeam()) + "\n")
    f.write(pitcherString)
    return(pitcherString)
      #print(str(player) + "\n" + str(player.avgFastball()) + "\n" + str(player.avgChangeup()) + "\n"+ str(player.avgCurveball()) + "\n"+ str(player.avgSlider()) + "\n"+ str(player.avgSplitter()) + "\n" + str(player.avgCutter()) + "\n" + str(player.avgSinker()) + "\n" + str(player.avgTwoSeam()) + "\n")

def writeHitterData(hitter):
  with open('hitterData.txt', 'w') as f:
    hitterString = (str(hitter))
    f.write(hitterString)
    return hitterString

def formatHTML(string):
  """Replace newline characters with breaks to format according to HTML formats"""
  return_string = string.replace("\n", "<br>")
  return return_string

def pltPitches(Player): 
  """Creates of a plot of all of the players given pitches plotted on a scatter plot with a zone and exported as a .png with the pitchers name"""
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
      if (pitch.ptype == "Fastball" or pitch.ptype == "FourSeamFastBall") and pitch.plside != "":
        xFast.append(float(pitch.plside))
        yFast.append(float(pitch.plheight))
      elif pitch.ptype == "ChangeUp" and pitch.plside != "":
        xChup.append(float(pitch.plside))
        yChup.append(float(pitch.plheight))
      elif pitch.ptype == "Splitter" and pitch.plside != "":
        xSplit.append(float(pitch.plside))
        ySplit.append(float(pitch.plheight))
      elif pitch.ptype == "Slider" and pitch.plside != "":
        xSlid.append(float(pitch.plside))
        ySlid.append(float(pitch.plheight))
      elif pitch.ptype == "Curveball" and pitch.plside != "":
        xCurv.append(float(pitch.plside))
        yCurv.append(float(pitch.plheight))
      elif pitch.ptype == "Sinker" and pitch.plside != "":
        xSink.append(float(pitch.plside))
        ySink.append(float(pitch.plheight))
      elif pitch.ptype == "TwoSeamFastBall" and pitch.plside != "":
        xTsea.append(float(pitch.plside))
        yTsea.append(float(pitch.plheight))
      elif pitch.ptype == "Cutter" and pitch.plside != "":
        xCutt.append(float(pitch.plside))
        yCutt.append(float(pitch.plheight))

  rect=mpatches.Rectangle((-.8,1.3),1.6,2.2, fill = False, color = "gray", linewidth = 2)   
  plt.gca().add_patch(rect)
  shadow=mpatches.Rectangle((-1,1.1),2,2.6, fill = False, color = "gray", linewidth = 2)    
  plt.gca().add_patch(shadow)
  if len(xFast) != 0:
    plt.scatter(xFast, yFast, label= "Fastballs", c= "blue", marker= ".")
  if len(xChup) != 0:
    plt.scatter(xChup, yChup, label= "Changeups", c= "red", marker= ".")
  if len(xSplit) != 0:
    plt.scatter(xSplit, ySplit, label= "Splitters", c= "green", marker= ".")
  if len(xSlid) != 0:
    plt.scatter(xSlid, ySlid, label= "Sliders", c= "orange", marker= ".")
  if len(xCurv) != 0:
    plt.scatter(xCurv, yCurv, label= "Curveballs", c= "purple", marker= ".")
  if len(xCutt) != 0:
    plt.scatter(xCutt, yCutt, label= "Cutters", c= "yellow", marker= ".")
  if len(xSink) != 0:
    plt.scatter(xSink, ySink, label= "Sinkers", c= "pink", marker= ".")
  if len(xTsea) != 0:
    plt.scatter(xTsea, yTsea, label= "TwoSeams", c= "brown", marker= ".")
  #fig, ax = plt.subplots()   
  plt.xlabel('Pitch Width (ft)')

  plt.ylabel('Pitch Height (ft)')

  #ax.add_patch(Rectangle((1, 1), -1, 1, edgecolor = 'blue', facecolor = 'blue', fill=False, lw=5))
  plt.title(str(Player.name) + "\'s Pitch Locations")
  plt.xlim(-3, 3)
  plt.ylim(-1, 5)
  plt.legend(fontsize = "8")
  plt.show()
  plt.savefig((str(Player.name) + 'Pitches.png'))
  plt.clf()

def pltMovement(Player): 
  """Creates of a plot of all of the players given pitches plotted on a scatter plot with a zone and exported as a .png with the pitchers name"""
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
      if (pitch.ptype == "Fastball" or pitch.ptype == "FourSeamFastBall") and pitch.hbreak != "":
        xFast.append(float(pitch.hbreak))
        yFast.append(float(pitch.vbreak))
      elif pitch.ptype == "ChangeUp" and pitch.hbreak != "":
        xChup.append(float(pitch.hbreak))
        yChup.append(float(pitch.vbreak))
      elif pitch.ptype == "Splitter" and pitch.hbreak != "":
        xSplit.append(float(pitch.hbreak))
        ySplit.append(float(pitch.vbreak))
      elif pitch.ptype == "Slider" and pitch.hbreak != "":
        xSlid.append(float(pitch.hbreak))
        ySlid.append(float(pitch.vbreak))
      elif pitch.ptype == "Curveball" and pitch.hbreak != "":
        xCurv.append(float(pitch.hbreak))
        yCurv.append(float(pitch.vbreak))
      elif pitch.ptype == "Sinker" and pitch.hbreak != "":
        xSink.append(float(pitch.hbreak))
        ySink.append(float(pitch.vbreak))
      elif pitch.ptype == "TwoSeamFastBall" and pitch.hbreak != "":
        xTsea.append(float(pitch.hbreak))
        yTsea.append(float(pitch.vbreak))
      elif pitch.ptype == "Cutter" and pitch.hbreak != "":
        xCutt.append(float(pitch.hbreak))
        yCutt.append(float(pitch.vbreak))
  if len(xFast) != 0:
    fig.scatter(xFast, yFast, label= "Fastballs", c= "blue", marker= ".")
  if len(xChup) != 0:
    fig.scatter(xChup, yChup, label= "Changeups", c= "red", marker= ".")
  if len(xSplit) != 0:
    fig.scatter(xSplit, ySplit, label= "Splitters", c= "green", marker= ".")
  if len(xSlid) != 0:
    fig.scatter(xSlid, ySlid, label= "Sliders", c= "orange", marker= ".")
  if len(xCurv) != 0:
    fig.scatter(xCurv, yCurv, label= "Curveballs", c= "purple", marker= ".")
  if len(xCutt) != 0:
    fig.scatter(xCutt, yCutt, label= "Cutters", c= "yellow", marker= ".")
  if len(xSink) != 0:
    fig.scatter(xSink, ySink, label= "Sinkers", c= "pink", marker= ".")
  if len(xTsea) != 0:
    fig.scatter(xTsea, yTsea, label= "TwoSeams", c= "brown", marker= ".")
  #fig, ax = plt.subplots()   
  fig.xlabel('Horizontal Break (in)')

  fig.ylabel('Vertical Break (in)')
  fig.axvline(x=0, c="black")
  fig.axhline(y=0, c="black")
  #ax.add_patch(Rectangle((1, 1), -1, 1, edgecolor = 'blue', facecolor = 'blue', fill=False, lw=5))
  fig.title(str(Player.name) + "\'s Pitch Movement")
  fig.xlim(-30, 30)
  fig.ylim(-30, 30)
  fig.legend(fontsize = "8")
  fig.show()
  fig.savefig((str(Player.name) + 'Movement.png'))
  fig.clf()

def pltSpin(Player): 
  """Creates of a plot of all of the players given spins axis plotted on a scatter plot with a zone and exported as a .png with the pitchers name"""
  FastAX = []
  FastSpin = []

  ChupAX = []
  ChupSpin = []

  SplitAX = []
  SplitSpin = []

  SlidAX = []
  SlidSpin = []

  CurvAX = []
  CurvSpin = []

  SinkAX = []
  SinkSpin = []

  TseaAX = []
  TseaSpin = []

  CuttAX = []
  CuttSpin = []
  fig = plt.figure()
  ax = fig.add_subplot(projection='polar')
  ax.set_theta_direction(-1)
  ax.set_theta_offset(math.pi / 2.0)
  for pitch in Player.pitches:
      if (pitch.ptype == "Fastball" or pitch.ptype == "FourSeamFastBall") and pitch.axis != "":        
        FastAX.append(float(pitch.axis)*(math.pi/6))
        FastSpin.append(float(pitch.spin))
      elif pitch.ptype == "ChangeUp" and pitch.axis != "":
        ChupAX.append(float(pitch.axis)*(math.pi/6))
        ChupSpin.append(float(pitch.spin))
      elif pitch.ptype == "Splitter" and pitch.axis != "":
        SplitAX.append(float(pitch.axis)*(math.pi/6))
        SplitSpin.append(float(pitch.spin))
      elif pitch.ptype == "Slider" and pitch.axis != "":
        SlidAX.append(float(pitch.axis)*(math.pi/6))
        SlidSpin.append(float(pitch.spin))
      elif pitch.ptype == "Curveball" and pitch.axis != "":
        CurvAX.append(float(pitch.axis)*(math.pi/6))
        CurvSpin.append(float(pitch.spin))
      elif pitch.ptype == "Sinker" and pitch.axis != "":
        SinkAX.append(float(pitch.axis)*(math.pi/6))
        SinkSpin.append(float(pitch.spin))
      elif pitch.ptype == "TwoSeamFastBall" and pitch.axis != "":
        TseaAX.append(float(pitch.axis)*(math.pi/6))
        TseaSpin.append(float(pitch.spin))
      elif pitch.ptype == "Cutter" and pitch.axis != "":
        CuttAX.append(float(pitch.axis)*(math.pi/6))
        CuttSpin.append(float(pitch.spin))
  if len(FastAX) != 0:
    ax.scatter(FastAX, FastSpin, label= "Fastballs", c= "blue", marker= ".")
  if len(ChupAX) != 0:
    ax.scatter(ChupAX, ChupSpin, label= "Changeups", c= "red", marker= ".")
  if len(SplitAX) != 0:
    ax.scatter(SplitAX, SplitSpin, label= "Splitters", c= "green", marker= ".")
  if len(SlidAX) != 0:
    ax.scatter(SlidAX, SlidSpin, label= "Sliders", c= "orange", marker= ".")
  if len(CurvAX) != 0:
    ax.scatter(CurvAX, CurvSpin, label= "Curveballs", c= "purple", marker= ".")
  if len(CuttAX) != 0:
    ax.scatter(CuttAX, CuttSpin, label= "Cutters", c= "yellow", marker= ".")
  if len(SinkAX) != 0:
    ax.scatter(SinkAX, SinkSpin, label= "Sinkers", c= "pink", marker= ".")
  if len(TseaAX) != 0:
    ax.scatter(TseaAX, TseaSpin, label= "TwoSeams", c= "brown", marker= ".")
  #fig, ax = plt.subplots()  

  #fig.xlabel('Horizontal Break (in)')

  #fig.ylabel('Vertical Break (in)')
  #fig.axvline(x=0, c="black")
  #fig.axhline(y=0, c="black")
  #ax.add_patch(Rectangle((1, 1), -1, 1, edgecolor = 'blue', facecolor = 'blue', fill=False, lw=5))
  plt.title(str(Player.name) + "\'s Spin Axis")
  #fig.xlim(-30, 30)
  plt.ylim(0, 3000)
  leg = plt.legend()
  ax.legend_ = None
  plt.show()
  plt.savefig((str(Player.name) + 'Spin.png'))
  plt.clf()

def pltRelease(Player): 
  """Creates of a plot of all of the players given pitches plotted on a scatter plot with a zone and exported as a .png with the pitchers name"""
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
      if (pitch.ptype == "Fastball" or pitch.ptype == "FourSeamFastBall") and pitch.rside != "":
        xFast.append(float(pitch.rside))
        yFast.append(float(pitch.rheight))
      elif pitch.ptype == "ChangeUp" and pitch.rside != "":
        xChup.append(float(pitch.rside))
        yChup.append(float(pitch.rheight))
      elif pitch.ptype == "Splitter" and pitch.rside != "":
        xSplit.append(float(pitch.rside))
        ySplit.append(float(pitch.rheight))
      elif pitch.ptype == "Slider" and pitch.rside != "":
        xSlid.append(float(pitch.rside))
        ySlid.append(float(pitch.rheight))
      elif pitch.ptype == "Curveball" and pitch.rside != "":
        xCurv.append(float(pitch.rside))
        yCurv.append(float(pitch.rheight))
      elif pitch.ptype == "Sinker" and pitch.rside != "":
        xSink.append(float(pitch.rside))
        ySink.append(float(pitch.rheight))
      elif pitch.ptype == "TwoSeamFastBall" and pitch.rside != "":
        xTsea.append(float(pitch.rside))
        yTsea.append(float(pitch.rheight))
      elif pitch.ptype == "Cutter" and pitch.rside != "":
        xCutt.append(float(pitch.rside))
        yCutt.append(float(pitch.rheight))

  if len(xFast) != 0:
    plt.scatter(xFast, yFast, label= "Fastballs", c= "blue", marker= ".")
  if len(xChup) != 0:
    plt.scatter(xChup, yChup, label= "Changeups", c= "red", marker= ".")
  if len(xSplit) != 0:
    plt.scatter(xSplit, ySplit, label= "Splitters", c= "green", marker= ".")
  if len(xSlid) != 0:
    plt.scatter(xSlid, ySlid, label= "Sliders", c= "orange", marker= ".")
  if len(xCurv) != 0:
    plt.scatter(xCurv, yCurv, label= "Curveballs", c= "purple", marker= ".")
  if len(xCutt) != 0:
    plt.scatter(xCutt, yCutt, label= "Cutters", c= "yellow", marker= ".")
  if len(xSink) != 0:
    plt.scatter(xSink, ySink, label= "Sinkers", c= "pink", marker= ".")
  if len(xTsea) != 0:
    plt.scatter(xTsea, yTsea, label= "TwoSeams", c= "brown", marker= ".")
  #fig, ax = plt.subplots()   
  plt.xlabel('Release Side (ft)')

  plt.ylabel('Release Height (ft)')

  #ax.add_patch(Rectangle((1, 1), -1, 1, edgecolor = 'blue', facecolor = 'blue', fill=False, lw=5))
  plt.title(str(Player.name) + "\'s Pitch Release")
  plt.xlim(-4, 4)
  plt.ylim(0, 7)
  plt.legend(fontsize = "8")
  plt.show()
  plt.savefig((str(Player.name) + 'Release.png'))
  plt.clf()

def createHTML():
  f = open('BucknellBaseballPitcherData.html', 'w')

  html_template = "<html> \n<head> \n<title>Bucknell Baseball Data Sheet</title>"
  for players in pitchers:
    html_template1 = str(html_template) + "<body> \n<p>" + str(formatHTML(writePitcherData(players))) + "</p> \n<img src=\"" + str(players.name) + "Pitches.png\" alt=\"PNG Image\"> \n<img src=\"" + str(players.name) + "Movement.png\" alt=\"PNG Image\">\n<img src=\"" + str(players.name) + "Spin.png\" alt=\"PNG Image\">\n<img src=\"" + str(players.name) + "Release.png\" alt=\"PNG Image\">\n</body>"
    html_template = html_template1
  html_template1 = html_template + "\n</html>"
  f.write(html_template1)   
  f.close()

def createPortal(beginDate, endDate):
  createHTML()
  for players in pitchers:
    pltPitches(players)
    pltMovement(players)
    pltSpin(players)
    pltRelease(players)
    writePitcherData(players)

createPortal(10, 10)

"""for batter in hitters:
  writeHitterData(batter)
  print(batter.name)
  print(batter.swingMissFast())
  print(batter.avgLA())"""
