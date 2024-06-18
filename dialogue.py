import random
import os
from items import autopsy, bullet_casing, lucas_gun, rent_bill, safe_keycard, vixen_gun


vixenstress = 0
oliverstress = 0
lucasstress = 0
lucasmad = 0
person = 'person.txt'
personstress = 'personstress.txt'
gameoverfile = 'gameover.txt'
gameoverwilson = 'gameoverwilson.txt'
casefile = 'casefile.txt'

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

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
    print("VIXEN")
    print("--------------------------------------------------")
    print("[1] How did you know the victim? ")
    print("[2] What did you know about the murder? ")
    if rent_bill.progress == 1:
      print("[3] Why are you still living here without paying all of your rent?")
    if rent_bill.progress == 1 and vixen_gun.progress == 1:
      print("[4] Did being poor and desperate ever factor into the murder?")
    print("[5] I'm done with you")
    print("--------------------------------------------------")
    vixentalkquest = input("CHOICE: ")
    cls()
    if vixentalkquest == "1":
      print("> How did you know the victim?")
      print("")
      input("'She was my neighbour.'")
      print("")
      input("'...'")
      print("")
      print("[1] Is that all?")
      print("[2] You have to cooperate with me here ma'am.")
      print("")
      vixentalkquest1 = input("CHOICE:")
      if vixentalkquest1 == "1":
        cls()
        print(">Is that all?")
        print("")
        input("'...She was...'")
        input("*She begins to trail off...")
        input("'Rich.'")
        print("")
        input(">How so?")
        cls()
        input("'She wears designer.'")
        print("")
        input("*Your face instinctvely scrunches with confusion")
        print("")
        input("'Fancy clothing.' She says reassuringly")
        input("'Pearls, Fur Scarves...'")
        input("'Practically a slap to the face to anybody here.'")
        print("")
        input(">Alright...")
        cls()
      elif vixentalkquest1 == "2":
        cls()
        print(">You have to cooperate with me here ma'am.")
        print("")
        input("'Do I now?'")
        input("'Because I have cooperated with many of your types'")
        input("'None, look this...'")
        input("*She begins to trail off...")
        input("'Fitting, lets say.'")
        print("")
        input(">Are you calling me ugly?")
        cls()
        input("*She begins to grin")
        input("'Yeah.'")
      else:
        cls()
        input(">Gurrrrrrkkkk")
        print("")
        input("*She looks disgusted")
        input("'Eugh...'")
      pass
  
    elif vixentalkquest == "2":
      print("> What did you know about the murder?")
      print("")
      input("'I woke up, to hear some yelling...'")
      input("'Then I went outside and I saw everyone surrounding the victim.'")
      input("'I was the last to know what was wrong by then.'")
      print("")
      pass
    elif vixentalkquest == "3":
      print(">Are you still living here without paying all of your rent?")
      print("")
      input("*She looks angry")
      input("'What the hell? Have you broken into our room?'")
      input("'If I found out you so happened to lay a FINGER on my daughter I will- '")
      print("")
      input("*She cuts herself off")
      print("")
      input("'...No, we have managed to convince the landlord, to say here'")
      input("'I managed to work overtime as of late, and was able to pay off rent'")
      print("")
      input("...")
      input("*She worked overtime?")
      pass
    elif vixentalkquest == "4" and vixenstress == 0:
      vixenstress += 1
      print(">Did being poor and desperate ever factor into the murder?")
      print("")
      input("*She looks at you tensely.")
      input("[*You can get her here, You have to be careful...]")
      cls()
      input("'Where did you get this idea?'")
      print("")
      print("[1] I found a gun in your apartment, Vixen")
      print("[2] I found you hiding a child in your apartment, Vixen")
      vixentalkquest4a = input("CHOICE: ")
      if vixentalkquest4a == "1":
        print("> I found a gun in your apartment, Vixen")
        with open(personstress) as file:
          print(file.read())
        input("'...what?'")
        print("")
        input(">A gun. In your apartment.")
        cls()
        with open(person) as file:
          print(file.read())
        input("'That does NOT mean I did it!'")
        input("'Someone else could have grabbed the gun!")
        print("")
        print("[1] Who would that be?")
        print("[2] No one could've stolen your gun.")
        vixentalkquest4b = input("CHOICE: ")
        if vixentalkquest4b == "1":
          cls()
          print("> Who would that be?")
          print()
          input("'Lucas!'")
          input("*She said this confidently")
          input("'... or Oliver'")
          input("*She said this meekly")
          print("")
          input("'I lost my keycard yesterday!'")
          input("'Someone could have grabbed it and stolen my gun!'")
          input("'If you ever find who has my keycard I'm sure they did it!")
          print("")
          input("*She says this truthfully...")
          input("*However, she looks to not know who could have stolen it")
          input("*Maybe I'm closer to figuring this one out...")
          #LOCK
          pass
        elif vixentalkquest4b == "2":
          cls()
          print("> No one could've stolen your gun.")
          print("")
          input("'What do you mean?'")
          input("*Her voiced cracked")
          print("")
          input("> Who would return a gun back to your safe?")
          input("*Her eyes stares deep into yours")
          input("> Especially when you have a daughter guarding your apartment?")
          input("> Now that I think about it... ")
          print("")
          input("*A deep blue ocean with a hint of green pasture...")
          print("")
          input("> -Who works overtime for a job they don't have?")
          input("> I thought you quit?")
          print("")
          input("*Every second her eyes swallows your attention...")
          print("")
          input("> $65 and you thought you could easily steal " +
                "from the richest person here")
          input("> but she struggled didn't she? She fought back?")
          input("> That was because she needed the money as much you do.")
          print("")
          input("*Deeper...")
          print("")
          input("> You took the gun you couldn't sell, and you shot a " + 
                "person as poor as you")
          input("> Only to find...")
          print("")
          input("*Deeper...")
          print("")
          input("> Barely enough")
          input("> But you did it. Didn't you?")
          input("> For her.")
          print("")
          input("*That was the longest you have spoke without an interruption...")
          print("")
          input("...")
          cls()
          with open(personstress) as file:
            print(file.read())
          print("[SUCCESS]")
          input("'Please don't arrest me-'")
          input("'I-I have a daughter-'")
          input("'She can't lose both of her parents...'")
          input("'Please. For the love of god.'")
          input("'I know what I did was bad, but I couldn't" +
                " let my daughter live homeless'")
          input("'Please. For the love of god.'")
          input("'Please...'")
          print("")
          input("...")
          input("*I guess it's time to make an arrest...")
        else:
          cls()
          print("[FAILURE]")
          print(">GACK!")
          print("")
          input("...")
          input("*Vixen's face stares intensly")
          input("*Her face moves, and wrinkles...")
          input("*Suddenly...")
          input("'HAHAHAHAHAHAHA HAAAAA'")
          input("'Oh my DAYS, what a JOKE!'")
          input("'I thought you were SERIOUS!'")
          input("'A GUN?'")
          input("'HAHAHAHAHAHAHA HAAAAA'")
          input("'I don't mean to laugh at you, I know it is tough to live like this'")
          input("'-But I think your behaviors and appearance is a bit too...'")
          print("")
          input("*She tries to stiffle a laugh")
          input("*She is failing...")
          print("")
          input("'Silly!'")
          print("")
          input("*Vixen refuses to take you seriously...")
          input("*You are such a joke...")      
      elif vixentalkquest4a == "2":
        cls()
        print("> I found you hiding a child in your apartment, Vixen")
        print("")
        print("[FAILURE]")
        input("'...I am not hiding a child'")
        input("'I'm sure that everyone knows about her by now...'")
        input("'Including you!'")
        input("'Are you even a detective? Should I even be talking to you?'")
        print("")
        input("*This, sadly, is a genuine question...")
        print("")
        input("'Get away from me!'")
        print("")
        input("*..dammit")
        pass
      else:
        cls()
        print("[FAILURE]")
        print(">GACK!")
        print("")
        input("...")
        input("*Vixen's face stares intensly")
        input("*Her face moves, and wrinkles...")
        input("*Suddenly...")
        input("'HAHAHAHAHAHAHA HAAAAA'")
        input("'Oh my DAYS, what a JOKE!'")
        input("'I don't mean to laugh at you, I know it is tough to live like this'")
        input("'-But I think your behaviors and appearance is a bit too...'")
        print("")
        input("*She tries to stiffle a laugh")
        input("*She is failing...")
        print("")
        input("'Silly!'")
        print("")
        input("*Vixen refuses to take you seriously...")
        input("*You are such a joke...")
      pass
    if vixentalkquest == "4" and vixenstress == 1:
      input("*I think we are done with her")
      pass
    if vixentalkquest == "5":
      break
    else:
      print("WRONG INPUT")
      pass



  #VIXEN DIALOGUE AND QUESTIONING
  pass

