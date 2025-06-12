import pygame 
import colors
from board import Board 
from pawn import LightPawn, DarkPawn
from queen import Queen

WIDTH, HEIGHT = 600, 700

FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Game:
    def __init__(self):
        self.run = True 
        self.game_board = Board(WIDTH, HEIGHT) 
        self.white_turn = True
        self.white_king = self.game_board.board[7][4].piece
        self.black_king = self.game_board.board[0][4].piece
        self.white_points = 0
        self.black_points = 0
        self.check = False 
        self.draw = False 
        self.moves = []

    def selected_right_color(self, piece):
        if (self.white_turn and piece.color == "light"):
            return True
        elif (not self.white_turn and piece.color == "dark"):
            return True
        return False 

    def select_piece(self):
        for i, row in enumerate(self.game_board.board):
            for j, tile in enumerate(row):
                if tile.rect.collidepoint(pygame.mouse.get_pos()) and (tile.piece is not None) and self.selected_right_color(tile.piece):
                    tile.is_selected = True
                    tile.color = 255, 0, 0
                    return tile
        return None
    
    def select_tile(self):
        for i, row in enumerate(self.game_board.board):
            for j, tile in enumerate(row):
                if tile.rect.collidepoint(pygame.mouse.get_pos()):
                    return i, j
        return None, None
    
    def handle_moving_piece(self, selected_tile, new_r, new_c):
        if (new_r, new_c) == (selected_tile.piece.row, selected_tile.piece.col):
            self.game_board.revert_tile(selected_tile)
            selected_tile = None
            new_r, new_c = None, None 
        else:
            if selected_tile.piece.color == "light":
                king = self.white_king
            else:
                king = self.black_king
            selected_tile, self.white_points, self.black_points = selected_tile.piece.move_piece(self.game_board, self.game_board.sprite_group, self.white_points, self.black_points,
                                                                         new_r, new_c, king)
            if selected_tile is None:
                self.white_turn = not self.white_turn
                self.promote_pawns()
                self.check = self.check_for_check()
            
        return selected_tile

    def event_handler(self, selected_tile):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_focused() and selected_tile is None:
                selected_tile = self.select_piece()

            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_focused():
                new_r, new_c = self.select_tile()
                selected_tile = self.handle_moving_piece(selected_tile, new_r, new_c)
       
        return selected_tile
    
    def promote_pawns(self):
        for col, tile in enumerate(self.game_board.board[0]):
            if tile.piece is not None and isinstance(tile.piece, LightPawn):
                tile.piece.remove(self.game_board.sprite_group)
                img = r"Sprites\PNGs\No shadow\2x\w_queen_2x_ns.png"
                piece = Queen("light", (tile.rect.x, tile.rect.y), 0, col, img)
                piece.image = pygame.transform.scale(piece.image, (75, 75))
                piece.image.get_rect().center = tile.rect.center
                tile.piece = piece
                piece.add(self.game_board.sprite_group)
                break
        for col, tile, in enumerate(self.game_board.board[7]):
            if tile.piece is not None and isinstance(tile.piece, DarkPawn):
                tile.piece.remove(self.game_board.sprite_group)
                img = r"Sprites\PNGs\No shadow\2x\b_queen_2x_ns.png"
                piece = Queen("dark", (tile.rect.x, tile.rect.y), 7, col, img)
                piece.image = pygame.transform.scale(piece.image, (75, 75))
                piece.image.get_rect().center = tile.rect.center
                tile.piece = piece
                piece.add(self.game_board.sprite_group)
                break
            
    def check_for_checkmate_or_draw(self):
        move_exists = False 
        for piece in self.game_board.sprite_group:
            if piece.color == "light" and self.white_turn:
                move_exists = piece.has_legal_moves(self.game_board, self.white_king)
            elif piece.color == "dark" and not self.white_turn:
                move_exists = piece.has_legal_moves(self.game_board, self.black_king)
            
            if move_exists:
                return False
        
        if self.white_turn and not self.white_king.check_all_threats(self.game_board):
            self.draw = True
        elif not self.white_turn and not self.black_king.check_all_threats(self.game_board):
            self.draw = True 
        
        return True
    
    def check_for_check(self):
        if self.white_turn:
            return self.white_king.check_all_threats(self.game_board)
        else:
            return self.black_king.check_all_threats(self.game_board)

    def game_over(self, window):
        font = pygame.font.SysFont("comicsans", 50)
        if self.draw:
            text = font.render("Draw!", True, colors.BLUE)
        elif self.white_turn:
            text = font.render("Black wins!", True, colors.BLUE)
        else:
            text = font.render("White wins!", True, colors.BLUE)
        text_rect = text.get_rect()
        text_rect.center = WIDTH//2, HEIGHT//2
        window.blit(text, text_rect)
        

    def draw_text(self, window):
        font = pygame.font.SysFont("comicsans", 25)
        difference = self.white_points - self.black_points

        if difference == 0:
            point_text = font.render("", True, colors.BLUE)
        else:
            point_text = font.render(f"+{abs(difference)}", True, colors.BLUE)

        point_text_rect = point_text.get_rect()

        if self.white_points > self.black_points:
            point_text_rect.topleft = 550, 12
        else:
            point_text_rect.topleft = 550, 650

        window.blit(point_text, point_text_rect)

        check_text = font.render("Check", True, colors.BLUE)
        check_text_rect = check_text.get_rect()
        if self.check and self.white_turn:
            check_text_rect.center = 300, 675
            window.blit(check_text, check_text_rect)
        elif self.check and not self.white_turn:
            check_text_rect.center = 300, 25
            window.blit(check_text, check_text_rect)


    def play(self):
        pygame.font.init()
        pygame.display.set_caption("Slimmy's Chess")
        clock = pygame.time.Clock()
        selected_tile = None

        while self.run:
            clock.tick(FPS)

            game_over = self.check_for_checkmate_or_draw()
            selected_tile = self.event_handler(selected_tile)
            self.game_board.draw(window)
            self.draw_text(window)

            if game_over:
                self.game_over(window)
                self.run = False 
            
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.play()
    pygame.time.wait(3000)