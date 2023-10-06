from pitch import Pitch
import matplotlib.pyplot as plt

class Pitcher:
    """Class to store pitcher objects"""
    def __init__(self, name, handedness):
        """Class constructor for the pitcher object creates the name handness and an array to store every pitch as a pitch object"""
        self.name = name
        self.handedness = handedness
        self.pitches = []

    def insertPitch(self, pitchInstance):
        """Method to add new pitch objects to the pitcher array"""
        self.pitches.append(pitchInstance)

    def __str__(self):
        """String method to return the pitchers name"""
        return self.name
    
    def totStrike(self):
        totStrike = 0
        totPitches = len(self.pitches)
        for pitch in self.pitches:
            if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                totStrike += 1
            if pitch.outcome == "Undefined":
                totPitches -= 1
        return ("Total Strike Percentage: " + str(round(((totStrike/totPitches)*100), 2)) + "%");

    def avgFastball(self):
        """Calculates the pitchers average Fastball metrics and prints them"""
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        totVBreak = 0
        totHBreak = 0
        maxFast = 0
        strikePitches = 0
        for pitch in self.pitches:
            if (pitch.ptype == "Fastball" or pitch.ptype == "FourSeamFastBall"):
                if pitch.velocity == "" and numPitches > 0:
                    totVelo += float(totVelo)/numPitches
                    totSpin += float(totSpin)/numPitches
                    totHBreak += float(totHBreak)/numPitches
                    totVBreak += float(totVBreak)/numPitches
                elif numPitches == 0:
                    pass
                else:
                    if float(pitch.velocity) > maxFast:
                        maxFast = float(pitch.velocity)
                    numPitches += 1
                    strikePitches += 1
                    totVelo += float(pitch.velocity)
                    totSpin += float(pitch.spin)
                    if pitch.vbreak == "" or pitch.hbreak == "":
                        totHBreak += float(totHBreak)/numPitches
                        totVBreak += float(totVBreak)/numPitches
                    else:
                        totVBreak += float(pitch.vbreak)
                        totHBreak += float(pitch.hbreak)
                if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                    totStrike += 1
                if pitch.outcome == "Undefined":
                    strikePitches -= 1
        if (numPitches > 0): 
            return("Fastballs Thrown: " + str(numPitches) + "\n" + "Average Fastball Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Max Fastball Velocity: " + str(round((maxFast), 1)) + "\n" + "Average Fastball Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Average Fastball Vertical Break: " + str(round((totVBreak/numPitches), 1)) + "\n" + "Average Fastball Horizontal Break: " + str(round((totHBreak/numPitches), 1)) + "\n" "Fastball Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgChangeup(self):
        """Calculates the pitchers average Changeup metrics and prints them"""
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        totVBreak = 0
        totHBreak = 0
        strikePitches = 1
        for pitch in self.pitches:
            if pitch.ptype == "ChangeUp":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.vbreak == "" or pitch.hbreak == "":
                    totHBreak += float(totHBreak)/numPitches
                    totVBreak += float(totVBreak)/numPitches
                else:
                    totVBreak += float(pitch.vbreak)
                    totHBreak += float(pitch.hbreak)
                if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                    totStrike += 1
                if pitch.outcome == "Undefined":
                    strikePitches -= 1
        if (numPitches > 0): 
            return("Changeups Thrown: " + str(numPitches) + "\n" + "Average Changeup Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Changeup Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Average Changeup Vertical Break: " + str(round((totVBreak/numPitches), 1)) + "\n" + "Average Changeup Horizontal Break: " + str(round((totHBreak/numPitches), 1)) + "\n" "Changeup Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:  
            return ""
        
    def avgCurveball(self):
        """Calculates the pitchers average Curveball metrics and prints them"""
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        totVBreak = 0
        totHBreak = 0
        strikePitches = 1
        for pitch in self.pitches:
            if pitch.ptype == "Curveball":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.vbreak == "" or pitch.hbreak == "":
                    totHBreak += float(totHBreak)/numPitches
                    totVBreak += float(totVBreak)/numPitches
                else:
                    totVBreak += float(pitch.vbreak)
                    totHBreak += float(pitch.hbreak)
                if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                    totStrike += 1
                if pitch.outcome == "Undefined":
                    strikePitches -= 1
        if (numPitches > 0): 
            return("Cuverballs Thrown: " + str(numPitches) + "\n" + "Average Cuverball Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Cuverball Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Average Cuverball Vertical Break: " + str(round((totVBreak/numPitches), 1)) + "\n" + "Average Cuverball Horizontal Break: " + str(round((totHBreak/numPitches), 1)) + "\n" "Cuverball Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgSlider(self):
        """Calculates the pitchers average slider metrics and prints them"""
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        totVBreak = 0
        totHBreak = 0
        strikePitches = 1
        for pitch in self.pitches:
            if pitch.ptype == "Slider":
                numPitches += 1
                if pitch.velocity == "":
                    totVelo += float(totVelo)/numPitches
                    totSpin += float(totSpin)/numPitches
                else:
                    totVelo += float(pitch.velocity)
                    totSpin += float(pitch.spin)
                if pitch.vbreak == "" or pitch.hbreak == "":
                    totHBreak += float(totHBreak)/numPitches
                    totVBreak += float(totVBreak)/numPitches
                else:
                    totVBreak += float(pitch.vbreak)
                    totHBreak += float(pitch.hbreak)
                if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                    totStrike += 1
                if pitch.outcome == "Undefined":
                    strikePitches -= 1
        if (numPitches > 0): 
            return("Sliders Thrown: " + str(numPitches) + "\n" + "Average Slider Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Slider Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Average Slider Vertical Break: " + str(round((totVBreak/numPitches), 1)) + "\n" + "Average Slider Horizontal Break: " + str(round((totHBreak/numPitches), 1)) + "\n" "Slider Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgSplitter(self):
        """Calculates the pitchers average Splitter metrics and prints them"""
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        totVBreak = 0
        totHBreak = 0
        strikePitches = 1
        for pitch in self.pitches:
            if pitch.ptype == "Splitter":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.vbreak == "" or pitch.hbreak == "":
                    totHBreak += float(totHBreak)/numPitches
                    totVBreak += float(totVBreak)/numPitches
                else:
                    totVBreak += float(pitch.vbreak)
                    totHBreak += float(pitch.hbreak)
                if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                    totStrike += 1
                if pitch.outcome == "Undefined":
                    strikePitches -= 1
        if (numPitches > 0): 
            return("Splitters Thrown: " + str(numPitches) + "\n" + "Average Splitter Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Splitter Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Average Splitter Vertical Break: " + str(round((totVBreak/numPitches), 1)) + "\n" + "Average Splitter Horizontal Break: " + str(round((totHBreak/numPitches), 1)) + "\n" "Splitter Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgCutter(self):
        """Calculates the pitchers average Cutter metrics and prints them"""
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        totVBreak = 0
        totHBreak = 0
        strikePitches = 1
        for pitch in self.pitches:
            if pitch.ptype == "Cutter":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.vbreak == "" or pitch.hbreak == "":
                    totHBreak += float(totHBreak)/numPitches
                    totVBreak += float(totVBreak)/numPitches
                else:
                    totVBreak += float(pitch.vbreak)
                    totHBreak += float(pitch.hbreak)
                if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                    totStrike += 1
                if pitch.outcome == "Undefined":
                    strikePitches -= 1
        if (numPitches > 0): 
            return("Cutters Thrown: " + str(numPitches) + "\n" + "Average Cutter Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Cutter Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Average Cutter Vertical Break: " + str(round((totVBreak/numPitches), 1)) + "\n" + "Average Cutter Horizontal Break: " + str(round((totHBreak/numPitches), 1)) + "\n" "Cutter Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgSinker(self):
        """Calculates the pitchers average Sinker metrics and prints them"""
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        totVBreak = 0
        totHBreak = 0
        strikePitches = 1
        for pitch in self.pitches:
            if pitch.ptype == "Sinker":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.vbreak == "" or pitch.hbreak == "":
                    totHBreak += float(totHBreak)/numPitches
                    totVBreak += float(totVBreak)/numPitches
                else:
                    totVBreak += float(pitch.vbreak)
                    totHBreak += float(pitch.hbreak)
                if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                    totStrike += 1
                if pitch.outcome == "Undefined":
                    strikePitches -= 1
        if (numPitches > 0): 
            return("Sinkers Thrown: " + str(numPitches) + "\n" + "Average Sinker Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Sinker Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Average Sinker Vertical Break: " + str(round((totVBreak/numPitches), 1)) + "\n" + "Average Sinker Horizontal Break: " + str(round((totHBreak/numPitches), 1)) + "\n" "Sinker Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgTwoSeam(self):
        """Calculates the pitchers average TwoSeam metrics and prints them"""
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        totVBreak = 0
        totHBreak = 0
        strikePitches = 1
        for pitch in self.pitches:
            if pitch.ptype == "TwoSeamFastBall":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.vbreak == "" or pitch.hbreak == "":
                    totHBreak += float(totHBreak)/numPitches
                    totVBreak += float(totVBreak)/numPitches
                else:
                    totVBreak += float(pitch.vbreak)
                    totHBreak += float(pitch.hbreak)
                if pitch.outcome in ["StrikeCalled", "InPlay", "StrikeSwinging", "FoulBall"]:
                    totStrike += 1
                if pitch.outcome == "Undefined":
                    strikePitches -= 1
        if (numPitches > 0):
            return("TwoSeams Thrown: " + str(numPitches) + "\n" + "Average TwoSeam Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average TwoSeam Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Average TwoSeam Vertical Break: " + str(round((totVBreak/numPitches), 1)) + "\n" + "Average TwoSeam Horizontal Break: " + str(round((totHBreak/numPitches), 1)) + "\n" "TwoSeam Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
    