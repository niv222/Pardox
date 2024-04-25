import numpy as np
import pygame
from pyparsing import col
import time
from State import State
from constant import *



class Graphics:
    def __init__(self, win):
        # self.board = state.board
        # self.rows, self.cols = self.board.shape
        self.win = win

    def calc_pos(self, x_y, mode):
        pos_y = round((x_y[1] - 60) / 70)
        pos_x = -1

        if pos_y == 0:
            if 245 <= x_y[0] <= 315:
                pos_x = 3
            elif 325 <= x_y[0] <= 395:
                pos_x = 5
            elif 405 <= x_y[0] <= 475:
                pos_x = 7
            elif 485 <= x_y[0] <= 555:
                pos_x = 9
            
        elif pos_y == 1:
            if 200 <= x_y[0] <= 270:
                pos_x = 2
            elif 280 <= x_y[0] <= 350:
                pos_x = 4
            elif 360 <= x_y[0] <= 430:
                pos_x = 6
            elif 440 <= x_y[0] <= 510:
                pos_x = 8
            elif 520 <= x_y[0] <= 590:
                pos_x = 10

        elif pos_y == 2:
             if 160 <= x_y[0] <= 230:
                pos_x = 1
             elif 240 <= x_y[0] <= 310:
                pos_x = 3
             elif 320 <= x_y[0] <= 390:
                pos_x = 5
             elif 400 <= x_y[0] <= 470:
                pos_x = 7
             elif 480 <= x_y[0] <= 550:
                pos_x = 9
             elif 560 <= x_y[0] <= 630:
                pos_x = 11

        elif pos_y == 3:
            if 115 <= x_y[0] <= 185:
                pos_x = 0
            elif 195 <= x_y[0] <= 265:
                pos_x = 2
            elif 275 <= x_y[0] <= 345:
                pos_x = 4
            elif 355 <= x_y[0] <= 425:
                pos_x = 6
            elif 435 <= x_y[0] <= 505:
                pos_x = 8
            elif 515 <= x_y[0] <= 585:
                pos_x = 10
            elif 595 <= x_y[0] <= 665:
                pos_x = 12

        elif pos_y == 4:
            if 160 <= x_y[0] <= 230:
                pos_x = 1
            elif 240 <= x_y[0] <= 310:
                pos_x = 3
            elif 320 <= x_y[0] <= 390:
                pos_x = 5
            elif 400 <= x_y[0] <= 470:
                pos_x = 7
            elif 480 <= x_y[0] <= 550:
                pos_x = 9
            elif 560 <= x_y[0] <= 630:
                pos_x = 11
            
        elif pos_y == 5:
            if 200 <= x_y[0] <= 270:
                pos_x = 2
            elif 280 <= x_y[0] <= 350:
                pos_x = 4
            elif 360 <= x_y[0] <= 430:
                pos_x = 6
            elif 440 <= x_y[0] <= 510:
                pos_x = 8
            elif 520 <= x_y[0] <= 590:
                pos_x = 10

        elif pos_y == 6:
            if 245 <= x_y[0] <= 315:
                pos_x = 3
            elif 325 <= x_y[0] <= 395:
                pos_x = 5
            elif 405 <= x_y[0] <= 475:
                pos_x = 7
            elif 485 <= x_y[0] <= 555:
                pos_x = 9

        if mode == 2:
           #Return 1-7 [1- left-up, 2- left, 3- left-down, 4- right-up, 5- right, 6- right-up, 7 switch]
            if 120 <= x_y[0] <= 270 and 530 <= x_y[1] <= 570:
                return 0

            if 300 <= x_y[0] <= 450 and  530 <= x_y[1] <= 570:
                return 1

            if 480 <= x_y[0] <= 630 and  530 <= x_y[1] <= 570:
                return 2

            if 120 <= x_y[0] <= 270 and 590 <= x_y[1] <= 630:
                return 3

            if 300 <= x_y[0] <= 450 and 590 <= x_y[1] <= 630:
                return 4

            if 480 <= x_y[0] <= 630 and 590 <= x_y[1] <= 630:
                return 5

            if 650 <= x_y[0] <= 750 and 530 <= x_y[1] <= 630:
                return 6

            print('Choose an action')
            
            return None
        

        if pos_x == -1:
            return None
        
        
        
        return (pos_y, pos_x)

    def draw_all_pieces(self, state:State):
        board = state.board
        num = 0

        #level1
        pos_x = 280 - Circle_Size / 2
        pos_y = 60
        for item in board[0]:
            if num % 2 == 0:
                color = self.calc_color(item)
                if color:
                    pygame.draw.circle(self.win, color,(pos_x + Circle_Size / 2, pos_y), Circle_Size / 2)
                    pos_x += Circle_Size + 10
            num += 1

            

        #level2
        pos_x = 235 - Circle_Size / 2
        pos_y = 130
        for item in board[1]:
            if num % 2 == 0:
                color = self.calc_color(item)
                if color:
                    pygame.draw.circle(self.win, color,(pos_x + Circle_Size / 2, pos_y), Circle_Size / 2)
                    pos_x += Circle_Size + 10
            num += 1

        #level3
        pos_x = 195 - Circle_Size / 2
        pos_y = 200
        for item in board[2]:
            if num % 2 == 0:
                color = self.calc_color(item)
                if color:
                    pygame.draw.circle(self.win, color,(pos_x + Circle_Size / 2, pos_y), Circle_Size / 2)
                    pos_x += Circle_Size + 10
            num += 1

        #level4
        pos_x = 150 - Circle_Size / 2
        pos_y = 270
        for item in board[3]:
            if num % 2 == 0:
                color = self.calc_color(item)
                if color:
                    pygame.draw.circle(self.win, color,(pos_x + Circle_Size / 2, pos_y), Circle_Size / 2)
                    pos_x += Circle_Size + 10
            num += 1
        #level5
        pos_x = 195 - Circle_Size / 2
        pos_y = 340
        for item in board[4]:
            if num % 2 == 0:
                color = self.calc_color(item)
                if color:
                    pygame.draw.circle(self.win, color,(pos_x + Circle_Size / 2, pos_y), Circle_Size / 2)
                    pos_x += Circle_Size + 10
            num += 1

        #level6
        pos_x = 235 - Circle_Size / 2
        pos_y = 410
        for item in board[5]:
            if num % 2 == 0:
                color = self.calc_color(item)
                if color:
                    pygame.draw.circle(self.win, color,(pos_x + Circle_Size / 2, pos_y), Circle_Size / 2)
                    pos_x += Circle_Size + 10
            num += 1

        #level7
        pos_x = 280 - Circle_Size / 2
        pos_y = 480
        for item in board[6]:
            if num % 2 == 0:
                color = self.calc_color(item)
                if color:
                    pygame.draw.circle(self.win, color,(pos_x + Circle_Size / 2, pos_y), Circle_Size / 2)
                    pos_x += Circle_Size + 10
            num += 1
    
    def calc_color(self, number):
            if number == -100 or number == 100:
                return None

            if number == 0:
                return LIGHT_BROWN
            elif number > 0:
                return BROWN
            elif number < 0:
                return BLACK

    def draw(self, state, player):
        self.win.fill(LIGHTGRAY)
        self.draw_all_pieces(state)

        pygame.font.init()
        font = pygame.font.SysFont(None, 40)

        img = font.render(f'Player {player.player} turn', True, BLACK)
        self.win.blit(img, (300, 670))

        if str(type(player)) == "<class 'Human_Agent.Human_Agent'>" and player.mode == 2:
            pad = 180

            if player.Visible[0]:
                img = font.render(f'Left-Up', True, BLACK)
                pygame.draw.rect(self.win, (255,0,0), pygame.Rect(120, 530, 150, 40), 2)
                self.win.blit(img, (143, 535))

            if player.Visible[1]:
                img2 = font.render(f'Left', True, BLACK)
                pygame.draw.rect(self.win, (255,0,0), pygame.Rect(120 + pad, 530, 150 , 40), 2)
                self.win.blit(img2, (350, 535))

            if player.Visible[2]:
                img3 = font.render(f'Left-Down', True, BLACK)
                pygame.draw.rect(self.win, (255,0,0), pygame.Rect(120 + pad  * 2, 530, 150 , 40), 2)
                self.win.blit(img3, (490, 535))
            
            if player.Visible[3]:
                img4 = font.render(f'Right-Up', True, BLACK)
                pygame.draw.rect(self.win, (255,0,0), pygame.Rect(120, 590, 150, 40), 2)
                self.win.blit(img4, (143, 595))

            if player.Visible[4]:
                img5 = font.render(f'Right', True, BLACK)
                pygame.draw.rect(self.win, (255,0,0), pygame.Rect(120 + pad, 590, 150 , 40), 2)
                self.win.blit(img5, (350, 595))

            if player.Visible[5]:
                img6 = font.render(f'Right-Dow', True, BLACK)
                pygame.draw.rect(self.win, (255,0,0), pygame.Rect(120 + pad  * 2, 590, 150 , 40), 2)
                self.win.blit(img6, (490, 595))
            

            img7 = font.render(f'Switch', True, BLACK)
            pygame.draw.rect(self.win, (255,0,0), pygame.Rect(120 + pad  * 2 + 170, 530, 100 , 100), 2)
            self.win.blit(img7, (120 + pad  * 2 + 170 + 2.5 , 570))

           


        #img = font.render(f'Switch', True, BLACK)
        #pygame.draw.rect(self.win, (255,0,0), pygame.Rect(40, 500, 120, 60), 2)
        #self.win.blit(img, (55, 520))

        #img = font.render(f'Move', True, BLACK)
        #pygame.draw.rect(self.win, (255,0,0), pygame.Rect(660, 500, 120, 60), 2)
        #self.win.blit(img, (685, 520))
  
    def blink(self, row_col, color):
        row, col = row_col
        player = self.board[row][col]
        for i in range (3):
            self.draw_square((row, col), color)
            pygame.display.update()
            time.sleep(0.2)
            self.draw_piece((row, col))
            pygame.display.update()
            time.sleep(0.2)
    

    

        
    