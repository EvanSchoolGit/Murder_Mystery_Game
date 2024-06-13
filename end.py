
gameoverfile = 'gameover.txt'
gameoverwilson = 'gameoverwilson.txt'

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