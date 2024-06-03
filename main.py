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
wilson_progress = 0
corpse_discovery = 0



"""File Setups"""
mapfile = 'map.txt'
person = 'person.txt'
movementui = 'movementui.txt'
mainui = 'mainui.txt'

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

def tutorial():
  #DRAFT TEXT, FEEL FREE TO CHANGE ANYTHING, THIS IS ALL RUBBISH
  global wilson_progress
  with open(person) as file:
    print(file.read())
  if wilson_progress == 0:
    input("'God youre so ugly!'")
    input("'Why does your skin look transparent, jesus christ'")
    tutorial1 = input("It's a medical condition [1]  What skin? [2]: ")
    if tutorial1 == "1":
      print("")
      print("> It's a medical conditon")
      print("")
      input("'Whatever it is, do NOT touch me'")
    elif tutorial1 == "2":
      print("")
      print("> What skin?")
      print("")
      input("'Stand away from me you sick FREAK!'")
    else:
      print("")
      print("*You try to spit out any type of words, that can communicate your condition,")
      print("however this was a challenging feat. Your tounge boils with a longing to ")
      input("say anything, absolutely anything: ")
      print("")
      print(">gurrrrjirrr")
      print("")
      input("'I assume thats freak for 'I am ready to do my god damn job'")
      print("")
    input("'Look...'")
    input("'Your job is to go around and interact with every single thing that moves'")
    print("'But before you start barging into other peoples rooms, I need you to")
    input(" inspect the body first, and go to room 119 to meet the suspects'")
    print("")
    #ROUGH IDEAS
    input("Also..")
    input("A reminder that your firm is owned by Jax Co...: ")
    input("I could care less about who actually did it: ")
    input("Just make sure the person you arrest SEEM evil: ")
    print("GOT IT?")
    print("")
    print("No [1]")
    print("Yes [2]")
    input("-CHOICE: ")
    input("I don't care what a Jax lackie says to me: ")
    input("GET GOING: ")
    wilson_progress += 1
  elif wilson_progress == 1:
    input("WHY ARE YOU TALKING TO ME?! DO YOUR JOB LACKIE!: ")

def corpseinter():
  #DRAFT TEXT, FEEL FREE TO CHANGE ANYTHING, THIS IS ALL RUBBISH
  global corpse_discovery
  if corpse_discovery == 0:
    input("*The corpse curls in a ball, fitted with a restful stare")
    input("*Immediately you notice a pool of blood beneath the body")
    print("")
    print("*A man with a whisky beard stumbles towards you")
    input("*His eyes darts around the room execept for you or the corpse")
    print("")
    input("'Can I help you sir?'")
    print("")
    print("Ignore and Examine the Body [1]") 
    print("Ask for an Improv Autopsy [2]")
    corpsequest = input("CHOICE: ")
    if corpsequest == "1":
      input("*You look over the body and see a bloodied gash on the victims chest")
      input("*The wounds are smaller than any type of knife that can stab")
      print("")
      input("...'sir?'")
      print("")
      input("*a pike or some type of spear COULD do this, but thats highly illogical")
      print("")
      input("'Sir.'")
      print("")
      input("*We should use our energy looking for anytype of firearm located- ")
      print("")
      input("'SIR!'")
      print("")
      print("What? [1]") 
      print("WHAT! WHAT THE HELL DO YOU WANT, SHITLIPS!?  [2]")
      corpsequestA1 = input("CHOICE: ")
      if corpsequestA1 == "1":
        print("")
        print("> What?")
        print("")
        input("'Here's the Improv Autopsy'")
        print("")
        input("> Thank you")
      elif corpsequestA1 == "2":
        print("")
        print("> WHAT! WHAT THE HELL DO YOU WANT, SHITLIPS!?")
        print("")
        input("'...n-nothing sir'")
        input("'*The officer rips up a piece of paper'")
      else:
        print("")
        input("> ...")
        print("")
        input("'...Here's the uhh... Autopsy...sir'")
        input("...")
    elif corpsequest == "2":
      print("jiej")
    corpse_discovery += 1

def movementbarrier():
  global y_loc
  if corpse_discovery == 0:
    if y_loc == 0:
      y_loc +=1
      print("[YOU NEED TO INSPECT THE BODY FIRST]")
    elif y_loc == 2:
      y_loc -=1
      print("[YOU NEED TO INSPECT THE BODY FIRST]")
  
### ALTERANTIVE MAP/MOVEMENT DESIGN, instead of WASD just ask where the user wants to go
  
  

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
  if direction == "1":  #This will ask directly where the user wants to go.
    while True:
      with open(movementui) as file:
        print(file.read())
      directionquest = input("Where do you want to go to?: ")
      if directionquest == "1":
        x_loc = 0
        y_loc = 0
        break
      elif directionquest == "2":
        x_loc = 1
        y_loc = 0
        break
      elif directionquest == "3":
        x_loc = 0
        y_loc = 1
        break
      elif directionquest == "4":
        x_loc = 1
        y_loc = 1
        break
      elif directionquest == "5":
        x_loc = 0
        y_loc = 2
        break
      elif directionquest == "6":
        x_loc = 1
        y_loc = 2
        break
      else:
        pass
      
  elif direction == "2":
    if x_loc == 0 and y_loc == 1:
      tutorial()
    elif x_loc == 1 and y_loc == 1:
      corpseinter()

while True:
  with open(mainui) as file:
    print(file.read())
  roomdesc()
  #DEV TOOL
  print("COORDINATES: ",f"{x_loc}, {y_loc}")
  direction = input("CHOICE: ")
  movement(direction)


#heheh