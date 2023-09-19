from hit import Hit
import matplotlib.pyplot as plt

class Hitter:
    """Class to store pitcher objects"""
    def __init__(self, name, handedness):
        """Class constructor for the pitcher object creates the name handness and an array to store every pitch as a pitch object"""
        self.name = name
        self.handedness = handedness
        self.swingAndMiss = 0
        self.swingFast = 0
        self.hits = []

    def swingingMiss(self):
        self.swingAndMiss += 1

    def missFast(self):
        self.swingFast += 1

    def insertHit(self, pitchInstance):
        """Method to add new pitch objects to the pitcher array"""
        self.hits.append(pitchInstance)

    def __str__(self):
        """String method to return the pitchers name"""
        return self.name

    def avgLA(self):
        averageLA = 0
        totalHits = len(self.hits)
        for hits in self.hits:
            if hits.angle != '':
                averageLA += float(hits.angle)
            else:
                totalHits -= 1
        return round((averageLA/totalHits), 2)


    def avgEV(self):
        averageEV = 0
        totalHits = len(self.hits)
        for hits in self.hits:
            if hits.eVelocity != '':
                averageEV += float(hits.eVelocity)
            else:
                totalHits -= 1
        return round((averageEV/totalHits), 2)

    def overHundred(self):
        totHundy = 0
        for hits in self.hits:
            if float(hits.eVelocity) >= 100:
                totHundy += 1
        return totHundy

    def overNinety(self):
        totHundy = 0
        for hits in self.hits:
            if float(hits.eVelocity) >= 90:
                totHundy += 1
        return totHundy
    
    def overEighty(self):
        totHundy = 0
        for hits in self.hits:
            if float(hits.eVelocity) >= 80:
                totHundy += 1
        return totHundy

    def underEighty(self):
        totHundy = 0
        for hits in self.hits:
            if float(hits.eVelocity) < 80:
                totHundy += 1
        return totHundy

    def chaseRate(self):
        pass

    def swingInZone(self):
        pass

    def swingMissFast(self):
        missFast = self.swingFast
        totFast = self.swingFast
        for hit in self.hits:
            if hit.pType:
                totFast += 1
        return round((missFast/totFast), 2)

    def swingMiss(self):
        swingMiss = self.swingAndMiss
        totSwing = len(self.hits) + swingMiss
        return round((swingMiss/totSwing), 2)
        

