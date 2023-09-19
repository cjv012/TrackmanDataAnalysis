from hit import Hit
import matplotlib.pyplot as plt

class Hitter:
    """Class to store pitcher objects"""
    def __init__(self, name, handedness):
        """Class constructor for the pitcher object creates the name handness and an array to store every pitch as a pitch object"""
        self.name = name
        self.handedness = handedness
        self.hits = []

    def insertHit(self, pitchInstance):
        """Method to add new pitch objects to the pitcher array"""
        self.hits.append(pitchInstance)

    def __str__(self):
        """String method to return the pitchers name"""
        return self.name

    def avgLA(self):
        pass

    def avgEV(self):
        pass

    def overHundred(self):
        pass

    def overNinety(self):
        pass
    
    def overEighty(self):
        pass

    def underEighty(self):
        pass

    def chaseRate(self):
        pass

    def swingInZone(self):
        pass

    def swingMissFast(self):
        pass

    def swingMiss(self):
        pass

