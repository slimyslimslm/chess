from piece import Piece

class LightPawn(Piece):
    def __init__(self, color, coords, row, col, image):
        super().__init__(color, coords, row, col, image)
        self.first_move = True
        self.can_enpassant = False 
        self.used_enpassant = True 
        self.points = 1

    def update_first_move(self):
        self.first_move = False  

    def enemy_can_enpassant(self, game_board, r, c):
        board = game_board.board
        if board[r][c - 1].piece is not None and isinstance(board[r][c - 1].piece, DarkPawn):
            board[r][c - 1].piece.can_enpassant = True 
        if board[r][c + 1].piece is not None and isinstance(board[r][c + 1].piece, DarkPawn):
            board[r][c + 1].piece.can_enpassant = True 

    """
    Implement actually removing the pieces 
    """
    def validate_en_passant(self, game_board, old_r, old_c, new_r, new_c):
        board = game_board.board 
        desired_loc = board[new_r][new_c]
        if old_c + 1 < len(board[0]) and (new_r, new_c) == (old_r - 1, old_c + 1) and desired_loc.piece is None and isinstance(board[old_r - 1][old_c + 1].piece, DarkPawn):
            self.first_move = False
            return True 
        elif old_c - 1 >= 0 and (new_r, new_c) == (old_r - 1, old_c - 1) and desired_loc.piece is None and isinstance(board[old_r - 1][old_c - 1].piece, DarkPawn):
            self.first_move = False
            return True
        
        return False 


    def move_is_legal(self, game_board, old_r, old_c, new_r, new_c):
        desired_loc = game_board.board[new_r][new_c]
        # Check if move leaves king vulenerable here. Would return False if yes 

        # Checks if we are capturing a piece, consider putting en passant here later
        tile_is_enemy = desired_loc.piece is not None and desired_loc.piece.color == "dark"
        if (new_r, new_c) == (old_r - 1, old_c + 1) and tile_is_enemy:
            return True
        elif (new_r, new_c) == (old_r - 1, old_c - 1) and tile_is_enemy:
            return True
        elif (new_r, new_c) == (old_r - 1, old_c) and desired_loc.piece is None:
            return True
        elif (new_r, new_c) == (old_r - 2, old_c) and self.first_move and desired_loc.piece is None:
            # algorithim to check if no pieces block way
            if self.path_is_free(game_board, old_r, old_c, new_r, new_c):
                return True 
            
        if self.can_enpassant:
            pass 
        
        return False 
    
    def has_legal_moves(self, game_board, king):
        board = game_board.board 
        if self.row - 2 >= 0 and self.first_move:
            two_squares = self.move_is_legal(game_board, self.row, self.col, self.row - 2, self.col) and self.check_king_safe(game_board, self.row - 2, self.col, king)
            if not two_squares:
                return False 
            
        if self.col - 1 >= 0:
            start = self.col - 1
        else:
            start = self.col
        
        if self.col + 1 < len(board[0]):
            end = self.col + 2
        else:
            end = self.col + 1

        for c in range(start, end):
            valid_move = self.move_is_legal(game_board, self.row, self.col, self.row - 1, c) and self.check_king_safe(game_board, self.row - 1, c, king)
            if not valid_move:
                return False 
            
        return True 

class DarkPawn(Piece):
    def __init__(self, color, coords, row, col, image):
        super().__init__(color, coords, row, col, image)
        self.first_move = True
        self.points = 1

    def update_first_move(self):
        self.first_move = False  

    def move_is_legal(self, game_board, old_r, old_c, new_r, new_c):
        desired_loc = game_board.board[new_r][new_c]
        # Check if move leaves king vulenerable here. Would return False if yes 

        # Checks if we are capturing a piece, consider putting en passant here later
        tile_is_enemy = desired_loc.piece is not None and desired_loc.piece.color == "light"
        if (new_r, new_c) == (old_r + 1, old_c + 1) and tile_is_enemy:
            return True
        elif (new_r, new_c) == (old_r + 1, old_c - 1) and tile_is_enemy:
            return True
        elif (new_r, new_c) == (old_r + 1, old_c) and desired_loc.piece is None:
            return True
        elif (new_r, new_c) == (old_r + 2, old_c) and self.first_move and desired_loc.piece is None:
            # Implement algorithim to check if no pieces block way
            if self.path_is_free(game_board, old_r, old_c, new_r, new_c):
                return True 
        
        return False 
    
    def has_legal_moves(self, game_board, king):
        board = game_board.board 
        if self.row + 2 >= len(board) and self.first_move:
            two_squares = self.move_is_legal(game_board, self.row, self.col, self.row + 2, self.col) and self.check_king_safe(game_board, self.row + 2, self.col, king)
            if not two_squares:
                return False 
            
        if self.col - 1 >= 0:
            start = self.col - 1
        else:
            start = self.col
        
        if self.col + 1 < len(board[0]):
            end = self.col + 2
        else:
            end = self.col + 1

        for c in range(start, end):
            valid_move = self.move_is_legal(game_board, self.row, self.col, self.row + 1, c) and self.check_king_safe(game_board, self.row + 1, c, king)
            if not valid_move:
                return False 
            
        return True 

