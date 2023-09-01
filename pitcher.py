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
        return("Fastballs Thrown: " + str(numPitches) + "\n" + "Average Fastball Velocity: " + str(round((totVelo/numPitches), 1)) + "\n" + "Average Fastball Spin Rate: " + str(round((totSpin/numPitches), 1)) + "\n" + "Fastball Strike Percentage: " + str(round(((totStrike/numPitches) * 100), 1)) + "%")

    def avgChangeup(self):
        pass

    def avgCurveball(self):
        pass

    def avgSlider(self):
        pass

    def avgSplitter(self):
        pass

    def avgCutter(self):
        pass

    def avgSinker(self):
        pass

    def avgTwoSeam(self):
        pass