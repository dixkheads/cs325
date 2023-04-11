# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
#
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Harry He


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        # print("newPos = ", newPos)
        # print("newFood = ", newFood)
        # print("newGhostStates = ", newGhostStates)
        # print("newScaredTimes = ", newScaredTimes)

        score = 3 / (len(newFood.asList()) + 1)
        minFoodDist = 999999
        for food in newFood.asList():
            dist = manhattanDistance(food, newPos) / 1.9
            minFoodDist = min(minFoodDist, dist)

        score += 1 / (minFoodDist + 100)

        for ghost in newGhostStates:
            dist = manhattanDistance(newPos, ghost.getPosition())
            if 0 < dist < ghost.scaredTimer:
                score += (1 / (1 + dist))
            elif dist < 4:
                score -= dist / 20

        return score

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        # lastGhost = gameState.getNumAgents() - 1
        # def minVal(state, depth, ghost):
        #     if state.isWin() or state.isLose() or depth == self.depth:
        #         return self.evaluationFunction(state)
        #     else:
        #         result = 9999999
        #         for action in state.getLegalActions(ghost):
        #             if ghost == lastGhost:
        #                 result = min(result, maxVal(state.generateSuccessor(ghost, action), depth + 1))
        #             else:
        #                 result = min(result, minVal(state.generateSuccessor(ghost, action), depth, ghost + 1))
        #         return result
        #
        # def maxVal(state, depth):
        #     if state.isWin() or state.isLose() or depth == self.depth:
        #         return self.evaluationFunction(state)
        #     else:
        #         result = -9999999
        #         for action in state.getLegalActions(0):
        #             result = max(result, minVal(state.generateSuccessor(0, action), depth, 1))
        #
        #         return result
        #
        # max_act = None
        # result = -9999999
        # for action in gameState.getLegalActions(0):
        #     if minVal(gameState.generateSuccessor(0, action), 0, 1) > result:
        #         max_act = action
        #         result = minVal(gameState.generateSuccessor(0, action), 0, 1)
        #
        # return max_act
        lastGhost = gameState.getNumAgents() - 1

        def minVal(state, depth, ghost):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), None
            else:
                result = 9999999
                fin_action = None
                for action in state.getLegalActions(ghost):
                    if ghost == lastGhost:
                        temp_res, temp_act = maxVal(state.generateSuccessor(ghost, action), depth + 1)
                        if temp_res < result:
                            result = temp_res
                            fin_action = action
                    else:
                        temp_res, temp_act = minVal(state.generateSuccessor(ghost, action), depth, ghost + 1)
                        if temp_res < result:
                            result = temp_res
                            fin_action = action

                return result, fin_action

        def maxVal(state, depth):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), None
            else:
                result = -9999999
                fin_action = None
                for action in state.getLegalActions(0):
                    temp_res, temp_act = minVal(state.generateSuccessor(0, action), depth, 1)
                    if temp_res > result:
                        result = temp_res
                        fin_action = action

                return result, fin_action

        res_result, res_act = maxVal(gameState, 0)
        return res_act



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        lastGhost = gameState.getNumAgents() - 1
        def minVal(state, depth, ghost, alpha, beta):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), None
            else:
                result = 9999999
                fin_action = None
                for action in state.getLegalActions(ghost):
                    if ghost == lastGhost:
                        temp_res, temp_act = maxVal(state.generateSuccessor(ghost, action), depth + 1, alpha, beta)
                        if temp_res < result:
                            result = temp_res
                            fin_action = action
                    else:
                        temp_res, temp_act = minVal(state.generateSuccessor(ghost, action), depth, ghost + 1, alpha, beta)
                        if temp_res < result:
                            result = temp_res
                            fin_action = action
                    if result < alpha:
                        return result, fin_action
                    beta = min(beta, result)
                return result, fin_action

        def maxVal(state, depth, alpha, beta):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), None
            else:
                result = -9999999
                fin_action = None
                for action in state.getLegalActions(0):
                    temp_res, temp_act = minVal(state.generateSuccessor(0, action), depth, 1, alpha, beta)
                    if temp_res > result:
                        result = temp_res
                        fin_action = action
                    if result > beta:
                        return result, fin_action
                    alpha = max(alpha, result)

                return result, fin_action

        res_result, res_act = maxVal(gameState, 0, -9999999, 9999999)
        return res_act

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        lastGhost = gameState.getNumAgents() - 1

        def ExpectVal(state, depth, ghost):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), None
            else:
                result = 0
                fin_action = None
                for action in state.getLegalActions(ghost):
                    if ghost == lastGhost:
                        temp_res, temp_act = maxVal(state.generateSuccessor(ghost, action), depth + 1)
                        result += temp_res / len(state.getLegalActions(ghost))
                        fin_action = action
                    else:
                        temp_res, temp_act = ExpectVal(state.generateSuccessor(ghost, action), depth, ghost + 1)
                        result += temp_res / len(state.getLegalActions(ghost))
                        fin_action = action

                return result, fin_action

        def maxVal(state, depth):
            if state.isWin() or state.isLose() or depth == self.depth:
                return self.evaluationFunction(state), None
            else:
                result = -9999999
                fin_action = None
                for action in state.getLegalActions(0):
                    temp_res, temp_act = ExpectVal(state.generateSuccessor(0, action), depth, 1)
                    if temp_res > result:
                        result = temp_res
                        fin_action = action

                return result, fin_action

        res_result, res_act = maxVal(gameState, 0)
        return res_act


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: Evaluate the score based on 5 factors, the closest food and ghost, the total distance
    between ghosts and food, and the total number of food
    """
    "*** YOUR CODE HERE ***"

    # util.raiseNotDefined()
    def getClosesetFood():
        foodPos = currentGameState.getFood().asList()
        PacmanPos = currentGameState.getPacmanPosition()
        closest = 9999999
        for food in foodPos:
            closest = min(manhattanDistance(food, PacmanPos), closest)
        return closest

    def getAllFood():
        foodPos = currentGameState.getFood().asList()
        PacmanPos = currentGameState.getPacmanPosition()
        sum = 0
        for food in foodPos:
            sum += manhattanDistance(food, PacmanPos)
            PacmanPos = food
        return sum

    def getClosestGhost():
        GhostPos = currentGameState.getGhostPositions()
        PacmanPos = currentGameState.getPacmanPosition()
        closest = 9999999
        for ghost in GhostPos:
            closest = min(manhattanDistance(ghost, PacmanPos), closest)
        return closest

    def getAllGhost():
        GhostPos = currentGameState.getGhostPositions()
        PacmanPos = currentGameState.getPacmanPosition()
        sum = 0
        for ghost in GhostPos:
            sum += 1 / manhattanDistance(ghost, PacmanPos)
        # print("sum = ", sum)
        return sum

    facClosestFood, facAllFood, facClosestGhost, facAllGhost, facFoodNum = -50, -1, 2, 0, -2000
    if getClosestGhost() < 3:
        return -9999999
    elif len(currentGameState.getFood().asList()) == 0:
        return 9999999
    else:
        return getClosesetFood() * facClosestFood + getAllFood() * facAllFood + getClosestGhost() * facClosestGhost + getAllGhost() * facAllGhost + facFoodNum * len(currentGameState.getFood().asList())


# Abbreviation
better = betterEvaluationFunction
