#Repository Owner = ABleasdale1
#Last Updated = 10/02/2023 11:00
#####################################
import sys
import os
import time
import random
from characters import Enemies, Hero
#####################################
loki = Enemies("Loki", "1500", "You will never be a god.", "90","50", "150")
freya = Enemies("Freya", "1750", "Desires are what can most easily ruin us, lovely.", "75","100", "200")
hel = Enemies("Hel", "10000", "I am become death, the destroyer of worlds.", "5","1000", "350")
#####################################
#odin = Hero("Odin", "500", "You have forgotten … And you will forget still more!", "6","100", "250")
#thor = Hero("Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "6","50", "200")
#####################################
os.system('cls')
#####################################
heroes = [["Odin", "500", "You have forgotten … And you will forget still more!", "30","100", "250"],
["Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "65","50", "200"]]
hero = None
#####################################
menu()
#####################################
for record in heroes:
    print("Name =", record[0])
    print("Health =", record[1])
    print("Dodge =", record[3])
    print("Minimum Damage =", record[4])
    print("Maximum Damage =", record[5], "\n")

def Start():
    global hero
    while True:
        print ("Choose a Hero\n1.Odin\n2.Thor")
        choice = int(input())
        if choice == 1:
            hero = Hero("Odin", "500", "You have forgotten … And you will forget still more!", "6","100", "250")
            break
        elif choice == 2:
            hero = Hero("Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "6","50", "200")
            break
        else:
            print("Invalid input") 

def menu():
    print("Hello and welcome to ABleasdale1's Game\n\n")
    print("Please choose an option\n1.Start Game\n2. View Instructions\n3. Exit")
    choice = int(input())
    if choice == 1:
        os.system('cls')
        Start()
    elif choice == 2:
        print ("Instructions")
    elif choice == 3:
        sys.exit()
    else:
        print ("Not a valid Input try again")
