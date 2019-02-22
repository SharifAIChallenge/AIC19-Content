import random
def reflexAgentAction(self, gameState):
    legalMoves = gameState.getLegalActions()
    return random.choice(legalMoves)