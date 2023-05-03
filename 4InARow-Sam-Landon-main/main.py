#import
import turtle as t

wn = t.Screen()
wn.setup(1280, 720)
fontTitle = ("Time New Roman", 100, "normal")
fontPlay = ("Time New Roman", 50, "normal")
menu_image = "./mainMenu.gif"
wn.addshape(menu_image)
wn.addshape("./board.gif")
background = t.Turtle()
background.shape(menu_image)
brdTrt = t.Turtle()
brdTrt.hideturtle()
brdTrt.shape("./board.gif")
peice = t.Turtle()
peice.shape("circle")
peice.speed(0)
peice.shapesize(3)
peice.hideturtle()
message = t.Turtle()
message.hideturtle()
message.penup()
message.goto(0,300)
clickCount=0

move = 0

def Clear():
  peice.clearstamps()

def Clicked(x, y):
  global clickCount
  global menu_image
  global move
  global board
  if menu_image == "./mainMenu.gif":  #buttons for main menu
    if (x > -397.0 and x < 364.0 and y > -186.0 and y < -116.0):
      menu_image = "./playOpt.gif"
      wn.addshape(menu_image)
      background.shape(menu_image)
    if (x > -401.0 and x < 50.0 and y > -303.0 and y < -230.0):
      menu_image = "./directions.gif"
      wn.addshape(menu_image)
      background.shape(menu_image)
    if (x > 94.0 and x < 370.0 and y > -302.0 and y < -230.0):
      print("hi")
      menu_image = "./cred.gif"
      wn.addshape(menu_image)
      background.shape(menu_image)

  elif menu_image == "./playOpt.gif":  #buttons for play options
    if (x > -199.0 and x < -37.0 and y > -216.0 and y < -141.0):
      print("pvp")
      menu_image = "./gameScreen.gif"
      wn.addshape(menu_image)
      background.shape(menu_image)
      brdTrt.showturtle()
      Clear()
      x = 0
      y = 0
      
    if (x > 4.0 and x < 169.0 and y > -218.0 and y < -141.0):
      print("pvc")

  if (x > -601.0 and x < -392.0 and y > 249.0 and y < 320.0):
    menu_image = "./mainMenu.gif"
    clickCount=0
    wn.addshape(menu_image)
    background.shape(menu_image)
    brdTrt.hideturtle()
    board = [
      ["-", "-", "-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-", "-", "-"],
    ]
    peice.clearstamps()
    message.clear()

  print(x, y)
  print(move)

def moveInput(x):
  global move
  if (x > -354.0 and x < -284.0):
    move = 1
  elif (x > -248.0 and x < -178.0):
    move = 2
  elif (x > -142.0 and x < -72.0):
    move = 3
  elif (x > -36.0 and x < 35.0):
    move = 4
  elif (x > 71.0 and x < 141.0):
    move = 5
  elif (x > 175.0 and x < 248.0):
    move = 6
  elif (x > 284.0 and x < 354.0):
    move = 7
  else:
    move = 0


#vars
currentPlayer = "Red"

win = False

#- = blank
#x = red
#o = blue

board = [
  ["-", "-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-", "-", "-"],
]

#defs


def checkForWins():
  global win
  for word in ["xxxx", "oooo"]:  #pulls word to search for
    for row in range(len(board)):  #imagin a pointer combing through every row and column of the word search.
      for column in range(len(board[row])):
        for scanDirection in [
          [1, 0, "down"], [-1, 0, "up"], [0, 1, "right"], [0, -1, "left"],
          [1, 1, "right down"], [-1, -1, "left up"], [1, -1, "left down"],
          [-1, 1, "right up"]
        ]:  #the scan direction is the direction that the word is going
          checksum = 0  #the checksum should equal the word length. if it does then the word was found.
          for i in range(len(word)):
            if (row + (i * scanDirection[0])) < 0 or (row + (i * scanDirection[0])) > (len(board) - 1) or (column + (i * scanDirection[1])) < 0 or (column + (i * scanDirection[1])) > (len(board[row])-1):  #makes sure the scanner doesn't go out of bounds
              pass
            elif word[i].lower() == board[row + (i * scanDirection[0])][
                column +
              (i*scanDirection[1])].lower():  #each letter is thouroughly checked
              checksum += 1
          if checksum == len(word):
            win = True  #makes a list of where the words are

  return (win)


def makeAMove(x, y):
  checksum = 0
  global move
  global currentPlayer
  gravity = 5

  while True:  #loop makes sure input is valid
    moveInput(x)
    if move in [1, 2, 3, 4, 5, 6, 7]:
      if board[0][move - 1] in ["x", "o"]:  #disallows putting peice in full column
        break
      else:
        while board[gravity][move - 1] in ["x","o"]:  #simulates gravity of peice
          gravity -= 1
        message.color(currentPlayer)
        message.write(f"{currentPlayer} Player's Turn", align="center", font=("Times", 16, "normal"))
        if currentPlayer == "Red":
          currentPlayer = "Blue"
        else:
          currentPlayer = "Red"
        
        if currentPlayer == "Red":  #swaps who the player is so they can make turns
          board[gravity][move - 1] = "x"

          peice.color("Red")
          peice.penup()
          peice.goto(-320 + (106 * (move - 1)), 194 - (77 * gravity))
          peice.showturtle()
          peice.stamp()
          peice.hideturtle()
        else:
          board[gravity][move - 1] = "o"

          peice.color("Blue")
          peice.penup()
          peice.goto(-320 + (106 * (move - 1)), 194 - (77 * gravity))
          peice.showturtle()
          peice.stamp()
          peice.hideturtle()

        break

    else:
      break


#main operation
def mainProccess(x, y):
  global board
  global win
  global clickCount

  Clicked(x, y)
  if (menu_image == "./gameScreen.gif"):
    if checkForWins() == False:
      message.clear()
      clickCount=clickCount+1
      if clickCount>1:
        makeAMove(x, y)
    else:
      message.clear()
      message.color(currentPlayer)
      message.write(f"{currentPlayer} Player Wins!", align="center", font=("Times", 16, "normal"))
      board = [
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-"],
      ]
      ###CLEAR BOARD AFTER WINS
      peice.clearstamps()
      win = False


wn.onscreenclick(mainProccess)
wn.mainloop()
