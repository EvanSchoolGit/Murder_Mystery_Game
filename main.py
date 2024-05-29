#CHECKLIST
#Map and Movement System (easy)
#Room Interaction (medium easy)
#Nuanced Character Interaction Dependant on progress of game (HARDEST) 
#Item Interactions (Hard)
#Intro
#Multiple Endings
########################################################################
# Title : Murder Mystery
# Class : Computer Science 30
# Assighnment : make a murder mystery text game
# Coder : Evan Urban
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
  print("COORDINATES: ",f"{x_loc}, {y_loc}")
  direction = input("CHOICE: ")
  movement(direction)


