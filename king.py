from piece import Piece
from queen import Queen
from rook import Rook
from bishop import Bishop
from pawn import DarkPawn
from pawn import LightPawn
from knight import Knight

class King(Piece):
    def __init__(self, color, coords, row, col, image):
        super().__init__(color, coords, row, col, image)
        self.first_move = True

    def update_first_move(self):
        self.first_move = False 

    def no_check_while_castle(self, game_board, rook):
        # Kingside castling
        if self.col < rook.col:
            for col in range(self.col + 1, rook.col):
                if not self.check_king_safe(game_board, self.row, col, self):
                    return False 
        # Queenside castling 
        else:
            for col in range(rook.col + 2, self.col):
                if not self.check_king_safe(game_board, self.row, col, self):
                    return False
                
        return True 
    
    def move_is_legal(self, game_board, old_r, old_c, new_r, new_c):
        desired_loc = game_board.board[new_r][new_c]
        
        """
        Check if king is/can castle first
        """

        if (abs(old_r - new_r) <= 1 and abs(old_c - new_c) <= 1) and (desired_loc.piece is None or desired_loc.piece.color != self.color):
            return True
        return False 
    
    def check_straight_threats(self, game_board):
        board = game_board.board
        hor_threat = False 
        passed_king = False 

        for tile in board[self.row]:
            is_enemy_queen =  tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Queen)
            is_enemy_rook =  tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Rook) 
    
            if tile.piece is not None and (is_enemy_queen or is_enemy_rook):
                hor_threat = True
            elif tile.piece is not None and tile == board[self.row][self.col]:
                passed_king = True
            elif tile.piece is not None:
                hor_threat = False 
                if passed_king:
                    break
            
            if passed_king and hor_threat:
                break

        vert_threat = False
        passed_king = False
        for i in range(len(board)):
            tile = board[i][self.col]
            is_enemy_queen = tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Queen)
            is_enemy_rook = tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Rook) 

            if tile.piece is not None and (is_enemy_queen or is_enemy_rook):
                vert_threat = True
            elif tile.piece is not None and tile == board[self.row][self.col]:
                passed_king = True
            elif tile.piece is not None:
                vert_threat = False
                if passed_king:
                    break
            
            if passed_king and vert_threat:
                break
        
        return hor_threat or vert_threat
    
    def loop_through_diagonal(self, game_board, r_add, c_add):
        board = game_board.board
        row, col = self.row, self.col
        r_init = row

        while 0 <= row < len(board) and 0 <= col < len(board[0]):
            tile = board[row][col] 
            is_enemy_queen = tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Queen)
            is_enemy_bishop = tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Bishop)
            enemy_dark_pawn_near = row == r_init - 1 and tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, DarkPawn)
            enemy_light_pawn_near = row == r_init + 1 and tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, LightPawn)
        
            if is_enemy_queen or is_enemy_bishop:
                return True
            elif enemy_dark_pawn_near or enemy_light_pawn_near:
                return True
            elif tile.piece is not None and tile != board[self.row][self.col]:
                break
            
            row += r_add
            col += c_add

        return False
    

    def check_diagonal_threats(self, game_board):

        ne_diag = self.loop_through_diagonal(game_board, -1, 1)
        se_diag = self.loop_through_diagonal(game_board, 1, 1)
        sw_diag = self.loop_through_diagonal(game_board, 1, -1)
        nw_diag = self.loop_through_diagonal(game_board, -1, -1)
       
        return ne_diag or se_diag or sw_diag or nw_diag
    
    def check_knight_threats(self, game_board):
        board = game_board.board

        if 0 <= self.row + 1 < len(board) and 0 <= self.col + 2 < len(board[0]):
            tile = board[self.row + 1][self.col + 2]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      

        if 0 <= self.row + 1 < len(board) and 0 <= self.col - 2 < len(board[0]):
            tile = board[self.row + 1][self.col - 2]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      

        if 0 <= self.row - 1 < len(board) and 0 <= self.col + 2 < len(board[0]):
            tile = board[self.row - 1][self.col + 2]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      
        
        if 0 <= self.row - 1 < len(board) and 0 <= self.col - 2 < len(board[0]):
            tile = board[self.row - 1][self.col - 2]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      
            
        if 0 <= self.row + 2 < len(board) and 0 <= self.col + 1 < len(board[0]):
            tile = board[self.row + 2][self.col + 1]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      
            
        if 0 <= self.row + 2 < len(board) and 0 <= self.col - 1 < len(board[0]):
            tile = board[self.row + 2][self.col - 1]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      
            
        if 0 <= self.row - 2 < len(board) and 0 <= self.col + 1 < len(board[0]):
            tile = board[self.row - 2][self.col + 1]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      
            
        if 0 <= self.row - 2 < len(board) and 0 <= self.col - 1 < len(board[0]):
            tile = board[self.row - 2][self.col - 1]
            if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, Knight):
                return True      
            
        return False 
    
    def check_king_threats(self, game_board):
        board = game_board.board 

        if self.row - 1 >= 0:
            start_row = self.row - 1
        else:
            start_row = self.row 

        if self.row + 1 < len(board):
            end_row = self.row + 2
        else:
            end_row = self.row + 1

        if self.col - 1 >= 0:
            start_col = self.col - 1
        else:
            start_col = self.col

        if self.col + 1 < len(board[0]):
            end_col = self.col + 2
        else:
            end_col = self.col + 1

        
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                tile = board[r][c]
                if tile.piece is not None and tile.piece == self:
                    continue
                if tile.piece is not None and tile.piece.color != self.color and isinstance(tile.piece, King):
                    return True 
                
        return False 

    
    def check_all_threats(self, game_board):
        return (self.check_straight_threats(game_board) or self.check_diagonal_threats(game_board) 
                or self.check_knight_threats(game_board) or self.check_king_threats(game_board))
    
    def has_legal_moves(self, game_board, king):
        board = game_board.board
        if self.row - 1 >= 0:
            start_row = self.row - 1
        else:
            start_row = self.row 
        
        if self.row + 1 < len(board):
            end_row = self.row + 2
        else:
            end_row = self.row + 1

        if self.col - 1 >= 0:
            start_col = self.col - 1
        else:
            start_col = self.col
        
        if self.col + 1 < len(board[0]):
            end_col = self.col + 2
        else:
            end_col = self.col + 1

        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                tile = board[r][c]
                if tile.piece == self:
                    continue
                valid_move = self.move_is_legal(game_board, self.row, self.col, r, c) and self.check_king_safe(game_board, r, c, king)
                if valid_move:
                    return True
                
        return False 

    def is_castling(self, game_board, new_c):

        if abs(new_c - self.col) != 2:
             return False 
    
        if new_c > self.col:
            rook_tile = game_board.board[self.row][7]
        elif new_c < self.col:
            rook_tile = game_board.board[self.row][0]
        else:
            return False 
        
        if not isinstance(rook_tile.piece, Rook):
            return False

        if rook_tile.piece.first_move is False:
            return False 

        return (self.path_is_free(game_board, self.row, self.col, self.row, new_c) and
            self.no_check_while_castle(game_board, rook_tile.piece))
    
    def castle(self, game_board, new_c):
        board = game_board.board
    
        old_king_col = self.col
        if new_c > self.col:
            rook = board[self.row][7].piece
            old_rook_col = 7
            new_rook_col = 5
            new_king_col = self.col + 2
        else:
            rook = board[self.row][0].piece
            old_rook_col = 0
            new_rook_col = 3
            new_king_col = self.col - 2

        old_rook_tile = board[rook.row][old_rook_col]

        self.update_first_move()
        board[self.row][new_king_col].piece = self
        self.rect.x, self.rect.y = board[self.row][new_king_col].rect.x, board[self.row][new_king_col].rect.y
        board[self.row][old_king_col].piece = None
        self.col = new_king_col
        game_board.revert_tile(board[self.row][old_king_col])

        rook.update_first_move()
        board[rook.row][new_rook_col].piece = rook
        old_rook_tile.piece.rect.x, old_rook_tile.piece.rect.y = board[rook.row][new_rook_col].rect.x, board[rook.row][new_rook_col].rect.y
        old_rook_tile.piece = None
        rook.col = new_rook_col
        game_board.revert_tile(old_rook_tile)

    def move_piece(self, game_board, sprite_group, white_points, black_points, new_r, new_c, king):
        if self.first_move and self.is_castling(game_board, new_c):
            self.castle(game_board, new_c)
            return None, white_points, black_points
        
        return super().move_piece(game_board, sprite_group, white_points, black_points, new_r, new_c, king)