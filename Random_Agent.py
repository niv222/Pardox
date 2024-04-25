import random
from Pardox import Pardox
from Graphics import *
from State import State


class Random_Agent():
    def __init__(self, env : Pardox, player = None) -> None:
        self.player = player
        self.env = env

        

    def get_Action (self, graphics : Graphics = None, state: State = None ,events = None, train = True):
        if state.player == None or state.player != 1:
            state.player = -1

        legal_actions = self.env.get_legal_actions(state)

        if legal_actions == None:
            print(f'state: {state.board}')
            print(f'player: {state.player}')

        return random.choice(legal_actions)