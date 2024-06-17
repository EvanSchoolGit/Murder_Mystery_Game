import random
from items import autopsy, bullet_casing, lucas_gun, rent_bill, safe_keycard, vixen_gun
import os

vixen_roomentry = 0
kidlock = 0
safeprogress = 0

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def vixenroomentry():
  #When incorrect choice in first question, it does nothing
  global vixen_roomentry, kidlock
  input("*You open the door...")
  input("*Cracks and mold are immediately present before entry...")
  input("*This would breach a few RISHA regulations...")
  input("...")
  input("'Hello?'")
  print("")
  input("*A child peeks around the doorframe, staring at you.")
  print("")
  print("[1] Wassup dude")
  print("[2] Are you not supposed to be here?")
  childquest = input("CHOICE: ")
  if childquest == "1":
    print(">Wassup dude")
    print("")
    input("'I'm not a dude!' the kid whines.")
    input("'I'm a girl, watch!'")
    input("*The child claps her hands as she spins around energetically.")
    input("'See!'")
    input("*The child has a pride in her performance...")
    print("")
    print("[1] Wow! You are so good... at... that!")
    print("[2] Honestly, that was once of the worst performances I have ever seen, " +
    "and I think you should give up, as soon as possible.")
    childquesta = input("CHOICE: ")
    if childquesta == "1":
      print("> Wow! You are so good... at... that!")
      print("")
      input("'I know!'")
      input("'I'm not allowed to let angry men inside'")
      input("'My mom told me that'")
      print("")
      print("[1] I am not angry")
      print("[2] I am not a man")
      childquesa1 = input("CHOICE: ")
      if childquesa1 == "1":
        print(">I am not angry")
        print("")
        input("'Oh, Okay!'")
        input("*The child opens the door wider")
        input("'Come inside!'")
        vixen_roomentry += 1
      elif childquesa1 == "2":
        print(">I am not a man")
        print("")
        input("'Oh...'")
        input("*She squints her eyes...")
        input("'What are you then?'")
        print("")
        input("*You don't know how to answer that...")
        input("'Doesn't matter! You can come in!'")
        vixen_roomentry += 1
      else:
        input("*At this moment in time, the worst scenario to have an episode, " +
          "is at this current conversation")
        input("*However, as she looks at you with a curious gaze, " +
          "it quickly turns into a horrified stare as the bones " +
          "in your body begin to crack")
        input("*Your jaw unhinges, while your posture slumps, still keeping your eye" +
          "contact with her")
        input("*She immediateley slams the door...")
        print("")
        input(">...dammit")
        vixen_roomentry += 2
    elif childquesta == "2":
      print(">Honestly, that was once of the worst performances I have ever seen, " +
    "and I think you should give up, as soon as possible.")
      print("")
      input("*The child covers her mouth as if you shouted at her.")
      input("*She holds her hands still as her breathing draws quicker and quicker.")
      input("*Tears form around her eyes, as she tries to stiffle her reaction,")
      input("*But she cannot hold it in.")
      input("*Congratulations, you just made a kid cry!")
      input("*She immediateley slams the door...")
      print("")
      input(">Alright...")
      vixen_roomentry += 2
    else:
      input("*At this moment in time, the worst scenario to have an episode, " +
            "is at this current conversation")
      input("*However, as she gazes at you with a proud look, " +
            "it quickly turns into a horrified stare as the bones " +
            "in your body begin to crack")
      input("*Your jaw unhinges, while your posture slumps, still keeping your eye" +
            "contact with her")
      input("*She immediateley slams the door...")
      print("")
      input(">...Dammit")
      vixen_roomentry += 2

  elif childquest == "2":
    print(">Are you not supposed to be here?")
    print("")
    input("*It scowls at you...")
    input("'Are YOU not supposed to be here'")
    input("'MY mom says I shouldn't let angry men inside'")
    input("'and you seem to be all of those things...'")
    print("")
    print("[1] *Rush inside and throw the kid out (80%)")
    print("[2] I am actually a very reasonable person")
    childquestb = input("CHOICE: ")
    if childquestb == ("1"):
      childrandom = random.randint(0, 10)
      if childrandom > 8:
        print("[FAILURE]")
        input("*You take form in a sprinter's position...")
        input("*You have to act fast, and calculated, and-")
        input("*...chk...click")
        input("*...The door losed...")
        input("*You slowly get up.")
        input(">...Alright.")
        vixen_roomentry += 2
      elif childrandom < 8:
        print("[SUCCESS]")
        input("In one swift action, you ran inside as well as pushing out the child.")
        input("'HEY!'")
        input("*SLAM...click")
        input("*You closed, and locked the door...")
        kidlock += 1
        vixen_roomentry += 1
    elif childquestb == "2":
      print(">I am actually very reasonable")
      print("")
      input("'Oh, Okay!'")
      input("*The kid opens the door a bit more.")
      input("'Come in!'")
      vixen_roomentry += 1
    else:
      input("*...chk...click")
      input("*...The door closed...")
      input(">...Alright.")
  else:
    pass
  pass



