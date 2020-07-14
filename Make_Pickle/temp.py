class Athlete:
    def __init__(self, value='Jane'):
        self.thing = value
    def getAthlete(self):
        return self.thing

a = Athlete()
a.getAthlete()
print(a.getAthlete())
b = Athlete('Holy')
b.getAthlete()
print(b.getAthlete())

Athlete.__init__(a)
Athlete.__init__(b,'Boly')
print(b.getAthlete())