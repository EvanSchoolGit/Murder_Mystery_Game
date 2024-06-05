import random

from items import autopsy, bullet_casing, lucas_gun, rent_bill, safe_keycard, vixen_gun


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

"Child Class Setups"


"""File Setups"""
mapfile = 'map.txt'
person = 'person.txt'
movementui = 'movementui.txt'
mainui = 'mainui.txt'
autopsyfile = 'autopsy.txt'

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
    input("'God, you're so ugly!'")
    input("'Why does your skin look transparent, Jesus Christ!'")
    print("[1] It's a medical condition.")
    print("[2] What skin?")
    tutorial1 = input("CHOICE: ")
    if tutorial1 == "1":
      print("")
      print("> It's a medical conditon.")
      print("")
      input("'Whatever it is, do NOT touch me.'")
    elif tutorial1 == "2":
      print("")
      print("> What skin?")
      print("")
      input("'Stand away from me, you sick FREAK!'")
    else:
      print("")
      print("*You try to spit out any type of words to communicate your condition,")
      print("however this was a challenging feat. Your tongue boils with a longing to ")
      input("say anything, absolutely anything: ")
      print("")
      print(">Gurrrrjirrr")
      print("")
      input("'...I assume thats freak for 'I am ready to do my god damn job!'")
      print("")
    input("'Look...'")
    input("'Your job is to go around and interact with every single thing that moves.'")
    print("'But before you start barging into other peoples rooms, I need you to")
    input(" inspect the body first, and go to room 119 to meet the suspects'")
    print("")
    #ROUGH IDEAS
    input("Also..")
    input("A reminder that your firm is owned by Jax Co...: ")
    input("I could care less about who actually did it: ")
    input("Just make sure the person you arrest SEEMS evil: ")
    print("GOT IT?")
    print("")
    print("[1] No")
    print("[2] Yes")
    input("-CHOICE: ")
    input("I don't care what a Jax lackie says to me: ")
    input("GET GOING: ")
    wilson_progress += 1
  elif wilson_progress == 1:
    input("WHY ARE YOU TALKING TO ME?! DO YOUR JOB LACKIE!: ")

def corpseinter():
  #FIX FORMATTING
  global corpse_discovery
  if corpse_discovery == 0:
    input("*The corpse is curled in a ball, fitted with a restful stare.")
    input("*Immediately, you notice a pool of blood beneath the body.")
    print("")
    print("*A man with a whisky beard stumbles towards you.")
    input("*His eyes dart around the room, avoiding you or the corpse.")
    print("")
    input("'Can I help you sir?'")
    print("")
    print("[1] Ignore and Examine the Body") 
    print("[2] Ask for an Improv Autopsy")
    corpsequest = input("CHOICE: ")
    if corpsequest == "1":
      input("*You look over the body and see a bloodied gash on the victims chest.")
      input("*The wounds are too small to come from a knife.")
      print("")
      input("...'sir?'")
      print("")
      input("*A pike or some type of spear COULD do this, but thats highly illogical...")
      print("")
      input("'Sir.'")
      print("")
      input("*You notice within the small gash that-")
      print("")
      input("'SIR!'")
      print("")
      print("[1] What?") 
      print("[2] WHAT! WHAT THE HELL DO YOU WANT, SHITLIPS!?")
      corpsequesta1 = input("CHOICE: ")
      if corpsequesta1 == "1":
        print("")
        print("> What?")
        print("")
        input("'Here's the Improvised Autopsy.'")
        print("")
        input("> Thank you...")
      elif corpsequesta1 == "2":
        print("")
        print("> WHAT!? WHAT THE HELL DO YOU WANT, SHITLIPS!?")
        print("")
        input("'...Here's the uhh... Autopsy...sir.'")
      else:
        print("")
        input("> ...")
        print("")
        input("'...Here's the uhh... Autopsy...sir.'")
      input("'*The officer hands you a wrinkled piece of paper.'")
      autopsy.progress += 1
      print("")
      input("...")
      input("*You lost your train of thought...")
      print("[1] Reannalize the body {90%}")
      print("[2] Read the autopsy that was given instead")
      corpsequesta2 = input("CHOICE: ")
      if corpsequesta2 == "1":
        corpserandom = random.randint(0,10)
        if corpserandom == 10:
          print("[FAILURE]")
          input(">...Shit")
          input("*You don't notice anything off with the corpse.")
        else:
          print("[SUCCESS]")
          input("*As you look around, you notice that there is a small object, covered by the victim's hand.")
          input("YOU OBTAINED SE BULLET CASING")
          bullet_casing.progress += 1
      elif corpsequesta2 == "2":
         with open(autopsyfile) as file:
           print(file.read())
         input(">...This is the worst autopsy youve ever read.")
  
    elif corpsequest == "2":
      input("'Here ya go, Madam.'")
      input("'*The officer hands you a wrinkled piece of paper'")
      with open(autopsyfile) as file:
         print(file.read())
      input(">...This is the worst autopsy youve ever read")
      autopsy.progress += 1    
    input("...")
    input(">I think we are done here")
    corpse_discovery += 1

