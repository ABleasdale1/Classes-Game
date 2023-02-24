#Repository Owner = ABleasdale1
#####################################
import sys
import os
import time
import random as rand
from characters import Enemies, Hero, Item
#####################################
loki = Enemies("Loki", "1500", "You will never be a god.", "90","50", "150")
freya = Enemies("Freya", "1750", "Desires are what can most easily ruin us, lovely.", "75","100", "200")
hel = Enemies("Hel", "10000", "I am become death, the destroyer of worlds.", "5","1000", "2350")
#####################################
basicHammer = Item("Basic Hammer", "This item grants an extra 50 attack damage", "50", "75 gold ")
advancedHammer = Item("Advanced Hammer", "This item grants an extra", "100", "250 gold")
bobsNuke = Item("Bob's Nuke","Bob is a dangerous man. Don't trust bob", "500", "500 gold")
tacticalNuke = Item("Tactical Nuke", "I mean its a tactical nuke what more can I say", "10000", "1000 gold")
#####################################
odin = Hero("Odin", "500", "You have forgotten … And you will forget still more!", "6","100", "250")
thor = Hero("Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "6","50", "200")
#####################################
os.system('cls')
#####################################
heroes = [["Odin", "500", "You have forgotten … And you will forget still more!", "30","100", "250"],
["Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "65","50", "200"]]
hero = None
my_bool = True
dot = '.....\n'
gold = 50
level = 1
fctMenu5 = "You have 2 options.\n1. Attempt to comunicate with the God\n2. Fight the God\n3. Run Away"
#####################################
def store():
    global gold
    os.system('cls')
    print ("Welcome to the store\nYou have", gold, "Gold")
    print ("Items are")
    print (basicHammer.itemName(), basicHammer.description(), basicHammer.itemCost())
    print (advancedHammer.itemName(), advancedHammer.description(), advancedHammer.itemCost())
    print (bobsNuke.itemName(), bobsNuke.description(), bobsNuke.itemCost())
    print (tacticalNuke.itemName(), tacticalNuke.description(), tacticalNuke.itemCost())

heroChoice = 'Odin'

def lokiFight():
    if heroChoice == 'Odin':
        print(loki.nameCPU())
        print(loki.healthRemCPU())
        print(odin.nameUser())
        print(odin.healthRemUser())
    elif heroChoice == 'Thor':
        print(loki.nameCPU())
        print(loki.healthRemCPU())
        print(thor.nameUser())
        print(thor.healthUser())
    else:
        print ("Its all gone wrong")

def helFight():
    print ("INCOMPLETE")

def freyaFight():
    print ("INCOMPLETE")

def path1():
    global dot
    global gold
    print("You continue down the path cautiosly when suddenly")
    for char in dot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.2)
    print ("Loki appears from a snake and blocks your path.")
    while True:    
        print (fctMenu5)
        choice = int(input())
        if choice == 1:
            print ("You attempt to communicate with the God")
            sucess = rand.randint(1, 2)
            for char in dot:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.2)
            if sucess == 1:
                print ("You are sucessful. The God gives you 25 gold")
                gold = gold + 25
                print ("Transitioning you to the store")
                store()
            else:
                print ("You were unsucsseful. Now you must fight.")
                lokiFight()
        elif choice == 2:
            print ("You chose to fight")
            lokiFight()
        elif choice == 3:
            break
        else:
            print ("Invalid Input")

def path2():
    global dot
    global gold
    print("You continue down the path cautiosly when suddenly")
    for char in dot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.2)
    print ("An angry Hel Rises from a fiery pit blocking your path.")
    while True:    
        print (fctMenu5)
        choice = int(input())
        if choice == 1:
            print ("You attempt to communicate with the God")
            sucess = rand.randint(1, 15)
            for char in dot:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.2)
            if sucess == 1:
                print ("You are sucessful. The God gives you 25 gold")
                gold = gold + 150
                print ("Do you wish to view the store? (Y/N)")
                choice2 = input()
                if choice2 == 'y' or choice2 == 'Y':
                    store()
            else:
                print ("You were unsucsseful. Now you must fight.")
        elif choice == 2:
            print ("You chose to fight")
        elif choice == 3:
            break
        else:
            print ("Invalid Input")
    
def path3():
    global dot
    global gold
    print("You continue down the path cautiosly when suddenly")
    for char in dot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.2)
    print ("A flying Freya drops from the sky blocking your path.")
    while True:    
        print (fctMenu5)
        choice = 2
        if choice == 1:
            print ("You attempt to communicate with the God")
            sucess = rand.randint(1, 5)
            for char in dot:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(.2)
            if sucess == 1 :
                print ("You are sucessful. The God gives you 25 gold")
                gold = gold + 50
                print ("Do you wish to view the store? (Y/N)")
                choice2 = input()
                if choice2 == 'y' or choice2 == 'Y':
                    store()
            else:
                print ("You were unsucsseful. Now you must fight.")
        elif choice == 2 :
            print ("You chose to fight")
        elif choice == 3:
            break
        else:
            print ("Invalid Input")

def forestWalks():
    while True:
        os.system('cls')
        print ("You are walking through a forest when you come across a fork in the path. You do not know what lays ahead.\nWhich path will you take? 1/2/3 ([4] to exit)")
        choice2 = int(input())
        if choice2 == 1:
            path1()
        elif choice2 == 2:
            path2()
        elif choice2 == 3:
            path3()
        elif choice2 == 4:
            sys.exit()
        else:
            print("Invalid input")

def Start():
    global hero
    global heroChoice
    while True:
        for record in heroes:
            print("Name =", record[0])
            print("Health =", record[1])
            print("Dodge =", record[3])
            print("Minimum Damage =", record[4])
            print("Maximum Damage =", record[5], "\n")
        print ("Choose a Hero\n1.Odin\n2.Thor")
        choice = int(input())
        if choice == 1:
            heroChoice = 'Odin'
            hero = Hero("Odin", "500", "You have forgotten … And you will forget still more!", "6","100", "250")
            forestWalks()
        elif choice == 2:
            heroChoice = 'Thor'
            hero = Hero("Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "6","50", "200")
            forestWalks()
        else:
            print("Invalid input")

def menu():
    global my_bool
    print("Hello and welcome to ABleasdale1's Game\n\n")
    while my_bool == True:
        print("Please choose an option\n1. Start Game\n2. View Instructions\n3. Exit")
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

#####################################
#menu()