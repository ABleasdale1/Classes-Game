#Repository Owner = ABleasdale1
#Last Updated = 20/02/2023
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
    def __init__(self, name, desc, damadd, cost):
        self.name = name
        self.desc = desc
        self.damadd = damadd
        self.cost = cost        
#####################################