def s():
  global starter
  starter = input("Hello, My name is Chatterbox /n a) Hello! q) Quit ")

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

def ending():
  d = " is a cool hobby, thanks for talking with me!"
  print(continue2 + d)


s()
if starter != 'q':
  continue1st()
  if continue1 != 'q':
    continue2nd()
    if continue2 != 'q':
      ending()