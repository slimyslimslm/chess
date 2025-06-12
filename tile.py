from piece import Piece 
import pygame

class Tile():
    def __init__(self, name: str, type: str, rect: pygame.Rect, color: tuple[int], piece: Piece):
        self.name = name # Ex. "a1"
        self.type = type 
        self.rect = rect 
        self.color = color
        self.piece = piece
        self.is_selected = False 

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
