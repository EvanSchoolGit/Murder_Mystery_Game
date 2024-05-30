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
y_loc=0

"""File Setups"""
mapfile = 'map.txt'

rooms = {
  "First": {
    "name" : "ROOM: Strange Room",
    "description" : """'There is a scent of blood. Proceed with caution'"""},

  "Second": {
    "name" : "ROOM: Strange Room",
    "description" : """'There is a scent of sweat. Proceed with caution'"""},

  "Last": {
    "name" : "ROOM: Strange Room",
    "description" : """'There is a scent of tears. Proceed with caution'"""},

  "Gag": {
    "name" : "ROOM: The Dungeon",
    "description" : "'The Cobblestone flooring does not match with the office'"},

  "FINAL": {
    "name" : "ROOM: Final Stage",
    "description" : "'If I go past this area, I should be prepared...'"}

def intro():
  input("")
  

"""Simple Movements"""
def movement(direction): 
  global x_loc, y_loc
  if direction == "a": #Classic WASD Controls
    x_loc-= 1
  elif direction == "d":
    x_loc+= 1
  elif direction == "w":
    y_loc-= 1
  elif direction == "s":
    y_loc+= 1

while True:
  with open(mapfile) as file:
    print(file.read())
  print("COORDINATES: ",f"{x_loc}, {y_loc}")
  direction = input("CHOICE: ")
  movement(direction)


#heheh