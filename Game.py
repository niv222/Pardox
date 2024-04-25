import numpy as np
import pygame
from Graphics import Graphics
from constant import *
from State import State
from Human_Agent import Human_Agent
from Random_Agent import Random_Agent
from Pardox import Pardox
from MinMax_Agent import MinMaxAgent
from DQN_Agent import DQN_Agent
from AlphaBeta_Agent import AlphaBeta_Agent
from DQN_Agent import DQN_Agent

my_turn = True
FPS = 60
win = pygame.display.set_mode((800, 700))

row1 = [-100, -100, -100, 1, 1, -1, -1, 1, 1, -1, -1, -100, -100, -100]
row2 = [-100, -100, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, -100, -100]
row3 = [-100, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -100]
row4 = [-1, -1, 0, 0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1]
row5 = [-100, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -100]
row6 = [-100, -100, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, -100, -100]
row7 = [-100, -100, -100, 1, 1, -1, -1, 1, 1, -1, -1, -100, -100, -100]


board = np.array([row1, row2, row3, row4, row5, row6, row7])
state = State(board)

environment = Pardox()
pygame.display.set_caption('Pardox')
pygame.font.init()
    
player1 = Human_Agent(environment, player=1)
#player1 = Random_Agent(environment, player=1)
#player1 = MinMaxAgent(environment=environment, player=1)
#player1 = AlphaBeta_Agent(environment=environment, player=1)
#player1 = DQN_Agent(env= environment, player = 1, parametes_path=f'Data/params_3.pth')

player2 = Human_Agent(environment, player=-1)
#player2 = Random_Agent(environment, player=-1)
#player2 = MinMaxAgent(environment=environment, player=-1)
#player2 = AlphaBeta_Agent(environment=environment, player= -1)
#player2 = DQN_Agent(env= environment, player = -1, parametes_path=f'Data/params_600.pth')



def main ():
    player = player1
    state.player = 1
    environment.state.player = 1
    #puzzle.shuffle(iteration=70)

    graphics = Graphics(win)
    #agent = Human_Agent()
    run = True
    clock = pygame.time.Clock()
    #graphics.draw(state)
    pygame.display.update()
    

    while(run):
        clock.tick(FPS)
        graphics.draw(environment.state, player)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False

        action = player.get_Action(events=events, state=environment.state, graphics=graphics)
        if action:
            environment.move(environment.state, action)
            print(environment.state.board)
            graphics.draw(environment.state, player)
            pygame.display.update()
            if player == player1:
                player = player2
                environment.state.player = -1
                state.player = -1
            else:
                player = player1
                state.player = 1
                environment.state.player = 1
        
        if environment.is_end_of_game(environment.state):
            print(environment.state.score(environment, environment.state))
            run = False
            print(f'Congrats player {environment.Winner} has won')
            
        #time.sleep(0.7)
        
        graphics.draw(environment.state, player)
        
        
        pygame.display.update()


    pygame.quit()

    
def switch_players(player):
    pass
    

if __name__ == '__main__':
    main()
