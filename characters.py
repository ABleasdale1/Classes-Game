#Repository Owner = ABleasdale1
#Last Updated = 10/02/2023
#####################################
class Enemies(object):
    def __init__(self, name, health, dodge, speech, minDam, maxDam): 
        self.name = name
        self.health = health
        self.speech = speech
        self.dodge = dodge
        self.minDam = minDam
        self.maxDam = maxDam

    def get_name(self):
        return self.name    
#####################################
class Hero(object):
    def __init__(self, name, health, dodge, speech, minDam, maxDam): 
        self.name = name
        self.health = health
        self.speech = speech
        self.dodge = dodge
        self.minDam = minDam
        self.maxDam = maxDam        
#####################################
class Item(object):
    def __init__(self, name, damadd):
        self.name = name
        self.name = damadd
#####################################