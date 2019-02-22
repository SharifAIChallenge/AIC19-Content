import random
def alphaBetaAgentAction(agent, gameState):
    legalMoves = gameState.getLegalActions()
    return random.choice(legalMoves)