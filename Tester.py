from Random_Agent import Random_Agent
from Pardox import Pardox
import numpy as np
from State import State
from DQN_Agent import DQN_Agent
from MinMax_Agent import MinMaxAgent
from AlphaBeta_Agent import AlphaBeta_Agent
from DQN_Agent import DQN_Agent
from Human_Agent import Human_Agent

class Tester:
    def __init__(self, env : Pardox, player1, player2) -> None:
        self.env = env
        self.player1 = player1
        #self.player1.player = -1
        self.player2 = player2
        #self.player2.player = 1
        

    def test (self, games_num):
        env = self.env
        player = self.player1
        player1_win = 0
        player2_win = 0
        games = 0
        max_step = 1000
        step = 0
        while games < games_num:
            env.state.player = player.player
            action = player.get_Action(state = env.state, train = False)
            env.move(env.state, action)
            step += 1
            player = self.switchPlayers(player)
            print(games,end="\r")
            #print(player.player)
            if env.is_end_of_game(env.state) or step > max_step:
                score = env.state.score(self.env, self.env.state)
                if score == self.player1.player:
                    player1_win += 1

                elif score == self.player2.player:
                    player2_win += 1


                env.state = env.get_init_state()
                games += 1
                player = self.player1
                step = 0

            
        return player1_win, player2_win        

    def switchPlayers(self, player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def __call__(self, games_num):
        return self.test(games_num)

if __name__ == '__main__':
    row1 = [-100, -100, -100, 1, 1, -1, -1, 1, 1, -1, -1, -100, -100, -100]
    row2 = [-100, -100, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, -100, -100]
    row3 = [-100, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -100]
    row4 = [-1, -1, 0, 0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1]
    row5 = [-100, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -100]
    row6 = [-100, -100, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, -100, -100]
    row7 = [-100, -100, -100, 1, 1, -1, -1, 1, 1, -1, -1, -100, -100, -100]

    board = np.array([row1, row2, row3, row4, row5, row6, row7])
    state = State(board)
    env = Pardox()
    #player1= Random_Agent(env=env, player = 1)
    #player1 = AlphaBeta_Agent(environment = env, player = 1)
    player1 = DQN_Agent(env = env, player = -1, parametes_path=f'Data/params_800.pth')
    #player1 = DQN_Agent(env = env, player = 1, parametes_path='Data/params_3.pth')

    
    #player2 = DQN_Agent(env = env, player = -1, parametes_path='Data/params_800.pth')
    #player2 = DQN_Agent(env = env, player = 1, parametes_path='Data/params_3.pth')
    #player2 = AlphaBeta_Agent(environment = env, player = -1)
    player2= Random_Agent(env=env, player = 1)
    #player2= Human_Agent(environment=env, player=-1)
    #player2 = MinMaxAgent(environment = env, player = -1)
    
    test = Tester(env,player1, player2)
    print(test.test(100)) 
    # print(test.test(100)) 
    # print(test.test(100)) 
    # print(test.test(100)) 
    # print(test.test(100)) 
    # print(test.test(100)) 
    # print(test.test(100)) 
    #player1 = MinMaxAgent(environment = env, player = 1)
    #player1 = AlphaBeta_Agent(environment = env, player = -1)
    #player2 = Random_Agent(env, player = -1)
    #test = Tester(env,player1, player2)
    #print(test.test(100))DDD

