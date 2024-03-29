# search.py
# ---------
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

"""THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
A TUTOR OR CODE WRITTEN BY OTHER STUDENTS
- Harry He"""


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions

    #util.raiseNotDefined()
    stack = []
    isVisited = set()
    PathMap = {}
    #stack.append(curr)
    End = None
    for i in problem.getSuccessors(problem.getStartState()):
        stack.append(i)
        PathMap[i] = None
    while stack:
        curr = stack.pop()
        if problem.isGoalState(curr[0]):
            End = curr
            Path = []
            while End is not None:
                Path.append(End[1])
                End = PathMap[End]
            Path.reverse()
            return Path
        if curr[0] in isVisited: continue
        isVisited.add(curr[0])
        for i in problem.getSuccessors(curr[0]):
            PathMap[i] = curr
            stack.append(i)
    return None




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    queue = []
    isVisited = set()
    PathMap = {}
    # stack.append(curr)
    End = None
    isVisited.add(problem.getStartState())
    for i in problem.getSuccessors(problem.getStartState()):
        queue.append(i)
        isVisited.add(i[0])
        PathMap[i] = None
    while queue:
        curr = queue.pop(0)
        if problem.isGoalState(curr[0]):
            End = curr
            Path = []
            while End is not None:
                Path.append(End[1])
                End = PathMap[End]
            Path.reverse()
            return Path
        for i in problem.getSuccessors(curr[0]):
            if i[0] in isVisited: continue
            isVisited.add(i[0])
            PathMap[i] = curr
            queue.append(i)
    return None


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()


    from queue import PriorityQueue

    queue = PriorityQueue()
    isVisited = {}
    PathMap = {}
    # stack.append(curr)
    End = None
    isVisited[problem.getStartState()] = 0
    ShitIndex = 0
    for i in problem.getSuccessors(problem.getStartState()):
        queue.put((i[2], ShitIndex, i))
        ShitIndex += 1
        isVisited[i[0]] = i[2]
        PathMap[i] = None
    while queue:
        cost, temp, curr = queue.get()
        if problem.isGoalState(curr[0]):
            End = curr
            Path = []
            while End is not None:
                Path.append(End[1])
                End = PathMap[End]
            Path.reverse()
            return Path
        for i in problem.getSuccessors(curr[0]):
            ncost = cost + i[2]
            if i[0] not in isVisited and i not in queue.queue:
                isVisited[i[0]] = ncost
                PathMap[i] = curr
                queue.put((ncost, ShitIndex, i))
                ShitIndex += 1
            elif ncost < isVisited[i[0]]:
                isVisited[i[0]] = ncost
                PathMap[i] = curr
                queue.put((ncost, ShitIndex, i))
                ShitIndex += 1
    return None




def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    from queue import PriorityQueue

    queue = PriorityQueue()
    isVisited = {}
    PathMap = {}
    # stack.append(curr)
    End = None
    isVisited[problem.getStartState()] = 0
    ShitIndex = 0
    for i in problem.getSuccessors(problem.getStartState()):
        queue.put((i[2] + heuristic(i[0], problem), ShitIndex, i))
        ShitIndex += 1
        isVisited[i[0]] = i[2]
        PathMap[i] = None
    while queue:
        cost, temp, curr = queue.get()
        if problem.isGoalState(curr[0]):
            End = curr
            Path = []
            while End is not None:
                Path.append(End[1])
                End = PathMap[End]
            Path.reverse()
            return Path
        for i in problem.getSuccessors(curr[0]):
            ncost = isVisited[curr[0]] + i[2]
            if i[0] not in isVisited and i not in queue.queue:
                isVisited[i[0]] = ncost
                PathMap[i] = curr
                queue.put((ncost + heuristic(i[0], problem), ShitIndex, i))
                ShitIndex += 1
            elif ncost < isVisited[i[0]]:
                isVisited[i[0]] = ncost
                PathMap[i] = curr
                queue.put((ncost + heuristic(i[0], problem), ShitIndex, i))
                ShitIndex += 1
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
