from pitch import Pitch

class Pitcher:
    def __init__(self, name, handedness):
        self.name = name
        self.handedness = handedness
        self.pitches = []

    def insertPitch(self, pitchInstance):
        self.pitches.append(pitchInstance)

    def __str__(self):
        return self.name

    def avgFastball(self):
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        for pitch in self.pitches:
            if pitch.ptype == "Fastball":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.outcome == "StrikeCalled":
                    totStrike += 1
        if (numPitches > 0): 
            return("Fastballs Thrown: " + str(numPitches) + "\n" + "Average Fastball Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Fastball Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Fastball Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgChangeup(self):
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        for pitch in self.pitches:
            if pitch.ptype == "ChangeUp":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.outcome == "StrikeCalled":
                    totStrike += 1
        if (numPitches > 0): 
            return("Changeups Thrown: " + str(numPitches) + "\n" + "Average Changeup Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Changeup Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Changeup Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgCurveball(self):
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        for pitch in self.pitches:
            if pitch.ptype == "Curveball":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.outcome == "StrikeCalled":
                    totStrike += 1
        if (numPitches > 0): 
            return("Curveballs Thrown: " + str(numPitches) + "\n" + "Average Curveball Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Curveball Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Curveball Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgSlider(self):
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        for pitch in self.pitches:
            if pitch.ptype == "Slider":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.outcome == "StrikeCalled":
                    totStrike += 1
        if (numPitches > 0): 
            return("Sliders Thrown: " + str(numPitches) + "\n" + "Average Slider Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Slider Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Slider Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgSplitter(self):
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        for pitch in self.pitches:
            if pitch.ptype == "Splitter":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.outcome == "StrikeCalled":
                    totStrike += 1
        if (numPitches > 0): 
            return("Splitters Thrown: " + str(numPitches) + "\n" + "Average Splitter Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Splitter Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Splitter Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgCutter(self):
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        for pitch in self.pitches:
            if pitch.ptype == "Cutter":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.outcome == "StrikeCalled":
                    totStrike += 1
        if (numPitches > 0): 
            return("Cutters Thrown: " + str(numPitches) + "\n" + "Average Cutter Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Cutter Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Cutter Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgSinker(self):
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        for pitch in self.pitches:
            if pitch.ptype == "Sinker":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.outcome == "StrikeCalled":
                    totStrike += 1
        if (numPitches > 0): 
            return("Sinkers Thrown: " + str(numPitches) + "\n" + "Average Sinker Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Sinker Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Sinker Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""
        
    def avgTwoSeam(self):
        numPitches = 0
        totVelo = 0
        totSpin = 0
        totStrike = 0
        for pitch in self.pitches:
            if pitch.ptype == "TwoSeamFastBall":
                numPitches += 1
                totVelo += float(pitch.velocity)
                totSpin += float(pitch.spin)
                if pitch.outcome == "StrikeCalled":
                    totStrike += 1
        if (numPitches > 0): 
            return("TwoSeams Thrown: " + str(numPitches) + "\n" + "Average TwoSeam Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average TwoSeam Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Fastball TwoSeam Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")
        else:
            return ""