def lucastalk():
  global random
  global lucasstress, lucasmad
  while True:
    cls()
    if lucasstress == 0:
      with open(person) as file:
        print(file.read())
    elif lucasstress == 2:
      with open(personstress) as file:
        print(file.read())
    print("LUCAS")
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
      print("> How did you know the victim? ")
      print("")
      input("'She was my wife.'")
      input("'She was smart, funny...'")
      input("*His face remains neutral")
      input("'Pretty much the perfect person to ask for'")
      input("*His face shifts into a sad stare")
      input("'I don't know why anyone would kill her'")
      print("")
      input("> Wasn't she rich?")
      print("")
      input("'No. She wasn't...'")
      input("'I don't really want to talk more about her'")
      input("*He's knows more than he is letting on...")
      input("*Maybe you could take him by surprise here...")
      print("")
      print("[1] You know more than youre letting on")
      print("[2] Heh, I hate MY wife too, HIGH FIVE! (30%)")
      lucastalkquestA = input("CHOICE: ")
      print("")
      if lucastalkquestA == "1":
        cls()
        print("> You know more than youre letting on")
        print("")
        input("'What did you say to me?'")
        input("*He looks mad...")
        input("'My WIFE worked SO hard to make sure we don't end up homeless!'")
        input("'She has provided so much for US!'")
        input("'NEVER imply that I am hiding something again.'")
        print("")
        input("*Despite rumors, it appears that both Lucas and Lisa are poverish...")
        input("*You should probably ease on the subject...")
        pass
      elif lucastalkquestA == "2":
        print("> Heh, I hate MY wife too, HIGH FIVE! (30%)")
        lucasrandom = random.randint(0, 10)
        if lucasrandom >= 3:
          input("*You raise your hand, adorned with a dumb grin")
          input("*He looks unimpressed")
          input("*Scratch that. He looks annoyed")
          input("*Scratch that again. He looks like he is about" +
                " to punch you in your face")
          print("")
          input("THWOK!")
          cls()
          input("...")
          input("You stand up from the ground, your mouth burns")
          input("You somehow look uglier than before.")
          lucasmad += 1
          break
        elif lucasrandom <= 3:
          input("*You raise your hand, adorned with a smart grin")
          input("*He looks confused")
          input("'What?'")
          print("")
          input("> I hate my stupid wife too!")
          print("")
          input("*He looks ashamed")
          input("'She would've made the same joke y'know'")
          input("'She was the perfect women, I swear'")
          input("'I cheated on her. A while back...'")
          input("'With a fellow soldier'")
          input("'I just couldn't love her enough")
          input("'Not with her, not with any woman'")
          input("'And you wanna know what she said when she found out?'")
          input("'I'm sorry.'")
          input("'I can't believe anyone would have killed her'")
          input("'She was too nice. Way too nice for anyone'")
          input("'Especially me.'")
          print("")
          input("'I'm sorry.'")
          print("")
          input("*You recall Wilson's words...")
          input("*You lower your hand.")
          lucasstress += 1
          pass
          
        pass
      else:
        pass
        
      pass
    elif lucastalkquest == "2":
      print("> What did you know about the murder? ")
      print("")
      input("'I was waiting for my wife getting back from work'")
      input("'I then hear yelling.'")
      input("*He pauses")
      input("'Then I heard a gunshot'")
      print("")
      input("*He sounds indifferent")
      print("")
      input("'I came outside, and I saw my neighbor Oliver checking up on her'")
      input("'I then saw him pocket something'")
      input("'Like a piece of paper or something'")
      input("'Vixen then finally came outside to check what was going on'")
      input("'That's all I know")
      print("")
      input("*...Oliver pocketed a piece of paper?")
      pass
    elif lucastalkquest == "3":
      print("> Tell me why you have a gun in your room?")
      print("")
      input("*He looks unimpressed")
      input("'It's a service weapon'")
      input("'If you are implying that I killed my wife I reccomend you not doing so'")
      print("")
      input("*Threats aside, this does give you a reason to arrest him...")
      pass
    elif lucastalkquest == "4":
      break
    else:
      print("WRONG INPUT")
      pass

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
    print("OLIVER")
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
      print("> How did you know the victim? ")
      print("")
      input("*He shifts awkardly...")
      input("'I don't know much about her sir.'")
      input("'S-she seemed nice'")
      input("'-wore faux fur scarves, with imitation pearls'")
      input("'I guess its that type of 'live the life you want to live' sorta thing'")
      input("'I-I heard that she develops mostly on pills for feet fungus...'")
      input("'I believe it's FORAZ she works at which is probably why she works" +
            " long hours.'")
      input("'I believe they scored 98th on employee beneficiaries as of last month-'")
      input("...")
      input("*He's rambling nonsense...")
      input("'-I can't recall what chemical they mainly use for FungiFungo," +
            " but I heard it's pretty expensive, and-")
      print("")
      print("[1] You didn't know much about her you said?")
      print("[2] Oh my GOD, can you shut up PLEASE")
      print("")
      olivertalkquesta = input("CHOICE: ")
      if olivertalkquesta == ("1"):
        print("> You didn't know much about her you said?")
        print("")
        input("'Yeah'")
        print("")
        input("...")
        input("'I just thought these things would be common knowledge by now'")
        input("'Like, I know what Vixen's situation like, but I can't say-'")
        input("*He cuts himself off")
        input("'Nevermind, it is rude to gossip about people's struggles'")
        input("'I didn't know much about Lisa other than that, sorry.'")
        print("")
        input("*...Alright")
        pass
      elif olivertalkquesta == ("2"):
        print("> Oh my GOD, can you shut up PLEASE")
        print("")
        input("'...'")
        input("'S-sorry, sir'")
        input("'...'")
        input("*...Alright")
        pass
      #FINISH
      pass
    if olivertalkquest == "2":
      print("> What did you know about the murder? ")
      print("")
      input("'I woke up to a gunshot... and then I looked outside...'")
      input("'I tried to help her...'")
      input("'-but she died later'")
      input("*hm")
      input("*He doesnt have much to say...")
      pass
    if olivertalkquest == "3" and oliverstress == 0:
      cls()
      oliverstress+=1
      print("> Where did you find this?")
      print("")
      with open(personstress) as file:
        print(file.read())
      input("...")
      input("'I did it sir.'")
      print("")
      input("...")
      input("> What?")
      print("")
      input("'I shot her'")
      input("> ...Why?")
      input("*He pauses")
      input("'I am a thief, sir'")
      input("'I have broken into other rooms, as well as Vixen's'")
      input("'That was the keycard I have stolen to steal from her'")
      input("'Y-Yesterday, I planned on stealing from Lisa'")
      input("'B-but it went wrong, and I shot her in the stomach'")
      input("'Thats the truth sir'")
      print("")
      input("...")
      input("*You remembered what Wilson has told you...")
      input("*Let's make an arrest")
      pass
    elif olivertalkquest == "3" and oliverstress == 1:
      input("*We should stop talking to him")
    if olivertalkquest == "4":
      break
    else:
      print("WRONG INPUT")
      pass

  #OLIVER DIALOGUE AND QUESTIONING
  pass


