import random
def minimaxAgentAction(agent, gameState):
    legalMoves = gameState.getLegalActions()
    return random.choice(legalMoves)