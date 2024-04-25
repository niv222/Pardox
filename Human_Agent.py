import pygame
from Graphics import *
from State import State
from Pardox import Pardox


class Human_Agent:

    def __init__(self, environment: Pardox ,player: int, graphics = None, train = False) -> None:
        self.player = player
        self.mode = 0 
        self.environment = environment
        self.graphics = graphics
        self.piece1 = None
        self.piece2 = None
        self.Visible = [False, False, False, False, False, False, True]
        # action = ((row1, col1), (row2, col2), direction );
        # after choosing two legal pieces the player will choose from the options: up-left; up-right; down-left; down-right; left; right; switch
        # mode: 0 - choose first piece; 1 - choose second piece; 2 - choose direction 

        # if mode == 0:
        #   if player choose legal piece:
        #       self.piece1 = piece
        #       mode = 1
        #       return None
        # if mode == 1:
        #   if player choose legal piece:
        #       self.piece2 = piece
        #       mode = 2
        #       return None
        # if mode == 2:
        #   if player choose legal direction:
        #       action = (self.piece1, self.piece2, direction)
        #       mode = 0
        #       return action

    

    def get_Action(self, graphics: Graphics = None, state : State= None, events = None):
        board = state.board
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                row_col = pygame.mouse.get_pos()
                pos = graphics.calc_pos(row_col, self.mode)
                Is_Good = True
                print(pos)
                
                if self.mode == 2:
                    graphics.draw(state, self)
                    pygame.display.update()
                    if pos or pos == 0:
                        action = (self.piece1, self.piece2, pos)
                        self.mode = 0
                        self.Visible = [False, False, False, False, False, False, True]
                        return action
                    
                if self.mode == 1:
                    if pos:
                        if self.environment.is_legal_Pos(state, self.piece1, pos) == False:
                            print('Pieces too far')
                            
                        if pos == self.piece1:
                            print('Cant choose the same piece')
                            
                        if state.board[pos[0]][pos[1]] == 0:
                            print('Cant choose empty piece') 

                        if self.environment.is_legal_Pos(state, self.piece1, pos) and pos != self.piece1 and state.board[pos[0]][pos[1]] != 0:
                            self.piece2 = pos
                            self.mode = 2
                            print(self.environment.get_Actions(state, (self.piece1, self.piece2)))
                            self.environment.Update_List(state ,self.Visible, self.piece1, self.piece2)


                    
                    else:
                        print('Illegal Position')
                        Is_Good = False
                        self.mode = 0
                        self.piece1 = None

                if self.mode == 0 and Is_Good:
                    if pos and state.board[pos[0]][pos[1]] != 0:
                        self.piece1 = pos
                        self.mode = 1
                
                
                
                



                    
                        

                    

                       

                            

        





        

           
                     
            

                        
                        

            




