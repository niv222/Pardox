import numpy as np
import torch

class State:
    def __init__(self, board):
        self.board = board
        self.player = None # np.array Board 7 * 14; player1 = 1; player 2 = -1; empty = 0; outof board = -100;
                            # every piece has 2 squares.
                            # player can move to directions: 1. down-right; 2. down-left; 3. left; 4. right; 5. up-left; 6. up-right; 7. switch
                            # piece is determined by the left square
                            # action = ((row1, col1), (row2, col2), direction );
                            # legal move: two pieces are adjacent: there is a square that is adjacent; targer is empty

    def get_blank_pos (self):
        pos = np.where(self.board == 0)
        row = pos[0].item()
        col = pos[1].item()
        return row, col

    def __eq__(self, other):
        return np.equal(self.board, other.board).all()

    def copy (self):
        newBoard = np.copy(self.board)
        new_state = State (newBoard)
        new_state.player = self.player
        return new_state

    def getcols(self):
        return self.cols

    def getrows(self):
        return self.rows        
    
    def __hash__(self) -> int:
        return hash(repr(self.board))
    
    def reverse (self):
        reversed = self.copy()
       # reversed.board = reversed.board * -1
        #reversed.board[reversed.board == 100] = -100
        reversed.player = reversed.player * -1
        return reversed
    
    def score(self, env, state): 
        arr = state.board
        for row in arr:
              greater_than_zero_indices = np.where(row > 0)[0]
              for i in range(len(greater_than_zero_indices) - 7):
                if np.all(np.diff(greater_than_zero_indices[i:i+8]) == 1):
                    #print('Brown')
                    return 1
                
        result = False
        for row in arr:
            consecutive_count = 0
            for value in row:
                if value == -1:
                    consecutive_count += 1
                    if consecutive_count == 8:
                        result = True
                        break
                else:
                    consecutive_count = 0

        if result:
            return -1
                

        
        num_of_row = 0
        for row in arr:
            current_col = env.Get_Min_Of_Cols(num_of_row)
            if num_of_row + 3 <= 6:
               for col in row:
                    if current_col - 1 >= env.Get_Min_Of_Cols(num_of_row + 1) and current_col - 2 >= env.Get_Min_Of_Cols(num_of_row + 2) and current_col - 3 >= env.Get_Min_Of_Cols(num_of_row + 3):
                        if (arr[num_of_row][current_col] == 1 and arr[num_of_row + 1][current_col - 1] == 1 and arr[num_of_row + 2][current_col - 2] == 1 and arr[num_of_row + 3][current_col - 3] == 1): 
                            #print('diag Brown')
                            return 1
                        
                        elif (arr[num_of_row][current_col] == -1 and arr[num_of_row + 1][current_col - 1] == -1 and arr[num_of_row + 2][current_col - 2] == -1 and arr[num_of_row + 3][current_col - 3] == -1): 
                            #print('diag Black')
                            return -1

                    if current_col + 1 <= env.Get_Max_Of_Cols(num_of_row):
                        current_col += 1
            num_of_row += 1

                
                
                

        num_of_row = 0
        for row in arr:
            current_col = env.Get_Min_Of_Cols(num_of_row)
            if num_of_row + 3 <= 6:
               for col in row:
                    if current_col + 1 <= env.Get_Max_Of_Cols(num_of_row + 1) and current_col + 2 <= env.Get_Max_Of_Cols(num_of_row + 2) and current_col + 3 <= env.Get_Max_Of_Cols(num_of_row + 3):
                        if (arr[num_of_row][current_col] == 1 and arr[num_of_row + 1][current_col + 1] == 1 and arr[num_of_row + 2][current_col + 2] == 1 and arr[num_of_row + 3][current_col + 3] == 1): 
                            #print('diag Brown')
                            return 1
                        elif (arr[num_of_row][current_col] == -1 and arr[num_of_row + 1][current_col + 1] == -1 and arr[num_of_row + 2][current_col + 2] == -1 and arr[num_of_row + 3][current_col + 3] == -1): 
                            #print('diag Black')
                            return -1

                    if current_col + 1 <= env.Get_Max_Of_Cols(num_of_row):
                        current_col += 1
            num_of_row += 1

        return 0

            
    def toTensor (self, device = torch.device('cpu')) -> tuple:
        board_np = self.board.reshape(-1)
        board_tensor = torch.tensor(board_np, dtype=torch.float32, device=device)
        #actions_np = np.array(self.legal_actions)
        #actions_tensor = torch.from_numpy(actions_np)
        return board_tensor
    
    [staticmethod]
    def tensorToState (state_tensor, player):
        
        board = state_tensor.reshape([7,14]).cpu().numpy()
        state = State(board)
        state.player = player
        return state