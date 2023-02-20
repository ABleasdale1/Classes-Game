#Repository Owner = ABleasdale1
#Last Updated = 20/02/2023
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
basicHammer = Item("Loki", "This item grants an extra 50 attack damage", "50", 75)
advancedHammer = Item("Loki", "This item grants an extra " "100")
bobsnuke = Item("Bob's Nuke", "500")
tacticalNuke = Item("Tactical Nuke", "10000")
#####################################
#odin = Hero("Odin", "500", "You have forgotten … And you will forget still more!", "6","100", "250")
#thor = Hero("Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "6","50", "200")
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
fctMenu5 = "You have 2 options.\n1. Attempt to comunicate with the God\n2. Fight"
#####################################
def store():
    print ("Welcome to the store\nYou have", gold,)
    while True:
        print ("Items are")


def path1():
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
                else:
                    print ("You were unsucsseful. Now you must fight.")
        elif choice == 2:
            print ("You chose to fight")
        else:
            print ("Invalid Input")

def path2():
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
                else:
                    print ("You were unsucsseful. Now you must fight.")
        elif choice == 2:
            print ("You chose to fight")
        else:
            print ("Invalid Input")
    
def path3():
    print("You continue down the path cautiosly when suddenly")
    for char in dot:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.2)
    print ("A flying Freya drops from the sky blocking your path.")
    while True:    
        print (fctMenu5)
        choice = int(input())
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
                else:
                    print ("You were unsucsseful. Now you must fight.")
        elif choice == 2 :
            print ("You chose to fight")
        else:
            print ("Invalid Input")

def Start():
    global hero
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
            hero = Hero("Odin", "500", "You have forgotten … And you will forget still more!", "6","100", "250")
            break
        elif choice == 2:
            hero = Hero("Thor", "750", "I make grave mistakes all the time. Everything seems to work out.", "6","50", "200")
            break
        else:
            print("Invalid input")
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

def menu():
    global my_bool
    print("Hello and welcome to ABleasdale1's Game\n\n")
    while my_bool == True:
        print("Please choose an option\n1. Start Game\n2. View Instructions\n3. Exit")
        choice = int(input())
        if choice == 1:
            os.system('cls')
            Start()
            my_bool = False
        elif choice == 2:
            print ("Instructions")
        elif choice == 3:
            sys.exit()
        else:
            print ("Not a valid Input try again")

#####################################
menu()
