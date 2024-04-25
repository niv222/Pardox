from State import State
from Pardox import Pardox
from constant import *
from Graphics import *
import random
MAXSCORE = 1000

class AlphaBeta_Agent:

    def __init__(self, player, depth = 2, environment: Pardox = None):
        self.player = player
        if player == 2:
            self.player = -1
        self.depth = depth
        self.environment : Pardox = environment



    def get_Action(self, events= None, state : State= None , graphics : Graphics = None, train = False):
        reached = set()
        value, bestAction = self.minMax(state, reached)

        return bestAction



    def evaluate (self, gameState : State):
        # player_score, opponent_score = gameState.score(player = self.player)
        # score =  player_score - opponent_score 
        score = 0
        if self.environment.is_end_of_game(gameState):
            if self.environment.Winner:
                if self.environment.Winner == self.player:
                    score += 1000
                    self.environment.Winner = 0
                elif self.environment.Winner == self.player * -1:
                    score -= 1000
                    self.environment.Winner = 0


        legal_action = 0
        tripels = 0
        Rows, Cols =  np.where(gameState.board == self.player)
        positons = tuple(zip(Rows, Cols))[0::2]

        for pos in positons:
            pairs = self.environment.get_pairs(pos, gameState)
            tripels = self.environment.get_triples(gameState, pos) + tripels
            legal_action = legal_action + len(pairs)

        score += legal_action *  5
        score += tripels * 8

        legal_action = 0
        tripels = 0
        Rows, Cols =  np.where(gameState.board == self.player * -1) #enemy
        positons = tuple(zip(Rows, Cols))[0::2]

        for pos in positons:
            pairs = self.environment.get_pairs(pos, gameState)
            tripels = self.environment.get_triples(gameState, pos) + tripels
            legal_action = legal_action + len(pairs)


        score -= legal_action *  5
        score -= tripels *  8



        #print(f'pairs: {len(legal_action)} player : {self.player}')


        #score = random.randint(-1000, 1000)
        #print(f'score : {score}')

        return score


    def minMax(self, state:State, visited:set):
        depth = 0
        alpha = -MAXSCORE
        beta = MAXSCORE
        return self.max_value(state, visited, depth, alpha, beta)
        
    def max_value (self, state:State, visited:set, depth, alpha, beta):
        
        value = -MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_end_of_game(state):
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(action, state)
            if newState not in visited:
                newState.player = self.player
                visited.add(newState)
                newValue, newAction = self.min_value(newState, visited,  depth + 1, alpha, beta)
                if newValue > value:
                    value = newValue
                    bestAction = action
                    alpha = max(alpha, value)
                if value >= beta:
                    return value, bestAction
                    
        if bestAction == None:
            bestAction = random.choice(legal_actions)


        return value, bestAction 

    def min_value (self, state:State, visited:set, depth, alpha, beta):
        
        value = MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_end_of_game(state):
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(action, state)
            if newState not in visited:
                visited.add(newState)
                newValue, newAction = self.max_value(newState, visited,  depth + 1, alpha, beta)
                if newValue < value:
                    value = newValue
                    bestAction = action
                    beta = min(beta, value)
                if value <= alpha:
                    return value, bestAction

        return value, bestAction    




