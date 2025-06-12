from piece import Piece

class Rook(Piece):
    def __init__(self, color, coords, row, col, image):
        super().__init__(color, coords, row, col, image)
        self.first_move = True 
        self.points = 5

    def update_first_move(self):
        self.first_move = False 
            
    def move_is_legal(self, game_board, old_r, old_c, new_r, new_c):
        desired_loc = game_board.board[new_r][new_c]
    

        if old_r == new_r and abs(old_c - new_c) >= 1 and (desired_loc.piece is None or desired_loc.piece.color != self.color):
            return self.path_is_free(game_board, old_r, old_c, new_r, new_c) 
        elif old_c == new_c and abs(old_r - new_r) >= 1 and (desired_loc.piece is None or desired_loc.piece.color != self.color):
            return self.path_is_free(game_board, old_r, old_c, new_r, new_c)
        
        return False 
    
    def has_legal_moves(self, game_board, king):
        board = game_board.board 

        # checks if legal moves exist horizontally 
        for col in range(len(board[0])):
            tile = board[self.row][col]
            if tile.piece is not None and tile.piece == self:
                continue
            valid_move = self.move_is_legal(game_board, self.row, self.col, self.row, col) and self.check_king_safe(game_board, self.row, col, king)

            if valid_move:
                return True 
        
        # Checks if legal moves exist vertically
        for row in range(len(board)):
            tile = board[row][self.col]
            if tile.piece is not None and tile.piece == self:
                continue

            valid_move = self.move_is_legal(game_board, self.row, self.col, self.row, col) and self.check_king_safe(game_board, self.row, col, king)
            if valid_move:
                return True 

        return False 
