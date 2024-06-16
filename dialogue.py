from items import autopsy, bullet_casing, lucas_gun, rent_bill, safe_keycard, vixen_gun
from end import cls

vixenstress = 0
oliverstress = 0
lucasstress = 0
person = 'person.txt'
personstress = 'personstress.txt'

def vixentalk():
  global vixenstress
  while True:
    cls()
    if vixenstress == 0:
      with open(person) as file:
        print(file.read())
    elif vixenstress == 2:
      with open(personstress) as file:
        print(file.read())
    print("--------------------------------------------------")
    print("[1] How did you know the victim? ")
    print("[2] What did you know about the murder? ")
    if rent_bill.progress == 1:
      print("[3] Why are you still living here without paying all of your rent?")
    if rent_bill.progress == 1 and vixen_gun.progress == 1:
      print("[4] Did you being poor and desperate ever factor into the murder?")
    print("[5] I'm done with you")
    print("--------------------------------------------------")
    vixentalkquest = input("CHOICE: ")
    cls()
    if vixentalkquest == "1":
      print("> How did you know the victim?")
      print("")
      input("'She was my neighbor'")
      print("")
      input("'...'")
      pass
    if vixentalkquest == "2":
      print("> What did you know about the murder?")
      print("")
      input("'I woke up, to hear some yelling...'")
      input("'Than I got ouside and I saw everyone surronded by the victim'")
      pass
    if vixentalkquest == "3":
      pass
    if vixentalkquest == "4":
      pass
    if vixentalkquest == "5":
      break



  #VIXEN DIALOGUE AND QUESTIONING
  pass

def lucastalk():
  global lucasstress
  while True:
    cls()
    if lucasstress == 0:
      with open(person) as file:
        print(file.read())
    elif lucasstress == 2:
      with open(personstress) as file:
        print(file.read())
    print("--------------------------------------------------")
    print("[1] How did you know the victim? ")
    print("[2] What did you know about the murder? ")
    if lucas_gun.progress == 1:
      print("[3] Tell me why you have a gun in your room?")
    print("[4] I'm done with you")
    print("--------------------------------------------------")
    lucastalkquest = input("CHOICE: ")
    cls()
    if lucastalkquest == "1":
      pass
    if lucastalkquest == "2":
      pass
    if lucastalkquest == "3":
      pass
    if lucastalkquest == "4":
      break

  #LUCAS DIALOGUE AND QUESTIONING
  pass

def olivertalk():
  global oliverstress
  while True:
    cls()
    if oliverstress == 0:
      with open(person) as file:
        print(file.read())
    elif lucasstress == 2:
      with open(personstress) as file:
        print(file.read())
    print("--------------------------------------------------")
    print("[1] How did you know the victim? ")
    print("[2] What did you know about the murder? ")
    if safe_keycard.progress == 1:
      print("[3] Where did you find this?")
    print("[4] I'm done with you")
    print("--------------------------------------------------")
    olivertalkquest = input("CHOICE: ")
    cls()
    if olivertalkquest == "1":
      input("*He shifts awkardly...")
      input("'I don't know much about her sir'")
      input("'I woke up to a gunshot... and then I looked outside...'")
      input("'I tried to help her...'")
      input("'-but she died later'")
      input("*hm")
      pass
    if olivertalkquest == "2":
      input("'I woke up to a gunshot... and then I looked outside...'")
      input("'I tried to help her...'")
      input("'-but she died later'")
      input("*hm")
      pass
    if olivertalkquest == "3":
      pass
    if olivertalkquest == "4":
      break

  #OLIVER DIALOGUE AND QUESTIONING
  pass
