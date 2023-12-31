class Pitch: 
    """Class to store pitch objects and the various metrics atrributable to each pitch"""
    def __init__(self, date, ptype, velocity, outcome, spin, vbreak, hbreak, degrees, axis, rheight, rside, extension, plheight, plside):
        """Constructor for each pitch type: Takes in the data and stores it to the pitch"""
        self.date = date
        self.ptype = ptype
        self.velocity = velocity
        self.outcome = outcome
        self.spin = spin
        self.vbreak = vbreak
        self.hbreak = hbreak
        self.degrees = degrees
        self.axis = axis.replace(":", ".")
        self.rheight = rheight
        self.rside = rside
        self.extension = extension
        self.plheight = plheight
        self.plside = plside
    
    def __str__(self):
        """String method that sprints about the data of the pitch and the various attributes of it"""
        return "Date: " + self.date + "\nPitch Type: " + self.ptype + "\nPitch Velocity: " + self.velocity + "\nStrike/Ball: " + self.outcome + "\nSpin Rate: " + self.spin + "\nInduced Vertical Break: " + self.vbreak + "\nHorizontal Break: " + self.hbreak + "\nTilt: " + self.axis + "\nRelease Height: " + self.rheight + "\nRelease Side: " + self.rside + "\nExtension: " + self.extension + "\nPlate Height: " + self.plheight + "\nPlate Side: " + self.plside + "\n"