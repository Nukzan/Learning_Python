# CLASS PARAMETER CAN HAVE LIST FACTOR
class Athlete:
    def __init__(self, athlete_name, athlete_dob=None, athlete_times=[]):
        self.name = athlete_name
        self.dob = athlete_dob
        self.times = athlete_times