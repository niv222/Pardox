import numpy as np
from State import State
from Graphics import *

class Pardox:
    def __init__(self) -> None:
        self.state = self.get_init_state()
        self.Winner = 0
        #self.state = state
        
    def is_legal_Play(self, row_col : tuple ,state: State):
        my_list = []
        if state.board[row_col[0]][row_col[1]] != -100:
            near_players = self.get_near_players(row_col, state)
                      
    def get_init_state(self):
        row1 = [-100, -100, -100, 1, 1, -1, -1, 1, 1, -1, -1, -100, -100, -100]
        row2 = [-100, -100, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, -100, -100]
        row3 = [-100, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -100]
        row4 = [-1, -1, 0, 0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1]
        row5 = [-100, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -100]
        row6 = [-100, -100, -1, -1, 0, 0, 0, 0, 0, 0, 1, 1, -100, -100]
        row7 = [-100, -100, -100, 1, 1, -1, -1, 1, 1, -1, -1, -100, -100, -100]

        board = np.array([row1, row2, row3, row4, row5, row6, row7])   
        return State(board)    


    def reward(self ,state : State, action = None, IsBlack = None):
        if action:
            next_state = self.get_next_state(action, state)
        else:
            next_state = state

        if (self.is_end_of_game(next_state)):
            sum =  next_state.score(self, state)
            if IsBlack:
                return sum * -1, True  

            return sum, True  
        
        return 0, False


    def get_pairs(self, pos ,state: State):
        row = pos[0]
        col = pos[1]
        value = state.board[row][col]
        near_players = []
        #(3, 4)(3, 5)
        #(4, 3)(4, 4)
        if row - 1 >= 0:
            if col - 1 >= self.Get_Min_Of_Cols(row - 1) and state.board[row - 1][col - 1] ==  value and state.board[row - 1][col] ==  value:
                near_players.append((row - 1, col - 1))

            if col + 2 <= self.Get_Max_Of_Cols(row - 1) and state.board[row - 1][col + 1] == value and state.board[row - 1][col + 2] == value:
                near_players.append((row - 1, col + 1))

        if row + 1 <= 6:
            if col - 1 >= self.Get_Min_Of_Cols(row + 1) and state.board[row + 1][col - 1] ==  value and state.board[row + 1][col] ==  value:
                near_players.append((row + 1, col - 1))

            if col + 2 <= self.Get_Max_Of_Cols(row + 1) and state.board[row + 1][col + 1] == value and state.board[row + 1][col + 2] == value:
                near_players.append((row + 1, col + 1))


        if col - 2 >= self.Get_Min_Of_Cols(row):#Left
            if state.board[row][col - 2] == value and state.board[row][col - 1] ==  value:
                near_players.append((row, col - 2))

        if col + 2 <= self.Get_Max_Of_Cols(row):
            if state.board[row][col + 2] ==  value and state.board[row][col + 1] ==  value:
                near_players.append((row, col + 2))

        return near_players        

    def get_near_players(self, pos, state : State):
        row = pos[0]
        col = pos[1]
        value = state.board[row][col]
        near_players = []
        #(3, 4)(3, 5)
        #(4, 3)(4, 4)
        if row - 1 >= 0:
            if col - 1 >= self.Get_Min_Of_Cols(row - 1) and state.board[row - 1][col - 1] == -1 * value and state.board[row - 1][col] == -1 * value:
                near_players.append((row - 1, col - 1))

            if col + 2 <= self.Get_Max_Of_Cols(row - 1) and state.board[row - 1][col + 1] == -1 * value and state.board[row - 1][col + 2] == -1 * value:
                near_players.append((row - 1, col + 1))

        if row + 1 <= 6:
            if col - 1 >= self.Get_Min_Of_Cols(row + 1) and state.board[row + 1][col - 1] == -1 * value and state.board[row + 1][col] == -1 * value:
                near_players.append((row + 1, col - 1))

            if col + 2 <= self.Get_Max_Of_Cols(row + 1) and state.board[row + 1][col + 1] == -1 * value and state.board[row + 1][col + 2] == -1 * value:
                near_players.append((row + 1, col + 1))


        if col - 2 >= self.Get_Min_Of_Cols(row):#Left
            if state.board[row][col - 2] == -1 * value and state.board[row][col - 1] == -1 * value:
                near_players.append((row, col - 2))

        if col + 2 <= self.Get_Max_Of_Cols(row):
            if state.board[row][col + 2] == -1 * value and state.board[row][col + 1] == -1 * value:
                near_players.append((row, col + 2))

        return near_players        
        
    def is_legal_Pos(self, state ,pos1, pos2):
        if abs(pos1[0] - pos2[0]) > 1:
            return False
        
        if abs(pos1[1] - pos2[1]) > 2:
            return False
        
        if state.board[pos1[0]][pos1[1]] != -1 and state.board[pos2[0]][pos2[1]] != 1 and state.board[pos1[0]][pos1[1]] != 1 and state.board[pos2[0]][pos2[1]] != -1:
            print('You must choose 2 difrrent pieces')
            return False
        
        return True           
    
    def Switch_Pieces(self, state: State, pos1: tuple[int, int], pos2: tuple[int, int]):
        temp = state.board[pos1[0][0]][pos1[0][1]] # gets value
        state.board[pos1[0][0]][pos1[0][1]] = state.board[pos2[0][0]][pos2[0][1]]
        state.board[pos1[1][0]][pos1[1][1]] = state.board[pos2[1][0]][pos2[1][1]]
        state.board[pos2[0][0]][pos2[0][1]] = temp
        state.board[pos2[1][0]][pos2[1][1]] = temp


    def Get_Max_Of_Cols(self, row):
        if row == 0 or row == 6:
            return 10
        if row == 1 or row == 5:
            return 11
        
        if row == 2 or row == 4:
            return 12
        
        if row == 3:
            return 13
        
    def Get_Min_Of_Cols(self, row):
        if row == 0 or row == 6:
            return 3
        if row == 1 or row == 5:
            return 2
        
        if row == 2 or row == 4:
            return 1
        
        if row == 3:
            return 0
        

    def Update_List(self, state ,lst, piece1, piece2):
        nothing, moves = self.get_Actions(state, (piece1, piece2))

        if 'Up-Left' in moves:
            lst[0] = True
        
        if 'Left' in moves:
            lst[1] = True
        
        if 'Down-Left' in moves:
            lst[2] = True

        if 'Up-Right' in moves:
            lst[3] = True

        if 'Right' in moves:
            lst[4] = True

        if 'Down-Right' in moves:
            lst[5] = True
    
    def sortByRow(l1 : list[tuple[int, int]]): # list << [[(0, 3), (0, 4)], [(0, 5), (0, 6)]]
        #l1[0] = [(0, 3), (0, 4)]
        #l1[1] = [(0, 5), (0, 6)]
        temp = l1[0]

        if l1[0][0][0] == l1[1][0][0]:
            if l1[0][0][1] > l1[1][0][1]:
                l1 = [l1[1], l1[0]]

                 
        if l1[0][0][0] > l1[1][0][0]:
            l1[0] = l1[1] 
            l1[1] = temp


    def get_Actions_Random(self, state : State= None, my_pos = None):
        my_pos = [[my_pos[0], (my_pos[0][0], my_pos[0][1] + 1)], [my_pos[1], (my_pos[1][0], my_pos[1][1] + 1)]]
        action = []
        self.sortByRow(my_pos)

        #my_pos = list << [[(0, 3), (0, 4)], [(0, 5), (0, 6)]]
        #l1[0] = [(0, 3), (0, 4)]
        #l1[1] = [(0, 5), (0, 6)]

        pos1 = my_pos[0] # [(0, 3), (0, 4)]
        pos2 = my_pos[1] # [(0, 5), (0, 6)]

        board = state.board
      

    #Same_Row
            #Right
        if pos1[0][0] == pos2[0][0]:
            
            if pos2[1][1] + 2 <= self.Get_Max_Of_Cols(pos1[0][0]): ## check if goes out of index at the Col + 1
                if board[pos2[1][0]][pos2[1][1] + 1]  == 0 and board[pos2[1][0]][pos2[1][1] + 2] == 0:
                    action.append((pos1[0], pos2[0], 4))

            #left
            if pos1[0][1] >= self.Get_Min_Of_Cols(pos1[0][0]): ## check if goes out of index at the Col - 1
                if board[pos1[0][0]][pos1[0][1] - 1] == 0 and board[pos1[0][0]][pos1[0][1] - 2] == 0:
                    action.append((pos1[0], pos2[0], 1))


            #up
            if pos1[0][0] != 0 and pos2[1][1] + 1 <= self.Get_Max_Of_Cols(pos1[0][0] - 1):  #check if row is 0
                if board[pos1[0][0] - 1][pos1[0][1] + 1] == board[pos1[0][0] - 1][pos2[1][1] + 1] == 0:
                    action.append((pos1[0], pos2[0], 3))

            if pos1[0][0] != 0 and pos1[0][1] -1 >= self.Get_Min_Of_Cols(pos1[0][0] - 1):
                if board[pos1[0][0] - 1][pos1[0][1] - 1] == board[pos2[0][0] - 1][pos2[0][1] - 1] == 0:
                    action.append((pos1[0], pos2[0], 0))

            #down

            if pos1[0][0] != 6 and pos1[0][1] - 1 >= self.Get_Min_Of_Cols(pos1[0][0] + 1):
                if board[pos1[0][0] + 1][pos1[0][1] - 1] == board[pos1[0][0] + 1][pos2[0][1] - 1] == 0:
                    action.append((pos1[0], pos2[0], 2))
       

            if pos1[0][0] != 6 and pos2[1][1] + 1 <= self.Get_Max_Of_Cols(pos2[0][0] + 1):
                if board[pos1[0][0] + 1][pos1[0][1] + 1] == board[pos1[0][0] + 1][pos2[0][1] + 1] == 0:
                    action.append((pos1[0], pos2[0], 5))


        #Now[[(3, 4), (3, 5)], [(4, 5), (4, 6)]]
        if abs(pos1[0][0] - pos2[0][0]) == 1:

            if pos1[0][1] - 1 == pos2[0][1]:
                #Right
                
               
                if pos1[1][1] + 2 <= self.Get_Max_Of_Cols(pos1[0][0]) and pos2[1][1] + 2 <= self.Get_Max_Of_Cols(pos2[0][0]):
                    if board[pos1[0][0]][pos1[0][1] + 2] == board[pos2[0][0]][pos2[0][1] + 2] == 0:
                        action.append((pos1[0], pos2[0], 4))

                #Left
                if pos1[0][1] - 2 >= self.Get_Min_Of_Cols(pos1[0][0]) and pos2[0][1] - 2 >= self.Get_Min_Of_Cols(pos2[0][0]):
                    if board[pos1[0][0]][pos1[0][1] - 2] == board[pos2[0][0]][pos2[0][1] - 2] == 0:
                        action.append((pos1[0], pos2[0], 1))

                #Up
                if pos1[0][0] != 0:
                    if pos1[1][1] + 1 <= self.Get_Max_Of_Cols(pos1[0][0] - 1):
                        if board[pos1[0][0] - 1][pos1[0][1] + 1] == 0:
                            action.append((pos1[0], pos2[0], 3))

        
                if pos1[0][0] != 0:
                    if pos1[0][1] - 1 >= self.Get_Min_Of_Cols(pos1[0][0] - 1):
                        if board[pos1[0][0] - 1][pos1[0][1] - 1] == board[pos2[0][0] - 1][pos2[0][1] - 1] == 0:
                            action.append((pos1[0], pos2[0], 0))

                #Down
                #Now[[(3, 8), (3, 9)], [(4, 7), (4, 8)]]
                #Goto [(4, 9), (4, 10)], [(5, 8), (5, 9)]

                if pos2[0][0] != 6:
                    if pos2[1][1] - 1 >= self.Get_Min_Of_Cols(pos2[0][0] + 1):
                        if board[pos2[0][0] + 1][pos2[0][1] - 1] == 0:
                            action.append((pos1[0], pos2[0], 2))
                if pos2[0][0] != 6:
                    if pos2[1][1] + 1 <= self.Get_Max_Of_Cols(pos2[0][0] + 1):
                        if board[pos1[0][0] + 1][pos1[0][1] + 1] == board[pos2[0][0] + 1][pos2[0][1] + 1] == 0:
                            action.append((pos1[0], pos2[0], 5))


            else:
                #Right
                #Now[[(3, 4), (3, 5)], [(4, 5), (4, 6)]]
                #Goto[[(3, 2), (3, 3)], [(4, 3), (4, 4)]]
               
                if pos2[1][1] + 2 <= self.Get_Max_Of_Cols(pos2[0][0]):
                    if board[pos1[0][0]][pos1[0][1] + 2] == board[pos2[0][0]][pos2[0][1] + 2] == 0:
                        action.append((pos1[0], pos2[0], 4))

                #Left
                if pos1[0][1] - 2 >= self.Get_Min_Of_Cols(pos1[0][0]) and pos2[0][1] - 2 >= self.Get_Min_Of_Cols(pos2[0][0]):
                    if board[pos1[0][0]][pos1[0][1] - 2] == board[pos2[0][0]][pos2[0][1] - 2] == 0:
                        action.append((pos1[0], pos2[0], 1))

                #Up
                if pos1[0][0] != 0:
                    if pos1[1][1] - 1 <= self.Get_Max_Of_Cols(pos1[0][0] - 1):
                        if board[pos1[0][0] - 1][pos1[0][1] - 1] == 0:
                            action.append((pos1[0], pos2[0], 3))

                #Now[[(3, 4), (3, 5)], [(4, 5), (4, 6)]]
                #Goto [[(2, 5), (2, 6)], [(3, 6), (3, 7)]]

                if pos1[0][0] != 0:
                    if pos1[1][1] + 1 <= self.Get_Max_Of_Cols(pos1[0][0] - 1):
                        if board[pos1[0][0] - 1][pos1[0][1] + 1] == board[pos2[0][0] - 1][pos2[0][1] + 1] == 0:
                            action.append((pos1[0], pos2[0], 0))

                #Down
                

                if pos2[0][0] != 6:
                    if pos2[1][1] + 1 <= self.Get_Max_Of_Cols(pos2[0][0] + 1):
                        if board[pos2[0][0] + 1][pos2[0][1] + 1] == 0:
                           action.append((pos1[0], pos2[0], 2))

                #Now [[(3, 4), (3, 5)], [(4, 5), (4, 6)]]
                #Goto [[(4, 3), (4, 4)], [(5, 4), (5, 5)]]

                if pos2[0][0] != 6:
                    if pos2[1][1] - 1 >= self.Get_Min_Of_Cols(pos2[0][0] + 1):
                        if board[pos1[0][0] + 1][pos1[0][1] - 1] == board[pos2[0][0] + 1][pos2[0][1] - 1] == 0:
                            action.append((pos1[0], pos2[0], 5))

        return action


    def get_Actions(self, state : State= None, my_pos = None):
        my_pos = [[my_pos[0], (my_pos[0][0], my_pos[0][1] + 1)], [my_pos[1], (my_pos[1][0], my_pos[1][1] + 1)]]
        moves = []
        moves_2 = []
        self.sortByRow(my_pos)

        #my_pos = list << [[(0, 3), (0, 4)], [(0, 5), (0, 6)]]
        #l1[0] = [(0, 3), (0, 4)]
        #l1[1] = [(0, 5), (0, 6)]

        pos1 = my_pos[0] # [(0, 3), (0, 4)]
        pos2 = my_pos[1] # [(0, 5), (0, 6)]
        board = state.board
      

    #Same_Row
            #Right
        if pos1[0][0] == pos2[0][0]:
            
            if pos2[1][1] + 2 <= self.Get_Max_Of_Cols(pos1[0][0]): ## check if goes out of index at the Col + 1
                if board[pos2[1][0]][pos2[1][1] + 1]  == 0 and board[pos2[1][0]][pos2[1][1] + 2] == 0:
                    moves.append([pos2, [(pos2[1][0], pos2[1][1] + 1), (pos2[1][0], pos2[1][1] + 2)]])
                    moves_2.append('Right')

            #left
            if pos1[0][1] >= self.Get_Min_Of_Cols(pos1[0][0]): ## check if goes out of index at the Col - 1
                if board[pos1[0][0]][pos1[0][1] - 1] == 0 and board[pos1[0][0]][pos1[0][1] - 2] == 0:
                    moves.append([((pos1[0][0], pos1[0][1] - 2), (pos1[0][0], pos1[0][1] - 1)), pos1])
                    moves_2.append('Left')


            #up
            if pos1[0][0] != 0 and pos2[1][1] + 1 <= self.Get_Max_Of_Cols(pos1[0][0] - 1) :  #check if row is 0
                if board[pos1[0][0] - 1][pos1[0][1] + 1] == board[pos1[0][0] - 1][pos2[1][1] + 1] == 0:
                    moves.append([[(pos1[0][0] - 1, pos1[0][1] + 1), (pos1[0][0] - 1, pos1[0][1] + 2)], [(pos1[0][0] - 1, pos1[0][1] + 3), ((pos1[0][0] - 1, pos1[0][1] + 4))]])
                    moves_2.append('Up-Right')

            if pos1[0][0] != 0 and pos1[0][1] -1 >= self.Get_Min_Of_Cols(pos1[0][0] - 1):
                if board[pos1[0][0] - 1][pos1[0][1] - 1] == board[pos2[0][0] - 1][pos2[0][1] - 1] == 0:
                    moves.append([[((pos1[0][0] - 1), (pos1[0][1] - 1)), ((pos1[0][0] - 1), (pos1[0][1]))], [((pos1[0][0] - 1), (pos1[0][1] + 1)), ((pos1[0][0] - 1), (pos1[0][1] + 2))]])
                    moves_2.append('Up-Left')

            #down

            if pos1[0][0] != 6 and pos1[0][1] - 1 >= self.Get_Min_Of_Cols(pos1[0][0] + 1):
                if board[pos1[0][0] + 1][pos1[0][1] - 1] == board[pos1[0][0] + 1][pos2[0][1] - 1] == 0:
                    moves.append([[((pos1[0][0] + 1), (pos1[0][1] - 1)), ((pos1[0][0] + 1), (pos1[0][1]))], [((pos2[0][0] + 1), (pos2[0][1] - 1)), ((pos2[0][0] + 1), (pos2[1][1] - 1))]])
                    moves_2.append('Down-Left')

       

            if pos1[0][0] != 6 and pos2[1][1] + 1 <= self.Get_Max_Of_Cols(pos2[0][0] + 1):
                if board[pos1[0][0] + 1][pos1[0][1] + 1] == board[pos1[0][0] + 1][pos2[0][1] + 1] == 0:
                    moves.append([[((pos1[0][0] + 1), (pos1[0][1] + 1)), ((pos1[0][0] + 1), (pos1[0][1] + 2))], [((pos2[0][0] + 1), (pos2[0][1] + 1)), ((pos2[0][0] + 1), (pos2[1][1] + 1))]])
                    moves_2.append('Down-Right')


        #Now[[(3, 4), (3, 5)], [(4, 5), (4, 6)]]
        if abs(pos1[0][0] - pos2[0][0]) == 1:

            if pos1[0][1] - 1 == pos2[0][1]:
                #Right
                
               
                if pos1[1][1] + 2 <= self.Get_Max_Of_Cols(pos1[0][0]) and pos2[1][1] + 2 <= self.Get_Max_Of_Cols(pos2[0][0]):
                    if board[pos1[0][0]][pos1[0][1] + 2] == board[pos2[0][0]][pos2[0][1] + 2] == 0:
                        moves.append([[((pos1[0][0]), (pos1[0][1] + 2)), ((pos1[0][0]), (pos1[1][1] + 2))], [((pos2[0][0]), (pos2[0][1] + 2)), ((pos2[0][0]), (pos2[1][1] + 2))]])
                        moves_2.append('Right')

                #Left
                if pos1[0][1] - 2 >= self.Get_Min_Of_Cols(pos1[0][0]) and pos2[0][1] - 2 >= self.Get_Min_Of_Cols(pos2[0][0]):
                    if board[pos1[0][0]][pos1[0][1] - 2] == board[pos2[0][0]][pos2[0][1] - 2] == 0:
                        moves.append([[((pos1[0][0]), (pos1[0][1] - 2)), ((pos1[0][0]), (pos1[1][1] - 2))], [((pos2[0][0]), (pos2[0][1] - 2)), ((pos2[0][0]), (pos2[1][1] - 2))]])
                        moves_2.append('Left')

                #Up
                if pos1[0][0] != 0:
                    if pos1[1][1] + 1 <= self.Get_Max_Of_Cols(pos1[0][0] - 1):
                        if board[pos1[0][0] - 1][pos1[0][1] + 1] == 0:
                            moves.append([pos1, [((pos1[0][0] - 1), (pos1[0][1] + 1)), ((pos1[0][0] - 1), (pos1[1][1] + 1))]])
                            moves_2.append('Up-Right')

        
                if pos1[0][0] != 0:
                    if pos1[0][1] - 1 >= self.Get_Min_Of_Cols(pos1[0][0] - 1):
                        if board[pos1[0][0] - 1][pos1[0][1] - 1] == board[pos2[0][0] - 1][pos2[0][1] - 1] == 0:
                            moves.append([[((pos1[0][0] - 1), (pos1[0][1] - 1)), ((pos1[1][0] - 1), (pos1[1][1] - 1))], [((pos2[0][0] - 1), (pos2[0][1] - 1)), ((pos2[0][0] - 1), (pos2[1][1] - 1))]])     
                            moves_2.append('Up-Left')

                #Down
                #Now[[(3, 8), (3, 9)], [(4, 7), (4, 8)]]
                #Goto [(4, 9), (4, 10)], [(5, 8), (5, 9)]

                if pos2[0][0] != 6:
                    if pos2[1][1] - 1 >= self.Get_Min_Of_Cols(pos2[0][0] + 1):
                        if board[pos2[0][0] + 1][pos2[0][1] - 1] == 0:
                            moves.append([pos2, [((pos2[0][0] + 1), (pos2[0][1] - 1)), ((pos2[0][0] + 1), (pos2[1][1] - 1))]])     
                            moves_2.append('Down-Left')

                if pos2[0][0] != 6:
                    if pos2[1][1] + 1 <= self.Get_Max_Of_Cols(pos2[0][0] + 1):
                        if board[pos1[0][0] + 1][pos1[0][1] + 1] == board[pos2[0][0] + 1][pos2[0][1] + 1] == 0:
                            moves.append([[((pos1[0][0] + 1), (pos1[0][1] + 1)), ((pos1[0][0] + 1), (pos1[1][1] + 1))], [((pos2[0][0] + 1), (pos2[0][1] + 1)), ((pos2[0][0] + 1), (pos2[1][1] + 1))]])     
                            moves_2.append('Down-Right')



            else:
                #Right
                #Now[[(3, 4), (3, 5)], [(4, 5), (4, 6)]]
                #Goto[[(3, 2), (3, 3)], [(4, 3), (4, 4)]]
               
                if pos2[1][1] + 2 <= self.Get_Max_Of_Cols(pos2[0][0]):
                    if board[pos1[0][0]][pos1[0][1] + 2] == board[pos2[0][0]][pos2[0][1] + 2] == 0:
                        moves.append([[((pos1[0][0]), (pos1[0][1] + 2)), ((pos1[0][0]), (pos1[1][1] + 2))], [((pos2[0][0]), (pos2[0][1] + 2)), ((pos2[0][0]), (pos2[1][1] + 2))]])
                        moves_2.append('Right')

                #Left
                if pos1[0][1] - 2 >= self.Get_Min_Of_Cols(pos1[0][0]) and pos2[0][1] - 2 >= self.Get_Min_Of_Cols(pos2[0][0]):
                    if board[pos1[0][0]][pos1[0][1] - 2] == board[pos2[0][0]][pos2[0][1] - 2] == 0:
                        moves.append([[((pos1[0][0]), (pos1[0][1] - 2)), ((pos1[0][0]), (pos1[1][1] - 2))], [((pos2[0][0]), (pos2[0][1] - 2)), ((pos2[0][0]), (pos2[1][1] - 2))]])
                        moves_2.append('Left')

                #Up
                if pos1[0][0] != 0:
                    if pos1[1][1] - 1 <= self.Get_Max_Of_Cols(pos1[0][0] - 1):
                        if board[pos1[0][0] - 1][pos1[0][1] - 1] == 0:
                            moves.append([pos1, [((pos1[0][0] - 1), (pos1[0][1] - 1)), ((pos1[0][0] - 1), (pos1[1][1] - 1))]])
                            moves_2.append('Up-Left')

                #Now[[(3, 4), (3, 5)], [(4, 5), (4, 6)]]
                #Goto [[(2, 5), (2, 6)], [(3, 6), (3, 7)]]

                if pos1[0][0] != 0:
                    if pos1[1][1] + 1 <= self.Get_Max_Of_Cols(pos1[0][0] - 1):
                        if board[pos1[0][0] - 1][pos1[0][1] + 1] == board[pos2[0][0] - 1][pos2[0][1] + 1] == 0:
                            moves.append([[((pos1[0][0] - 1), (pos1[0][1] + 1)), ((pos1[1][0] - 1), (pos1[1][1] + 1))], [((pos2[0][0] - 1), (pos2[0][1] + 1)), ((pos2[0][0] - 1), (pos2[1][1] + 1))]])     
                            moves_2.append('Up-Right')

                #Down
                

                if pos2[0][0] != 6:
                    if pos2[1][1] + 1 <= self.Get_Max_Of_Cols(pos2[0][0] + 1):
                        if board[pos2[0][0] + 1][pos2[0][1] + 1] == 0:
                            moves.append([pos2, [((pos2[0][0] + 1), (pos2[0][1] + 1)), ((pos2[0][0] + 1), (pos2[1][1] + 1))]])     
                            moves_2.append('Down-Right')

                #Now [[(3, 4), (3, 5)], [(4, 5), (4, 6)]]
                #Goto [[(4, 3), (4, 4)], [(5, 4), (5, 5)]]

                if pos2[0][0] != 6:
                    if pos2[1][1] - 1 >= self.Get_Min_Of_Cols(pos2[0][0] + 1):
                        if board[pos1[0][0] + 1][pos1[0][1] - 1] == board[pos2[0][0] + 1][pos2[0][1] - 1] == 0:
                            moves.append([[((pos1[0][0] + 1), (pos1[0][1] - 1)), ((pos1[0][0] + 1), (pos1[1][1] - 1))], [((pos2[0][0] + 1), (pos2[0][1] - 1)), ((pos2[0][0] + 1), (pos2[1][1] - 1))]])     
                            moves_2.append('Down-Left')

        return moves, moves_2


    def move(self, state: State, action = None):
        my_pos = [[action[0], (action[0][0], action[0][1] + 1)], [action[1], (action[1][0], action[1][1] + 1)]]
        Targets, moves = self.get_Actions(state, action)
        if my_pos[0][0][0] == my_pos[1][0][0]:
            if action[2] == 0: #Left-Up
                if 'Up-Left' in moves:
                    Target_Position = Targets[moves.index('Up-Left')]
                    self.Switch_Pieces(state, my_pos[1], Target_Position[1]) 
                    self.Switch_Pieces(state, my_pos[0], Target_Position[0])
                    return None

            if action[2] == 1: #Left
                if 'Left' in moves:
                    Target_Position = Targets[moves.index('Left')]
                    self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                    self.Switch_Pieces(state, my_pos[1], Target_Position[1])
                    return None

            if action[2] == 2: #Left
                if 'Down-Left' in moves:
                    Target_Position = Targets[moves.index('Down-Left')]
                    self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                    self.Switch_Pieces(state, my_pos[1], Target_Position[1])
                    return None

            if action[2] == 3: #Right-Up
                if 'Up-Right' in moves:
                    Target_Position = Targets[moves.index('Up-Right')]
                    self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                    self.Switch_Pieces(state, my_pos[1], Target_Position[1])
                    return None

            if action[2] == 4: #Right
                if 'Right' in moves:
                    Target_Position = Targets[moves.index('Right')]
                    self.Switch_Pieces(state, my_pos[1], Target_Position[1]) 
                    self.Switch_Pieces(state, my_pos[0], Target_Position[0])
                    return None

            if action[2] == 5:
                if 'Down-Right' in moves:
                    Target_Position = Targets[moves.index('Down-Right')]
                    self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                    self.Switch_Pieces(state, my_pos[1], Target_Position[1])
                    return None
        
        elif abs(my_pos[0][0][0] - my_pos[1][0][0]) == 1:
            if my_pos[0][0][1] - 1 == my_pos[1][0][1]:
                if action[2] == 0: #Left-Up
                    if 'Up-Left' in moves:
                        Target_Position = Targets[moves.index('Up-Left')]
                        self.sortByRow(Target_Position)
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1]) 
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0])
                        return None

                if action[2] == 1: #Left
                    if 'Left' in moves:
                        Target_Position = Targets[moves.index('Left')]
                        self.sortByRow(Target_Position)
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1])
                        return None

                if action[2] == 2: #Left
                    if 'Down-Left' in moves:
                        Target_Position = Targets[moves.index('Down-Left')]
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1]) 
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0])
                        return None

                if action[2] == 3: #Right-Up
                    if 'Up-Right' in moves:
                        Target_Position = Targets[moves.index('Up-Right')]
                        self.sortByRow(Target_Position)
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1])
                        return None

                if action[2] == 4: #Right
                    if 'Right' in moves:
                        Target_Position = Targets[moves.index('Right')]
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1]) 
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0])
                        return None

                if action[2] == 5:
                    if 'Down-Right' in moves:
                        Target_Position = Targets[moves.index('Down-Right')]
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1])
                        return None

            else:
                if action[2] == 0: #Left-Up
                    if 'Up-Left' in moves:
                        Target_Position = Targets[moves.index('Up-Left')]
                        self.Switch_Pieces(state, my_pos[0], Target_Position[1]) 
                        self.Switch_Pieces(state, my_pos[1], Target_Position[0])

                if action[2] == 1: #Left
                    if 'Left' in moves:
                        Target_Position = Targets[moves.index('Left')]
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1])

                if action[2] == 2: #Left
                    if 'Down-Left' in moves:
                        Target_Position = Targets[moves.index('Down-Left')]
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1])

                if action[2] == 3: #Right-Up
                    if 'Up-Right' in moves:
                        Target_Position = Targets[moves.index('Up-Right')]
                        self.sortByRow(Target_Position)
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0]) 
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1])

                if action[2] == 4: #Right
                    if 'Right' in moves:
                        Target_Position = Targets[moves.index('Right')]
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1]) 
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0])

                if action[2] == 5:
                    if 'Down-Right' in moves:
                        Target_Position = Targets[moves.index('Down-Right')]
                        self.Switch_Pieces(state, my_pos[1], Target_Position[1]) 
                        self.Switch_Pieces(state, my_pos[0], Target_Position[0])

       

        if action[2] == 6:
            self.Switch_Pieces(state, my_pos[0], my_pos[1])

                    

    def switchPlayers(self, player, player1, player2):
        if player == player1:
            return player2
        else:
            return player1
   
    def get_legal_actions(self, state: State):
        if state.player == None or state.player != 1:
            state.player = -1

        legal_action = []
        Rows, Cols =  np.where(state.board == 1)
        positons = tuple(zip(Rows, Cols))[0::2]

        for pos in positons:
            pairs = self.get_near_players(pos, state)

            for pair in pairs:
                action = self.get_Actions_Random(state, (pos, pair))
                legal_action = legal_action + action

        
        return legal_action


    def get_triples(self, state: State, pos):
        row = pos[0]
        col = pos[1]
        value = state.board[row][col]
        near_players = 0
        #(3, 4)(3, 5)
        #(4, 3)(4, 4)
        if row - 2 >= 0:
            if col - 3 >= self.Get_Min_Of_Cols(row - 2) and state.board[row - 1][col - 1] ==  value and state.board[row - 1][col] ==  value and state.board[row - 2][col - 1] ==  value and state.board[row - 2][col - 2] ==  value:
                near_players += 1

            if col + 3 <= self.Get_Max_Of_Cols(row - 2) and state.board[row - 1][col + 1] == value and state.board[row - 1][col + 2] == value and state.board[row - 2][col + 2] and state.board[row - 2][col + 3]:
                near_players += 1

        if row + 2 <= 6:
            if col  + 1>= self.Get_Min_Of_Cols(row + 2) and state.board[row + 1][col - 1] ==  value and state.board[row + 1][col] ==  value and state.board[row + 2][col + 1] == value:
                near_players += 1

            if col + 3 <= self.Get_Max_Of_Cols(row + 1) and state.board[row + 1][col + 1] == value and state.board[row + 1][col + 2] == value and state.board[row + 2][col + 3] == value:
                near_players += 1


        if col - 4 >= self.Get_Min_Of_Cols(row):#Left
            if state.board[row][col - 2] == value and state.board[row][col - 1] ==  value and state.board[row][col - 3] == value and state.board[row][col - 4] ==  value:
                near_players += 1

        if col + 4 <= self.Get_Max_Of_Cols(row):
            if state.board[row][col + 2] ==  value and state.board[row][col + 1] ==  value and state.board[row][col + 3] ==  value and state.board[row][col + 4] ==  value:
                near_players += 1

        return near_players        

    def get_all_next_states (self, state: State) -> tuple:
        legal_actions = self.get_legal_actions(state)
        next_states = []
        for action in legal_actions:
            next_states.append(self.get_next_state(action, state))
        return next_states, legal_actions

    def is_end_of_game(self ,arr : State): ## To fix
        arr = arr.board

        for row in arr:
              greater_than_zero_indices = np.where(row > 0)[0]
              for i in range(len(greater_than_zero_indices) - 7):
                if np.all(np.diff(greater_than_zero_indices[i:i+8]) == 1):
                    #print('Brown')
                    self.Winner = 1
                    return True
                
        result = False
        for row in arr:
            consecutive_count = 0
            for value in row:
                if -11 < value < 0:
                    consecutive_count += 1
                    if consecutive_count == 8:
                        result = True
                        break
                else:
                    consecutive_count = 0

        if result:
            #print('Black')
            self.Winner = -1
            return True
                

        
        num_of_row = 0
        for row in arr:
            current_col = self.Get_Min_Of_Cols(num_of_row)
            if num_of_row + 3 <= 6:
               for col in row:
                    if current_col - 1 >= self.Get_Min_Of_Cols(num_of_row + 1) and current_col - 2 >= self.Get_Min_Of_Cols(num_of_row + 2) and current_col - 3 >= self.Get_Min_Of_Cols(num_of_row + 3):
                        if (arr[num_of_row][current_col] == 1 and arr[num_of_row + 1][current_col - 1] == 1 and arr[num_of_row + 2][current_col - 2] == 1 and arr[num_of_row + 3][current_col - 3] == 1): 
                            #print('diag Brown')
                            self.Winner = 1
                            return True
                        
                        elif (arr[num_of_row][current_col] == -1 and arr[num_of_row + 1][current_col - 1] == -1 and arr[num_of_row + 2][current_col - 2] == -1 and arr[num_of_row + 3][current_col - 3] == -1): 
                            #print('diag Black')
                            self.Winner = -1
                            return True

                    if current_col + 1 <= self.Get_Max_Of_Cols(num_of_row):
                        current_col += 1
            num_of_row += 1

                
                
                

        num_of_row = 0
        for row in arr:
            current_col = self.Get_Min_Of_Cols(num_of_row)
            if num_of_row + 3 <= 6:
               for col in row:
                    if current_col + 1 <= self.Get_Max_Of_Cols(num_of_row + 1) and current_col + 2 <= self.Get_Max_Of_Cols(num_of_row + 2) and current_col + 3 <= self.Get_Max_Of_Cols(num_of_row + 3):
                        if (arr[num_of_row][current_col] == 1 and arr[num_of_row + 1][current_col + 1] == 1 and arr[num_of_row + 2][current_col + 2] == 1 and arr[num_of_row + 3][current_col + 3] == 1): 
                            #print('diag Brown')
                            self.Winner = 1
                            return True
                        elif (arr[num_of_row][current_col] == -1 and arr[num_of_row + 1][current_col + 1] == -1 and arr[num_of_row + 2][current_col + 2] == -1 and arr[num_of_row + 3][current_col + 3] == -1): 
                            #print('diag Black')
                            self.Winner = -1
                            return True

                    if current_col + 1 <= self.Get_Max_Of_Cols(num_of_row):
                        current_col += 1
            num_of_row += 1

        

        return False

    def get_next_state(self, action, state:State):
        next_state = state.copy()
        next_state.player = state.player
        self.move(next_state, action)

        return next_state
    
    def sortByRow(self ,l1 : list[tuple[int, int]]): #To Fix
        temp = l1[0]

        if l1[0][0] == l1[1][0]:
            if l1[0][1] > l1[1][1]:
                l1 = [l1[1], l1[0]]

                 
        if l1[0][0] > l1[1][0]:
            l1[0] = l1[1] 
            l1[1] = temp
    
    
    