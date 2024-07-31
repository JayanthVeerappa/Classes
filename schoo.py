class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def getNumberOfStudents(self):
        return self.numberOfStudents

    def setNumberOfStudents(self, newNumberOfStudents):
        self.numberOfStudents = newNumberOfStudents

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def getPickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + f". The pickup policy is {self.pickupPolicy}"

class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams

    def getSportsTeams(self):
        return self.sportsTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + f". The sports teams are {', '.join(self.sportsTeams)}"


a = School("Codecademy", "high", 100)
print(a.getName())  
print(a.getLevel())  
print(a.getNumberOfStudents())  
a.setNumberOfStudents(200)
print(a.getNumberOfStudents())  
print(a)  

b = PrimarySchool("Codecademy Primary", 300, "Pickup after 3pm")
print(b.getPickupPolicy())  
print(b)  

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams()) 
print(c)
