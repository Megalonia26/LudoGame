"""
    This module handle the player's position and the 
"""
import pygame
import const

class Pieces:
    """Handling pieces
    """
    def __init__(self, players):      
        self.player_colors = {
            "Player 1": "red",
            "Player 2": "green",
            "Player 3": "yellow",
            "Player 4": "blue",
        }
        
        self.pieces = {
            "Player 1": [pygame.R]
        }