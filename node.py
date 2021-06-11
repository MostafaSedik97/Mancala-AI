from move import movePlay
from evalute import evaluateFn
class node:

    def __init__(self, depth, state, mode, steal, player = False, i = 100):
      self.depth = depth
      self.nodes = []
      self.currentPit = i 
      self.player = player
      self.state=state
      self.value=100
      self.mode=mode
      self.steal = steal
      self.createLeafs()

    def createLeafs (self):
        if self.depth != 0 and not (all(int (s)==0 for s in self.state)):
              for i in range (6):
                if self.player== True:
                  if not (int(self.state[i])==0):
                    playState = self.state.copy()
                    nextState, changePlayer = movePlay(playState, i, self.player, self.steal)
                    self.nodes.append(node(self.depth-1, nextState, self.mode, self.steal, changePlayer, i))
                elif self.player == False:
                  if not (int(self.state[12-i])==0):
                    playState = self.state.copy()
                    nextState, changePlayer = movePlay(playState, 12-i, self.player, self.steal)
                    self.nodes.append(node(self.depth-1, nextState, self.mode, self.steal, changePlayer, 12-i))
          
        else:
            self.value = evaluateFn(self.state, self.player, self.mode, self.steal)
        

mini = -1000
maxi = 1000
Minimizing = False
Maximizing = True

def ABPruning(node, depth, alpha, beta, playerType):
  currentPit = -1
  if depth == 0 or len(node.nodes) == 0 :
    return node.value, node.currentPit
  if playerType is Maximizing:
    maxEva = mini
    for i in node.nodes:
      ev,index = ABPruning(i, node.depth-1, alpha, beta, not playerType)
      if (maxEva < ev):
        currentPit = i.currentPit
        maxEva = ev 
      alpha = max(alpha, maxEva)      
      if beta <= alpha: 
        break  
    return maxEva,currentPit
  elif playerType is Minimizing:
    minEva = maxi   
    for i in node.nodes: 
      ev,index = ABPruning(i, node.depth-1, alpha, beta, not playerType)  
      if (minEva > ev):
        currentPit = i.currentPit
        minEva = ev  
      beta = min(beta, minEva)  
      if beta <= alpha:  
        break          
    return minEva , currentPit


