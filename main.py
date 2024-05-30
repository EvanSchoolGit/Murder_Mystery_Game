#CHECKLIST
#Map and Movement System (easy)
#Room Interaction (medium easy)
#Nuanced Character Interaction Dependant on progress of game (HARDEST) 
#Item Interactions (Hard)
#Intro
#Multiple Endings
#######################################################################
# Title : Murder Mystery
# Class : Computer Science 30
# Assighnment : make a murder mystery text game
# Coder : Evan Urban and Tibby Schell
# Version : 1
########################################################################
""" 
Fill me out!!!!!
"""
###########################-IMPORTS-############################################

############################-SETUP-#############################################
"""Location Values"""
x_loc=0
y_loc=1

"Progress Keys"
corpse_discovery = 0



"""File Setups"""
mapfile = 'map.txt'

rooms = {
  "Room 118": {
    "name" : "ROOM: Room 118",
    "description" : ""'Oliver lives here'""},

  "Room 119": {
    "name" : "ROOM: Room 119",
    "description" : """INSERT BLURB """},

  "Room 120": {
    "name" : "ROOM: Room 120",
    "description" : """Lucas and Lisa used to live here"""},

  "Room 121": {
    "name" : "ROOM: Room 121",
    "description" : "Vixen lives here"},

  "Hallway": {
    "name" : "ROOM: Hallway",
    "description" : "The corpse is placed here"}

}



def intro():
  input("")
  

def roomdesc():
  if x_loc == 0 and y_loc == 0:
    print (rooms["Room 119"]["name"])
    print("")
    print (rooms["Room 119"]["description"])
  elif x_loc == 1 and y_loc == 0:
    print (rooms["Room 121"]["name"])
    print("")
    print (rooms["Room 121"]["description"])
  elif x_loc == 0 and y_loc == 2:
    print (rooms["Room 118"]["name"])
    print("")
    print (rooms["Room 118"]["description"])
  elif x_loc == 1 and y_loc == 2:
    print (rooms["Room 120"]["name"])
    print("")
    print (rooms["Room 120"]["description"])
  elif x_loc == 1 and y_loc == 1:
    print (rooms["Hallway"]["name"])
    print("")
    print (rooms["Hallway"]["description"])
  elif x_loc == 0 and y_loc == 1 and corpse_discovery == 0:
    print (rooms["Hallway"]["name"])
    print("")
    print ("[PRESS Q] ... What do I need to again?")
  
"""Simple Movements"""
def movement(direction): 
  global x_loc, y_loc
  if direction == "a" or "A": #Classic WASD Controls
    x_loc-= 1
  elif direction == "d" or "D":
    x_loc+= 1
  elif direction == "w" or "W":
    y_loc-= 1
  elif direction == "s" or "S":
    y_loc+= 1
  elif direction == "q" or "Q":
    if x_loc =

while True:
  with open(mapfile) as file:
    print(file.read())
  roomdesc()
  print("COORDINATES: ",f"{x_loc}, {y_loc}")
  direction = input("CHOICE: ")
  movement(direction)


#heheh