#prevent player from moving past mandatory scenes
def movementbarrier():
  global x_loc, y_loc
  if corpse_discovery == 0:
    if y_loc == 1:
      pass
    else:
      x_loc = 0
      y_loc = 1
      print("[YOU NEED TO INSPECT THE BODY FIRST]")
  
### ALTERANTIVE MAP/MOVEMENT DESIGN, instead of WASD just ask where the user wants to go

def inventory():
  print("")
  print("---------------------------------------")
  print("YOU HAVE: ")
  if autopsy.progress == 1:
    print(f"[1] {autopsy.name}")
  if bullet_casing.progress == 1:
    print(f"[2] {bullet_casing.name}")
  if safe_keycard.progress == 1:
    print(f"[3] {safe_keycard.name}")
  if vixen_gun.progress == 1:
    print(f"[4] {vixen_gun.name}")
  if lucas_gun.progress == 1:
    print(f"[5] {lucas_gun.name}")
  if rent_bill.progress == 1:
    print(f"[6] {rent_bill.name}")
  print("")

  print("---------------------------------------")
  print("")

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
  
def suspectroom():
  #INTEROGATION AND DIALOUGE SYSTEM
  pass
  
def vixentalk():
  #VIXEN DIALOUGE AND QUESTIONING
  pass
  
def lucastalk():
  #LUCAS DIALOUHE AND QUESTIONING
  pass
  
def olivertalk():
  #OLIVER DIALOUGE AND QUESTIONING
  pass
  
def vixenroom():
  input("*You look around the room...")
  input("*Cracks and mold are present in the walls...")
  input("*This would breach a few RISHA regulations...")
  input("...")
  input("'Hello?'")
  print("")
  input("*A child peeks around a corner, staring at you.")
  print("")
  print("[1] Wassup dude")
  print("[2] Are you not supposed to be here?")
  childquest = input("CHOICE: ")
  if childquest == "1":
    print(">Wassup dude")
    print("")
    input("'I'm not a dude!' the kid whinges")
    input("'I'm a girl, watch!'")
    input("*The child claps her hands as she spins around energetically")
    input("'See!'")
    input("*The child has a pride in her performance...")
    print("")
    print("[1] Wow! You are so good... at... that!")
    print("[2] Honestly, that was once of the worst performances I have ever seen, and I think you should give up")
    pass
  elif childquest == "2":
    print(">Are you not supposed to be here?")
    pass
  else:
    pass
  
  #VIXEN ROOM AND INTERACTION
  pass
  
def lucasroom():
  #LUCAS ROOM AND INTERACTION
  pass
  
def oliverroom():
  #OLIVER ROOM AND INTERACTION
  pass
  
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
  elif direction == "3":
    inventory()
while True:
  with open(mainui) as file:
    print(file.read())
  roomdesc()
  if autopsy.progress == 0:
    print(f"NAME: {autopsy.name}")
  #DEV TOOL
  print("COORDINATES: ",f"{x_loc}, {y_loc}")
  direction = input("CHOICE: ")
  movement(direction)


#heheh