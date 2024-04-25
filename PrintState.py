import numpy as np
import pygame
from Graphics import Graphics
from constant import *
from State import State
from Pardox import Pardox
import time
from Human_Agent import Human_Agent

FPS = 60
win = pygame.display.set_mode((800, 700))

class PrintState:
    def __init__(self, state : State) -> None:
        self.state = state

    def Print(self):
        FPS = 60
        win = pygame.display.set_mode((800, 700))
        graphics = Graphics(win)
        clock = pygame.time.Clock()
    #graphics.draw(state)
        player1 = Human_Agent(None, player=1)
        graphics.draw(self.state, player1)
        pygame.display.update()
        time.sleep(5)

        
row1 = [100, 100, 100 , -1 , -1 ,  1  , 1 , -1  ,-1   ,1  , 1 ,100, 100, 100]
row2 = [100, 100,   1 ,  1 ,  0  , 0  , 0  , 0 , -1 , -1  , 0  , 0 ,100 ,100]
row3 = [100,  -1 , -1 ,  0 ,  0  , 0  , 0  , -1 ,  -1 , -1 , -1 ,  0  , 0, 100]
row4 = [1 ,  1 ,  0 ,  0 ,  0 ,  0 , -1 , -1 ,  -1 ,  -1 ,  -1 ,  -1  ,0 ,  0]
row5 = [100,  -1 , -1  , 0  , 0 ,  0 ,  0  , 0   ,0 ,  -1  , -1 , -1 , -1 ,100]
row6 = [100, 100,   1 ,  1,  -1 , -1  , 0 ,  0 , -1 , -1 ,  1,   1 ,100 ,100]
row7 = [100 ,100 ,100  , 0 ,  0 ,  0  , 0   ,0  , 0  , 0  , 0, 100 ,100,100]



board = np.array([row1, row2, row3, row4, row5, row6, row7])
state = State(board)

environment = Pardox()
environment.state = state
print(state.score(environment, state))
try1 = PrintState(state)
try1.Print()
