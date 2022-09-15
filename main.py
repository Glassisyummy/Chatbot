def s():
  global starter
  starter = input("Hello, My name is Chatterbot!  a) Hello! q) Quit ")

def continue1st():
  global continue1
  if starter == 'a':
    continue1 = input("It's nice to meet you, what's your name? ")
  else:
    continue1 = input("That wasn't really an answer choice, but what's your name? ")
    
def continue2nd():
  global continue2
  global c
  c = " is a pretty name. What do you do for fun? "
  continue2 = input(continue1 + c)

def continue3rd():
  global continue3
  continue3 = input(continue2 + " is a cool hobby. Where are you from? ")

def continue4th():
  global continue4
  continue4 = input(continue3 + "? Do you like it there?     a) Yes  b) No  q) Quit ")
  
def continue5th():
  if continue4 == 'a':
    global continue5
    continue5 = input("Love that for you. How are you today? ")
  elif continue4 == 'b':
    continue5 = input("I'm sorry to hear that. How are you today? ")
  else:
    continue5 = input("I don't know what that's supposed to mean, but how are you today? ")

def ending():
  print("Cool, thanks for talking with me!")


s()
if starter != 'q':
  continue1st()
  if continue1 != 'q':
    continue2nd()
    if continue2 != 'q':
      continue3rd()
      if continue3 != 'q':
        continue4th()
        if continue4 != 'q':
          continue5th()
          if continue5 != 'q':
            ending()