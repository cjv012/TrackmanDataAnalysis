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