from piece import Piece

class Queen(Piece):
    def __init__(self, color, coords, row, col, image):
        super().__init__(color, coords, row, col, image)
        self.points = 9
    
    def move_is_legal(self, game_board, old_r, old_c, new_r, new_c):
        desired_loc = game_board.board[new_r][new_c]
        if desired_loc.piece is not None and desired_loc.piece.color == self.color:
            return False
        return self.path_is_free(game_board, old_r, old_c, new_r, new_c)
    
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
            

        # Northeast 
        row, col = self.row, self.col
        while (0 <= row < len(board) and 0 <= col < len(board[0])):
            valid_move = self.move_is_legal(game_board, self.row, self.col, row, col) and self.check_king_safe(game_board, row, col, king)
            if valid_move:
                return True

            row -= 1
            col += 1

        # Northwest
        row, col = self.row, self.col
        while (0 <= row < len(board) and 0 <= col < len(board[0])):
            valid_move = self.move_is_legal(game_board, self.row, self.col, row, col) and self.check_king_safe(game_board, row, col, king)
            if valid_move:
                return True

            row -= 1
            col -= 1

        # Southeast
        row, col = self.row, self.col
        while (0 <= row < len(board) and 0 <= col < len(board[0])):
            valid_move = self.move_is_legal(game_board, self.row, self.col, row, col) and self.check_king_safe(game_board, row, col, king)
            if valid_move:
                return True

            row += 1
            col += 1

        # Southwest 
        row, col = self.row, self.col
        while (0 <= row < len(board) and 0 <= col < len(board[0])):
            valid_move = self.move_is_legal(game_board, self.row, self.col, row, col) and self.check_king_safe(game_board, row, col, king)
            if valid_move:
                return True

            row -= 1
            col -= 1

        return False 