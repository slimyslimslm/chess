import pygame 
from bishop import Bishop
from king import King 
from knight import Knight
from pawn import LightPawn, DarkPawn
from rook import Rook 
from queen import Queen 
from tile import Tile 
from utility import increment_char
import colors

class Board:
    def __init__(self, WIDTH, HEIGHT):
        self.sprite_group = pygame.sprite.Group()
        self.board = self.create_board(WIDTH, HEIGHT)

    def add_pieces(self, board):
        for i, tile in enumerate(board[1]):
            img = r"Sprites\PNGs\No shadow\2x\b_pawn_2x_ns.png"
            piece = DarkPawn("dark", (tile.rect.x, tile.rect.y), 1, i, img)
            piece.image = pygame.transform.scale(piece.image, (75, 75))
            piece.image.get_rect().center = tile.rect.center
            tile.piece = piece
            piece.add(self.sprite_group)
        for i, tile in enumerate(board[6]):
            img = r"Sprites\PNGs\No shadow\2x\w_pawn_2x_ns.png"
            piece = LightPawn("light", (tile.rect.x, tile.rect.y), 6, i, img)
            piece.image = pygame.transform.scale(piece.image, (75, 75))
            piece.image = pygame.transform.scale(piece.image, (75, 75))
            tile.piece = piece
            piece.add(self.sprite_group)

        tile = board[7][0]
        img = r"Sprites\PNGs\No shadow\2x\w_rook_2x_ns.png"
        piece = Rook("light", (tile.rect.x, tile.rect.y), 7, 0, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        piece.image.get_rect().center = tile.rect.center
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[7][7]
        piece = Rook("light", (tile.rect.x, tile.rect.y), 7, 7, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        piece.image.get_rect().center = tile.rect.center
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[7][1]
        img = r"Sprites\PNGs\No shadow\2x\w_knight_2x_ns.png"
        piece = Knight("light", (tile.rect.x, tile.rect.y), 7, 1, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        piece.image.get_rect().center = tile.rect.center
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[7][6]
        piece = Knight("light", (tile.rect.x, tile.rect.y), 7, 6, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        piece.image.get_rect().center = tile.rect.center
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[7][2]
        img = r"Sprites\PNGs\No shadow\2x\w_bishop_2x_ns.png"
        piece = Bishop("light", (tile.rect.x, tile.rect.y), 7, 2, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        piece.image.get_rect().center = tile.rect.center
        tile.piece = piece
        piece.add(self.sprite_group)
    
        tile = board[7][5]
        img = r"Sprites\PNGs\No shadow\2x\w_bishop_2x_ns.png"
        piece = Bishop("light", (tile.rect.x, tile.rect.y), 7, 5, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        piece.image.get_rect().center = tile.rect.center
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[7][3]
        img = r"Sprites\PNGs\No shadow\2x\w_queen_2x_ns.png"
        piece = Queen("light", (tile.rect.x, tile.rect.y), 7, 3, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        piece.image.get_rect().center = tile.rect.center
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[7][4]
        img = r"Sprites\PNGs\No shadow\2x\w_king_2x_ns.png"
        piece = King("light", (tile.rect.x, tile.rect.y), 7, 4, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][0]
        img = r"Sprites\PNGs\No shadow\2x\b_rook_2x_ns.png"
        piece = Rook("dark", (tile.rect.x, tile.rect.y), 0, 0, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][7]
        piece = Rook("dark", (tile.rect.x, tile.rect.y), 0, 7, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][1]
        img = r"Sprites\PNGs\No shadow\2x\b_knight_2x_ns.png"
        piece = Knight("dark", (tile.rect.x, tile.rect.y), 0, 1, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][6]
        piece = Knight("dark", (tile.rect.x, tile.rect.y), 0, 6, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][2]
        img = r"Sprites\PNGs\No shadow\2x\b_bishop_2x_ns.png"
        piece = Bishop("dark", (tile.rect.x, tile.rect.y), 0, 2, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][5]
        piece = Bishop("dark", (tile.rect.x, tile.rect.y), 0, 5, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][3]
        img = r"Sprites\PNGs\No shadow\2x\b_queen_2x_ns.png"
        piece = Queen("dark", (tile.rect.x, tile.rect.y), 0, 3, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][4]
        img = r"Sprites\PNGs\No shadow\2x\b_king_2x_ns.png"
        piece = King("dark", (tile.rect.x, tile.rect.y), 0, 4, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)


    def test_pieces(self, board):
        tile = board[7][4]
        img = r"Sprites\PNGs\No shadow\2x\w_king_2x_ns.png"
        piece = King("light", (tile.rect.x, tile.rect.y), 7, 4, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[7][3]
        img = r"Sprites\PNGs\No shadow\2x\w_queen_2x_ns.png"
        piece = Queen("light", (tile.rect.x, tile.rect.y), 7, 3, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        piece.image.get_rect().center = tile.rect.center
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][3]
        img = r"Sprites\PNGs\No shadow\2x\b_queen_2x_ns.png"
        piece = Queen("dark", (tile.rect.x, tile.rect.y), 0, 3, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][4]
        img = r"Sprites\PNGs\No shadow\2x\b_king_2x_ns.png"
        piece = King("dark", (tile.rect.x, tile.rect.y), 0, 4, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)

        tile = board[0][7]
        img = r"Sprites\PNGs\No shadow\2x\b_rook_2x_ns.png"
        piece = Rook("dark", (tile.rect.x, tile.rect.y), 0, 7, img)
        piece.image = pygame.transform.scale(piece.image, (75, 75))
        tile.piece = piece
        piece.add(self.sprite_group)


    def create_board(self, WIDTH, HEIGHT):
        board = []
        '''
        Add this, initializes the board
        '''
        tile_num = 1
        num = 8
        x, y = 0, 50
        for _ in range(8):
            char = "a"
            row = []
    
            for _ in range(8):
                if tile_num % 2 == 0:
                    color = colors.DARK_SQUARE
                    type = "dark"
                else:
                    color = colors.LIGHT_SQUARE
                    type = "light"
                row.append(Tile(char + str(num), type, pygame.Rect(x, y, WIDTH//8, WIDTH//8), color, None))
                char = increment_char(char)
                tile_num += 1
                x += WIDTH//8
            y += WIDTH//8
            x = 0
            board.append(row)
            num -= 1
            tile_num += 1

        """
        Initialize starting positions of pieces 
        """
        self.add_pieces(board)
        
        return board
    
    def revert_tile(self, old_tile):
        if old_tile.type == "light":
            old_tile.color = colors.LIGHT_SQUARE
            old_tile.is_selected = False 
        else:
            old_tile.color = colors.DARK_SQUARE
            old_tile.is_selected = False
    
    def draw(self, window):
        window.fill((255, 255, 255))        
        for row in self.board:
            for tile in row:
                tile.draw(window)
        self.sprite_group.draw(window)

    