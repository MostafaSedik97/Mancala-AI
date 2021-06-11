def evaluateFn(stones, player, mode = "Hard", steal = True):
  value = 0

  #Alternative difficulty
  if mode == "Easy":
    if int(stones[6]) >= int(stones[13]):
        return -(int(stones[6]) - int(stones[13]))
    elif int(stones[13]) > int(stones[6]):
        return (int(stones[13]) - int(stones[6]))

  #check law da a5er el le3ba 5ales
  playerStones = 0
  AIStones = 0
  for i in range(6):
    playerStones = int(playerStones) + int(stones[i])
    AIStones = int(AIStones) + int(stones[12 - i])

  if int(playerStones) == 0 or int(AIStones) == 0:
    playState = stones.copy()
    playState[6] = int(playState[6]) + int(playerStones)
    playState[13] = int(playState[13]) + int(AIStones)
    if playState[6] > playState[13]:
      return -6 - (playState[6] - playState[13])
    elif playState[13] > playState[6]:
      return 6 + (playState[13] - playState[6])
    elif playState[6] == playState[13]:
      return 0

  if player == True:

    #bazawed far2 el scores
    if int(stones[6]) > int(stones[13]):
        value = value - (int(stones[6]) - int(stones[13]))
    elif int(stones[13]) > int(stones[6]):
        value = value + (int(stones[13]) - int(stones[6]))

    for i in range(6):
      #check law feh 5atwa t5aleny al3b tany
      if i + int(stones[i]) == 6:
        value = value - 1

      #check law 3andy 0 we feh ay stones ablaha te5las feha we elle 2osadha akbar men 0
      if steal == True and int(stones[i]) == 0 and int(stones[12 - i]) > 0:
        for j in range(i):
          if int(stones[j]) == i - j:
            value = value - 1

      #check law 3and el 5esm 0s we fe stones 3andy te2felhalo
      if steal == True and int(stones[12 - i]) == 0:
        for j in range(i):
          if int(stones[j]) >= 12 - i - j:
            value = value - 1

  elif player == False:

    #bazawed far2 el scores
    if int(stones[6]) > int(stones[13]):
        value = value - (int(stones[6]) - int(stones[13]))
    elif int(stones[13]) > int(stones[6]):
        value = value + (int(stones[13]) - int(stones[6]))

    for i in range(6):
      #check law feh 5atwa t5aleny al3b tany
      if 12 - i + int(stones[12 - i]) == 13:
        value = value + 1

      #check law 3andy 0 we feh ay stones ablaha te5las feha we elle 2osadha akbar men 0
      if steal == True and int(stones[12 - i]) == 0 and int(stones[i]) > 0:
        for j in range(7, 12 - i):
          if int(stones[j]) == 12 - i - j:
            value = value + 1
      
      #check law 3and el 5esm 0s we fe stones 3andy te2felhalo           
      if steal == True and int(stones[i]) == 0:
        for j in range(7, 12 - i):
          if int(stones[j]) >= 12 - i - j + 1:
            value = value + 1
  return value