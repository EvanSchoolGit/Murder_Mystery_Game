
#CHECKLIST
#Add option of descriptions in inventory
#finish all dialouge
#finish all endings
#clean up UI
#######################################################################
# Title : Murder Mystery
# Class : Computer Science 30
# Assighnment : make a murder mystery text game
# Coder : Evan Urban and Tibby Schell
# Version : 1
########################################################################
""" 
Incomplete Murder Mystery Game. 
"""
###########################-IMPORTS-##########################
import random
import os

from dialogue import vixentalk, olivertalk, lucastalk

from end import oliverend, lucasend, vixenend, wilsonend, intro

from items import autopsy, bullet_casing, lucas_gun, rent_bill, safe_keycard, vixen_gun

from rooms import vixenroomentry, vixen_roomentry, vixenroom, lucasroom, oliverroom



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
personstress = 'personstress.txt'
movementui = 'movementui.txt'
mainui = 'mainui.txt'
autopsyfile = 'autopsy.txt'
casefile = 'casefile.txt'

rooms = {
  "Room 118": {
    "name" : "ROOM: Oliver's Room",
    "description" : ""'Oliver lives here.'""},

  "Room 119": {
    "name" : "ROOM: Suspects Lineup",
    "description" : " "},

  "Room 120": {
    "name" : "ROOM: Lucas' Room",
    "description" : """Lucas and Lisa used to live here."""},

  "Room 121": {
    "name" : "ROOM: Vixen's Room",
    "description" : "Vixen lives here."},

  "Hallway": {
    "name" : "ROOM: Hallway",
    "description" : "The corpse is placed here."}

}

def cls():
  os.system('cls' if os.name=='nt' else 'clear')


intro()

def tutorial():
  #Text Scrunch Problems Fix
  global wilson_progress
  with open(person) as file:
    print(file.read())
  if wilson_progress == 0:
    input("'God, you're so ugly!'")
    input("'Why does your skin look transparent, Jesus Christ!'")
    print("")
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
    input("I couldn't care less about who actually did it: ")
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
    input("WHY ARE YOU TALKING TO ME?! GO TO THE BODY LACKY!: ")
tutorial()

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
      input("*You look over the body and see a bloodied gash on the victims" +
            "chest near the heart.")
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
      print("[1] Reanalyze the body {90%}")
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
         input(">...This is the worst autopsy you've ever read.")
  
    elif corpsequest == "2":
      input("'Here ya go, Madam.'")
      input("'*The officer hands you a wrinkled piece of paper.'")
      with open(autopsyfile) as file:
         print(file.read())
      input(">...This is the worst autopsy youve ever read.")
      autopsy.progress += 1    
    else:
      print("")
      input("> ...")
      print("")
      input("'...Here's the uhh... Autopsy...sir.'")
      input("'*The officer hands you a wrinkled piece of paper.'")
      autopsy.progress += 1
    input("...")
    input(">I think we are done here...")
    corpse_discovery += 1



def inventory():
  #FINISH INVENTORY EXCEPTIONS
  while True:
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
    print("[9] Leave")
    print("---------------------------------------")
    print("")
    invchoice = input("CHOICE: ")
    if invchoice == "1" and autopsy.progress == 1:
      cls()
      print(f"{autopsy.description}")
      with open(autopsyfile) as file:
         print(file.read())
      pass
    elif invchoice == "2" and bullet_casing.progress == 1:
      cls()
      print(f"{bullet_casing.description}")
      pass
    elif invchoice == "3" and safe_keycard.progress == 1:
      cls()
      print(f"{safe_keycard.description}")
      pass
    elif invchoice == "4" and vixen_gun.progress == 1:
      cls()
      print(f"{vixen_gun.description}")
      pass
    elif invchoice == "5" and lucas_gun.progress == 1:
      cls()
      print(f"{lucas_gun.description}")
      pass
    elif invchoice == "6" and rent_bill.progress == 1:
      cls()
      print(f"{rent_bill.description}")
      pass
    elif invchoice == "9":
      break
    else:
      pass
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
    print ("[PRESS 2] ... What do I need to again?")
  
def suspectroom():
  input("*You step inside...")
  input("*What should I do first")
  while True:
    cls()
    print("")
    print("------------------------------------")
    print("[1] TALK TO OLIVER")
    print("[2] TALK TO LUCAS")
    print("[3] TALK TO VIXEN")
    print("[4] DO SOMETHING ELSE")
    print("[5] MAKE AN ARREST")
    print("------------------------------------")
    print("")
    suspectroomchoice = input("CHOICE: ")
    if suspectroomchoice == "1":
      olivertalk()
      pass
    if suspectroomchoice == "2":
      lucastalk()
      pass
    if suspectroomchoice == "3":
      vixentalk()
      pass
    if suspectroomchoice == "4":
      break
    if suspectroomchoice == "5":
      arrest()
      pass
      
def arrest():
  cls()
  print("(WARNING, THIS IS THE FINAL DESCISION, BE CAUTIOUS)")
  print("")
  print("--------------------------------------------------")
  print("[1] ARREST OLIVER")
  print("[2] ARREST LUCAS")
  print("[3] ARREST VIXEN")
  print("[4] ARREST WILSON")
  print("[5] Let me rethink this...")
  print("--------------------------------------------------")
  arrestchoice = input("CHOICE")
  while True:
    if arrestchoice == "1":
      oliverend()
    elif arrestchoice == "2":
      lucasend()
    elif arrestchoice == "3":
      vixenend()
    elif arrestchoice == "4":
      wilsonend()
    elif arrestchoice == "5":
      break
    else:
      pass
  pass
  

  
def movement(direction): 
  global x_loc, y_loc
  cls()
  if direction == "1":  #This will ask directly where the user wants to go.
    while True:
      with open(movementui) as file:
        print(file.read())
      directionquest = input("Where do you want to go to?: ")
      if directionquest == "1":
        x_loc = 1
        y_loc = 1
        break
      elif directionquest == "2":
        x_loc = 0
        y_loc = 0
        break
      elif directionquest == "3":
        x_loc = 1
        y_loc = 0
        if vixen_roomentry == 0:
          vixenroomentry()
        elif vixen_roomentry == 2:
          x_loc = 1
          y_loc = 1
          input("[YOU MADE A KID CRY, SHE IS NOT LETTING YOU INSIDE.]")
          break
        else:
          break
        break
      elif directionquest == "4":
        x_loc = 0
        y_loc = 2
        break
      elif directionquest == "5":
        x_loc = 1
        y_loc = 2
        break
      else:
        pass     
  elif direction == "2":
    if x_loc == 0 and y_loc == 0:
      suspectroom()
      pass
      #suspect room
    elif x_loc == 1 and y_loc == 0:
      vixenroom()
    elif x_loc == 0 and y_loc == 1:
      tutorial()
    elif x_loc == 1 and y_loc == 1:
      corpseinter()
    elif x_loc == 0 and y_loc == 2:
      oliverroom()
    elif x_loc == 1 and y_loc == 2:
      lucasroom()  
    else:
      input("*THERE IS NOTHING HERE TO DO")
  elif direction == "3":
    inventory()

while True:
  cls()
  with open(mainui) as file:
    print(file.read())
  roomdesc()
  #DEV TOOL
  print("")
  direction = input("CHOICE: ")
  movement(direction)


#heheh 