import copy
import pygame 

class Piece(pygame.sprite.Sprite): 
    white_can_castle = False 
    black_can_castle = False
    
    def __init__(self, color, coords, row, col, image):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = coords 

        self.row = row
        self.col = col

        self.color = color
        self.legal_moves = []

    def check_diagonal_path(self, board, old_r, old_c, new_r, new_c):
        # Northeast diagonal
        if new_r < old_r and new_c > old_c:
            r_increm = -1
            c_increm = 1
        # Southeast 
        elif new_r > old_r and new_c > old_c:
            r_increm = 1
            c_increm = 1
        # Northwest
        elif new_r < old_r and new_c < old_c:
            r_increm = -1
            c_increm = -1 
        # Southwest
        elif new_r > old_r and new_c < old_c:
            r_increm = 1
            c_increm = -1
        else:
            return False 

        # Loops through diagonal
        row, col = old_r, old_c
        while 0 <= row < len(board) and 0 <= col < len(board[0]):
            if row == new_r and col == new_c:
                return True
            elif board[row][col].piece is not None and board[row][col].piece.color != self.color:
                return False
            row += r_increm
            col += c_increm
        # Returns False if move is not diagonal 
        return False 

    def path_is_free(self, game_board, old_r, old_c, new_r, new_c):
        board = game_board.board
        if new_r < old_r and old_c == new_c:
            for i in range(new_r + 1, old_r):
                if board[i][old_c].piece is not None:
                    return False 
        elif new_r > old_r and old_c == new_c:
            for i in range(old_r + 1, new_r):
                if board[i][old_c].piece is not None:
                    return False
        elif new_c < old_c and old_r == new_r:
            for i in range(new_c + 1, old_c):
                if board[old_r][i].piece is not None:
                    return False
        elif new_c > old_c and old_r == new_r:
            for i in range(old_c + 1, new_c):
                if board[old_r][i].piece is not None:
                    return False
        else:
            # Check for diagonals 
            return self.check_diagonal_path(board, old_r, old_c, new_r, new_c)
        
        return True 
    
    def check_king_safe(self, game_board, new_r, new_c, king):

        board_copy = copy.deepcopy(game_board)
        king_copy = board_copy.board[king.row][king.col].piece
        old_r, old_c = self.row, self.col
        new_tile = board_copy.board[new_r][new_c]
        old_tile = board_copy.board[old_r][old_c]

        new_tile.piece = old_tile.piece
        board_copy.board[old_r][old_c].piece = None
        new_tile.piece.row, new_tile.piece.col = new_r, new_c
 
        return not king_copy.check_all_threats(board_copy)
    
    def update_first_move(self):
        pass 

    def move_piece(self, game_board, sprite_group, white_points, black_points, new_r, new_c, king):
        old_r, old_c = self.row, self.col
        old_tile = game_board.board[old_r][old_c]
        new_tile = game_board.board[new_r][new_c]
    
        valid_move = self.move_is_legal(game_board, old_r, old_c, new_r, new_c) and self.check_king_safe(game_board, new_r, new_c, king)

        if (old_r, old_c) != (new_r, new_c) and valid_move:
            if new_tile.piece is not None: 
                if new_tile.piece.color == "light":
                    white_points += new_tile.piece.points
                else:
                    black_points += new_tile.piece.points 
                sprite_group.remove(new_tile.piece)

            old_tile.piece.update_first_move()
        
            new_tile.piece = self 
            self.rect.x, self.rect.y = new_tile.rect.x, new_tile.rect.y
            old_tile.piece = None 
            
            self.row = new_r
            self.col = new_c

            game_board.revert_tile(old_tile)
            old_tile = None
        
        return old_tile, white_points, black_points