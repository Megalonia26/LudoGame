"""This file handle the players pos and all

"""
# import pygame
import const

class Pieces:
    """
    Handling pieces
    """
    def __init__(self, players):
        """for parameter I'll user the players, colors
        """
        self.p1 = players[0]
        self.p2 = players[1]
        if len(players) > 2:
            self.p3 = players[2]
            self.p4 = players[3]
        self.p_colors = list(zip(range(len(players)), const.COLORS))

    def Players(self):
        """Maybe to handle the player's pieces/color
        """
        return self.p_colors
