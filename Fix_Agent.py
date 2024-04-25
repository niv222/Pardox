import numpy as np
from Pardox import Pardox
from State import State
import random


class Fix_Agent:
    def __init__(self, env: Pardox, player = 1, train = False, random = 0.10) -> None:
        self.env  = env
        self.player = player
        self.train = train
        self.random = random

    def value(self, state: State): 
        return state.score(self.env, state)
        
    def get_Action (self, events = None, graphics=None, state: State = None, epoch = 0, train = True):
        legal_actions = self.env.get_legal_actions(state)
        if self.train and train and random.random() < self.random:
             return random.choice(legal_actions)
        next_states, _ = self.env.get_all_next_states(state)
        values = []
        for next_state in next_states:
                values.append(self.value(next_state))
        if self.player == 1:
            maxIndex = values.index(max(values))
            return legal_actions[maxIndex]
        else:
            minIndex = values.index(min(values))
            return legal_actions[minIndex]

    