def intro():
  input("You are a commodity.")
  input("You are interchangable to Oil, Land, or Water.")
  input("Your value, however, is tied to work.")
  input("Such as gasoline's value is producing energy, you produce work.")
  input("Your work, however, is tied to solving murders.")
  input("You are the first of your brand to do so.")
  input("It is of upmost importance, that you will excel at your job.")
  input("if not...")
  input("'Products can always be recalled.'")
  print("")
  input("...")
  print("")
  input("You arrive on the scene:")
  input("This is what you know...")
  with open(casefile) as file:
    print(file.read())
  input("...")
  cls()
  input("The memory burns...")
  input("Get going, product.")

def end():
  with open(gameoverfile) as file:
    print(file.read())
  input("WHAT HAPPENS NEXT?: ")
  print("...")
  quit()

def oliverend():
  if oliverstress == 1:  
    cls()
    input("Based on the confession of Oliver, you seized him")
    input("He was put through 15 years of correctional training")
    input("They were no outrages, nor protests against this ruling")
    input("However,")
    input("A fringe group of conspiracy theorists believe that Oliver" +
          " was covering for someone")
    input("Although these never left niche internet forums")
    input("Oliver, by all means, was not guilty other than tampering")
    input("That does not matter however")
    input("You did your job perfectly")
    input("You live long to be Jax Co's best product")
    end()
  else:
    cls()
    input("Based on the standard of absolutely nothing, you arrested Oliver")
    input("They are put through 23 years of correctional training")
    input("Outraged and appalled, many claimed that you should be punished")
    input("You were")
    input("You have been recalled, never to be seen again")
    end()

