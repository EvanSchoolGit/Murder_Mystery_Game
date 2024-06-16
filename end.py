import os

gameoverfile = 'gameover.txt'
gameoverwilson = 'gameoverwilson.txt'
casefile = 'casefile.txt'


def intro():
  input("You are a commodity.")
  input("You are interchangable to Oil, Land or Water")
  input("Your value, however, is tied to work")
  input("Such as gasoline's value is producing energy, you produce work")
  input("Your work, however, is tied to solving murders")
  input("You are the first of your brand to do so")
  input("It is upmost importance, that you will excel at your job")
  input("if not...")
  input("'Products can always be recalled'")
  print("")
  input("...")
  print("")
  input("You arrive on the scene")
  input("This is what you know...")
  with open(casefile) as file:
    print(file.read())
  input("...")
  cls()
  input("The memory burns...")
  input("Get going, product")


def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def end():
  with open(gameoverfile) as file:
    print(file.read())
  input("WHAT HAPPENS NEXT?: ")
  print("...")
  quit()

def oliverend():
  end()

def lucasend():
  end()

def vixenend():
  end()

def wilsonend():
  with open(gameoverwilson) as file:
    print(file.read())
  pass