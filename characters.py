#Repository Owner = ABleasdale1
#####################################
class Enemies(object):
    def __init__(self, name, health, dodge, speech, minDam, maxDam): 
        self.name = name
        self.health = health
        self.speech = speech
        self.dodge = dodge
        self.minDam = minDam
        self.maxDam = maxDam

    def nameCPU(self):
        print(self.name)

    def healthRemCPU(self):
        print(self.health)

    def speechCPU(self):
        print(self.speech)   
#####################################
class Hero(object):
    def __init__(self, name, health, dodge, speech, minDam, maxDam): 
        self.name = name
        self.health = health
        self.speech = speech
        self.dodge = dodge
        self.minDam = minDam
        self.maxDam = maxDam

    def nameUser(self):
        print(self.name)

    def healthRemUser(self):
        print(self.health)

    def speechUser(self):
        print(self.speech)
#####################################
class Item(object):
    def __init__(self, name, desc, damadd, cost):
        self.name = name
        self.desc = desc
        self.damadd = damadd
        self.cost = cost        

    def itemName(self):
        print(self.name)

    def description(self):
        print(self.desc)

    def itemCost(self):
        print(self.cost)
#####################################