def lucasend():
  if lucasstress == 1:
    cls()
    input("Based on loose hypotheticals, you arrested Lucas")
    input("He was put through death")
    input("Many were outraged against Lucas for killing his loving wife")
    input("The discoverey of his affair was used more for propaganda " +
          "rather than evidence ")
    input("You have exceeded the expectations of Jax Co.")
    input("You are given 133% raise")
    input("You now make $1.33 an hour")
    input("Do not spend it all in one place!")
    cls()
    end()
    pass
  else:
    cls()
    input("Based on the standard of absolutely nothing, you arrested Lucas")
    input("They are put through 23 years of correctional training")
    input("Outraged and appalled, many claimed that you should be punished")
    input("You were")
    input("You have been recalled, never to be seen again")
    cls()
    end()

def vixenend():
  if vixenstress == 1:
    input("Based on the evidence, as well as an admission of guilt, " +
          "you arrested Vixen")
    input("She was sentenced to 23 years of correctional training")
    input("By all means you have done your job well")
    input("However many were heartbroken and saddened by this")
    input("Several people began to run charities as well as orginizations" +
          " to help poverish families, to prevent this from ever happening again")
    input("Although you were not recalled, you were given the luxury " +
          "of your first berating")
    input("You have developed tinnitus")
    input("For now on, for every single waking hour, you will remember your first case")
    input("Vixen's child, will not be able to see her mother until she is 29")
    input("...Your ear rings")
    cls()
    end()
    pass
  else:
    cls()
    input("Based on the standard of absolutely nothing, you arrested Vixen")
    input("They are put through 23 years of correctional training")
    input("Outraged and appalled, many claimed that you should be punished")
    input("You were")
    input("You have been recalled, never to be seen again")
    end()
    pass
  cls()
  end()

def wilsonend():
  cls()
  input("Based on the standard of absolutely nothing, you arrested Wilson")
  input("Arresting a fellow cop, usually means that the trial would be cancelled")
  input("However, many began to think that this was hilarious")
  input("Several people began to protest for the arrest of Wilson ")
  input("This began a long chain of jokes and mocking from wider society")
  input("Many cried of laughter after it was announced that they would" +
        " comply to your arrest")
  input("You were subsequently beaten, burned and shot at, by Jax Co affiliates")
  input("This began another set of jokes where people mourned for your death")
  input("You even had your own mock grave, decorated in front of several campuses")
  if vixenstress == 1:
    input("If you were alive as of now. You'd be proud with what you have done")
    input("You will be remembered for a very long time")
  cls()
  with open(gameoverwilson) as file:
    print(file.read())
  quit()
  