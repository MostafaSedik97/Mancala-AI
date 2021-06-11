def movePlay(stones, currentPit, Player, steal):

    movingStones = stones[currentPit]
    stones[currentPit] = 0

    if int(movingStones) == 0:
      print(currentPit)
      print("You chose an empty pit! Please choose a non-empty pit\n")
      return stones, Player

    #Moving player's or AI's stones

    nextPit = currentPit + 1
    for i in range(int(movingStones)):
      if Player == True and int(nextPit) == 13:
        nextPit = 0
      elif Player == False and int(nextPit) == 6:
        nextPit = 7
      stones[nextPit] = int(stones[nextPit]) + 1
      movingStones = int(movingStones) - 1
      if int(movingStones) == 0:
        lastPit = nextPit
      else:
        nextPit = int(nextPit) + 1
        if int(nextPit) > 13:
          nextPit = 0

    if Player == True and int(lastPit) == 6:
      Player = True
    elif steal == True and int(stones[lastPit]) == 1 and int(lastPit) < 6 and Player:
      stones[6] = int(stones[6]) + int(stones[12 - int(lastPit)]) + 1
      stones[lastPit] = 0
      stones[12 - int(lastPit)] = 0
      Player = not Player
    elif Player == False and int(lastPit) == 13:
      Player = False
    elif steal == True and int(stones[lastPit]) == 1 and int(lastPit) > 6 and not Player:
      stones[13] = int(stones[13]) + int(stones[12 - int(lastPit)]) + 1
      stones[lastPit] = 0
      stones[12 - int(lastPit)] = 0
      Player = not Player
    else:
      Player = not Player

    ####

    return stones, Player