def vixenroom():
  global safeprogress
  input("*You step inside...")
  input("*What should I do first?")
  while True:
    cls()
    print("")
    print("------------------------------------")
    print("[1] CHECK THE BEDROOM")
    print("[2] CHECK THE LIVING ROOM")
    print("[3] CHECK THE BATHROOM")
    if kidlock < 1:
      print("[4] TALK TO THE CHILD")
    print("[5] DO SOMETHING ELSE")
    print("------------------------------------")
    print("")
    vixenroomchoice = input("CHOICE: ")
    if vixenroomchoice == "1" and safeprogress == 0:
      input("*You look around the room...")
      input("*There's a safe in the corner...")
      safekeypad = input("INPUT: ")
      if safekeypad == "187":
        input("DING!")
        vixen_gun.progress += 1
        safeprogress += 1
        input("*As you open the door, you notice that there is only one item here")
        print("YOU FOUND GUN")
        input("[CHECK YOUR INVENTORY TO LEARN MORE]")
      else:
        input("BEEP!")
        input("*You got it wrong")
        pass      
      pass
    elif vixenroomchoice == "1" and safeprogress == 1:
      input("*You already inspected this")
    elif vixenroomchoice == "2":
      input("*A Couch. One Table. Three Chairs")
      input("*Those are the only things here.")
      input("*Scratch that. There is something else here")
      print("YOU FOUND RENT BILL")
      input("[CHECK YOUR INVENTORY TO LEARN MORE]")
      rent_bill.progress += 1
      pass
    elif vixenroomchoice == "3":
      input("*Seriously what is wrong with you?")
      input("*You found nothing. Weirdo.")
      pass
    elif vixenroomchoice == "4":
      input("'Why do you look like that?'")
      input("*The child looks at you curiously")
      input("'Did you get into an accident?'")
      input("'-or maybe like an EXPLOSION?!'")
      input("'Did you go all BOOM!'")
      input("*She gestures her hands to mimic an explosion...")
      print("")
      input("*You just stare at her")
      input("*She giggles")
      input("'You look funny!'")
      input("*This kid is already a handful...")
      input("*-and you met her 3 minutes ago...")
      pass
    elif vixenroomchoice == "5":
      break
    else:
      input("WRONG INPUT")



def lucasroom():
  #IF REPEATED DIALOGUE THEN BAD
  input("*You step inside...")
  input("*What should I do first?")
  while True:
    cls()
    print("")
    print("------------------------------------")
    print("[1] CHECK THE BEDROOM")
    print("[2] CHECK THE LIVING ROOM")
    print("[3] CHECK THE BATHROOM")
    print("[4] DO SOMETHING ELSE")
    print("------------------------------------")
    print("")
    lucasroomchoice = input("CHOICE: ")
    if lucasroomchoice == "1" and lucas_gun.progress==0:
      input("*The room is well made...")
      input("It looks as if it was just cleaned")
      input("*...or hasnt been used...")
      input("*You notice something ontop of the bedstand")
      print("YOU FOUND REVOLVER")
      input("[CHECK YOUR INVENTORY TO LEARN MORE]")
      print("")
      input("*...Look what we have here...")

      lucas_gun.progress+=1
      pass
    if lucasroomchoice == "1" and lucas_gun.progress==1:
      input("*I already checked here...")
      pass
    elif lucasroomchoice == "2":
      input("*You notice a punch hole in one of the walls...")
      input("*besides that...")
      input("*nothing...")
      pass
    elif lucasroomchoice == "3":
      input("...>Why am I here?")
      pass
    elif lucasroomchoice == "4":
      break
    else:
      input("WRONG INPUT")
      pass

  #LUCAS ROOM AND INTERACTION

def oliverroom():
  input("*You step inside...")
  input("*What should I do first?")
  while True:
    cls()
    print("")
    print("------------------------------------")
    print("[1] CHECK THE BEDROOM")
    print("[2] CHECK THE BATHROOM")
    print("[3] DO SOMETHING ELSE")
    print("------------------------------------")
    print("")
    oliverroomchoice = input("CHOICE: ")
    if oliverroomchoice == "1":
      input("*This is really depressing")
      input("*There is nothing here but a stench, and a mattress")
      input("*The matteress, lays on the floor, along with one pillow...")
      input("*You see a cockroach scuttle out of it")
      print("")
      input("...")
      input("*I'm going to pass out")
      pass
    elif oliverroomchoice == "2":
      input("*You step inside the bathroom")
      input("*It's just a hole...")
      input("*Just a hole to pee and crap in")
      input("*There is something that catches your eye however")
      input("*You plunge your hand in to the toilet hole...")
      print("")
      print("*YOU FOUND VAULT PASS CODE")
      input("[CHECK YOUR INVENTORY TO LEARN MORE]")
      safe_keycard.progress +=1
      pass
    elif oliverroomchoice == "3":
      break
    else:
      input("WRONG INPUT")
      pass
