from piece import Piece

class Knight(Piece):
    def __init__(self, color, coords, row, col, image):
        super().__init__(color, coords, row, col, image)
        self.points = 3
    
    def move_is_legal(self, game_board, old_r, old_c, new_r, new_c):
        desired_loc = game_board.board[new_r][new_c]
        if desired_loc.piece is not None and desired_loc.piece.color == self.color:
            return False 

        if abs(old_r - new_r) == 1 and abs(old_c - new_c) == 2:
            return True
        elif abs(old_r - new_r) == 2 and abs(old_c - new_c) == 1:
            return True
        
        return False 
    
    def has_legal_moves(self, game_board, king):
        board = game_board.board

        if 0 <= self.row + 1 < len(board) and 0 <= self.col + 2 < len(board[0]):
            if (self.move_is_legal(game_board, self.row, self.col, self.row + 1, self.col + 2) and 
                self.check_king_safe(game_board, self.row + 1, self.col + 2, king)):
                return True

        if 0 <= self.row + 1 < len(board) and 0 <= self.col - 2 < len(board[0]):
            if (self.move_is_legal(game_board, self.row, self.col, self.row + 1, self.col - 2) and 
                self.check_king_safe(game_board, self.row + 1, self.col - 2, king)):
                return True
            
        if 0 <= self.row - 1 < len(board) and 0 <= self.col + 2 < len(board[0]):
            if (self.move_is_legal(game_board, self.row, self.col, self.row - 1, self.col + 2) and 
                self.check_king_safe(game_board, self.row - 1, self.col + 2, king)):
                return True
        if 0 <= self.row - 1 < len(board) and 0 <= self.col - 2 < len(board[0]):
            if (self.move_is_legal(game_board, self.row, self.col, self.row - 1, self.col - 2) and 
                self.check_king_safe(game_board, self.row - 1, self.col - 2, king)):
                return True
            
        if 0 <= self.row + 2 < len(board) and 0 <= self.col + 1 < len(board[0]):
            tile = board[self.row + 2][self.col + 1]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      
            
        if 0 <= self.row + 2 < len(board) and 0 <= self.col - 1 < len(board[0]):
            if (self.move_is_legal(game_board, self.row, self.col, self.row + 2, self.col - 1) and 
                self.check_king_safe(game_board, self.row + 2, self.col - 1, king)):
                return True
            
        if 0 <= self.row - 2 < len(board) and 0 <= self.col + 1 < len(board[0]):
            if (self.move_is_legal(game_board, self.row, self.col, self.row - 2, self.col + 1) and 
                self.check_king_safe(game_board, self.row - 2, self.col + 1, king)):
                return True   
            
        if 0 <= self.row - 2 < len(board) and 0 <= self.col - 1 < len(board[0]):
            if (self.move_is_legal(game_board, self.row, self.col, self.row - 2, self.col - 1) and 
                self.check_king_safe(game_board, self.row - 2, self.col - 1, king)):
                return True
            
        return False 
 
        
        