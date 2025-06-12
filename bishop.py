from piece import Piece

class Bishop(Piece):
    def __init__(self, color, coords, row, col, image):
        super().__init__(color, coords, row, col, image)
        self.points = 3

    def move_is_legal(self, game_board, old_r, old_c, new_r, new_c):
        desired_loc = game_board.board[new_r][new_c]
        if (desired_loc.piece is not None and desired_loc.piece.color == self.color):
            return False 
        return self.check_diagonal_path(game_board.board, old_r, old_c, new_r, new_c)
    
    def has_legal_moves(self, game_board, king):
        board = game_board.board 

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