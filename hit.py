class Hit: 
    """Class to store pitch objects and the various metrics atrributable to each pitch"""
    def __init__(self, date, angle, eVelo, outcome, pType, distance):
        """Constructor for each pitch type: Takes in the data and stores it to the pitch"""
        self.date = date
        self.angle = angle
        self.pType = pType
        self.eVelocity = eVelo
        self.outcome = outcome
        self.distance = distance
        
    def __str__(self):
        """String method that sprints about the data of the pitch and the various attributes of it"""
        return "Date: " + self.date + "\nLaunch Angle: " + self.angle + "\nPitch Type: " + self.pType + "\nExit Velocity: " + self.eVelocity + "\nOutcome: " + self.outcome + "\nDistance: " + self.distance + "\n"