
import os
from move import movePlay 
from node import node , ABPruning 

print("")
print("    | "+ "\t" +" | "+ "\t" +" | "+ "\t" +" | "+ "\t" +" | "+ "\t" +" | "+ "\t" +" |    ")
print("")
print(" "+ "\t" +" | \t Welcome To Mancala!     | "+ "\t" +" ")
print("")
print("    | "+ "\t" +" | "+ "\t" +" | "+ "\t" +" | "+ "\t" +" | "+ "\t" +" | "+ "\t" +" |    ")
print("")
print("")

def drawBoard(stones):

  for i in range(len(stones)):
    stones[i] = int(stones[i])
    if stones[i] < 10:
      stones[i] = " " + str(stones[i])
    else:
      stones[i] = str(stones[i])

  print("")
  print("    | "+ stones[12] +" | "+ stones[11] +" | "+ stones[10] +" | "+ stones[9] +" | "+ stones[8] +" | "+ stones[7] +" |    ")
  print("")
  print(" "+ stones[13] +" |                             | "+ stones[6] +" ")
  print("")
  print("    | "+ stones[0] +" | "+ stones[1] +" | "+ stones[2] +" | "+ stones[3] +" | "+ stones[4] +" | "+ stones[5] +" |    ")
  print("")
  print("       a    b    c    d    e    f")
  print("")

mini = -1000
maxi = 1000
Minimizing = False
Maximizing = True

In_Game = True

earlyQuit = False

mode = ""

steal = True

movingStones = 0

currentPit = 0

lastPit = 0

stones = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

while(In_Game):
  if (os.path.isfile('SavedGame.txt')):
      playerInput = input("Press y to play first or n to play second or q to exit or l to load game: ")
  
  else:  
      playerInput = input("Press y to play first or n to play second or q to exit: ")
  print("")

  if playerInput == "y":
    Player = True
    break
  elif playerInput == "n":
    Player = False
    break
  elif playerInput == "q":
    earlyQuit = True
    break
  elif playerInput=="l" and os.path.isfile('SavedGame.txt'):
    f=open('SavedGame.txt')
    lines=f.readlines()
    stones=lines[0].split()
    mode = lines[1].replace('\n','')
    stealS=lines[2]
    depth = int(lines[3])
    if stealS == "yes":
      steal = True
    elif stealS == "no":
      steal = False
    f.close()
    Player = True
    break

  else:
    print("Wrong input!\n")

if earlyQuit == False and playerInput != "l":
  while(In_Game):
    playerInput = input("Press e for easy difficulty or m for medium difficulty or h for hard difficulty or q to quit: ")
    print("")

    
    if playerInput == "e":
      mode = "Easy"
      depth = 4
      break
    elif playerInput == "m":
      mode = "Medium"
      depth = 6
      break
    elif playerInput == "h":
      mode = "Hard"
      depth = 8
      break
    elif playerInput == "q":
      earlyQuit = True
      break
    else:
      print("Wrong input!\n")

if earlyQuit == False and playerInput != "l":
  while(In_Game):
    playerInput = input("Press y for steal mode or n for non-steal mode or q to quit: ")
    print("")

    if playerInput == "y":
      steal = True
      break
    elif playerInput == "n":
      steal = False 
      break
    elif playerInput == "q":
      earlyQuit = True
      break
    else:
      print("Wrong input!\n")

while(In_Game):

  if earlyQuit == True:
    input("Thank you.")
    break

  if Player == True:
    print("Your turn.")
  elif Player == False:
    print("AI's turn.")

  drawBoard(stones)

  if Player == True:

    #Player's turn

    quit = False
    playerInput = input("Input any non-empty pit from a to f,input s to save game, input q to exit: ")
    print("")
    if playerInput == "q":
      input("Thank you for playing.")
      break
    elif playerInput == "a":
      currentPit = 0
    elif playerInput == "b":
      currentPit = 1
    elif playerInput == "c":
      currentPit = 2
    elif playerInput == "d":
      currentPit = 3
    elif playerInput == "e":
      currentPit = 4
    elif playerInput == "f":
      currentPit = 5
    elif playerInput == 's':
        f=open ("SavedGame.txt",'w')
        for i in stones:    
            f.write(i)
        f.write('\n')
        f.write(mode)
        f.write('\n')
        if steal == True:
          stealS = "yes"
        elif steal == False:
          stealS = "no"
        f.write(stealS)
        f.write('\n')
        f.write(str(depth))
        f.close()
        input("Thank you for playing.")
        break
    else:
      print("Invalid input. Inputs allowed: from a to f, input q to exit\n")
      continue

    stones, Player = movePlay(stones, currentPit, Player, steal)

    ####End of player's turn

  elif Player == False:

    #AI's turn

    state = node(depth, stones, mode=mode, steal=steal)
    value,currentPit = ABPruning(state, depth, -1000, 1000, Maximizing)
    #print(depth)
    #print(currentPit)
    stones, Player = movePlay(stones, currentPit, Player, steal)

    ####End of AI's turn

  #Check for game ending

  playerStones = 0
  AIStones = 0

  for i in range(6):
    playerStones = int(playerStones) + int(stones[i])
    AIStones = int(AIStones) + int(stones[12 - i])
  if int(playerStones) == 0 or int(AIStones) == 0:
    stones[6] = int(stones[6]) + int(playerStones)
    stones[13] = int(stones[13]) + int(AIStones)
    for i in range(6):
      stones[i] = 0
      stones[12 - i] = 0
    drawBoard(stones)
    if stones[6] > stones[13]:
      input("You won!")
    elif stones[13] > stones[6]:
      input("AI won!")
    elif stones[6] == stones[13]:
      input("A tie!")
    break
  
  ####End of check


