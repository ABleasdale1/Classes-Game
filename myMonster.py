#####################################
import sys
import os
import time
import random
from characters import Enemies, Hero
#####################################
loki = Enemies("Loki", "1500", "You will never be a god.", "6","50", "150")
freya = Enemies("Freya", "1750", "Desires are what can most easily ruin us, lovely.", "6","100", "200")
hel = Enemies("Hel", "10000", "I am become death, the destroyer of worlds.", "6","1000", "350")
#####################################
odin = Hero("Odin", "500", "You have forgotten … And you will forget still more!", "6","100", "250")
thor = Hero("Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "6","50", "200")
#####################################
os.system('cls')
#####################################
print(loki.get_name())