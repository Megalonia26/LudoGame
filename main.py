"""Ludo Game made with python
"""

import sys
import time
import pygame
from diceRolling import roll_dice
import const

from app import Button

pygame.font.init()

W = const.WIDTH
H = const.HEIGHT

P_W = const.PIECES_WIDTH
P_H = const.PIECES_HEIGHT

game_active = True

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Ludo")
startBg = pygame.transform.scale(pygame.image.load("./img/start.jpg"), (W, H))
screen.blit(startBg, (0, 0))

BG = pygame.transform.scale(pygame.image.load("./img/bg.png"), (W, H))

text_font = pygame.font.SysFont("comicsans", 30)
dice_font = pygame.font.SysFont(None, 50)

class Game:
    """Game class
    """
    def __init__(self, players):
        """Game initialisation
        """
        self.p1 = players[0]
        self.p2 = players[1]
        if len(players) == 4:
            self.p3 = players[2]
            self.p4 = players[3]

    def drawPlayersName(self):
        """Drawing Player's name
        """
        player1_surf = text_font.render(f"{self.p1}", 1, "white")
        player1_rect = player1_surf.get_rect(center=(100, 10))
        screen.blit(player1_surf, player1_rect)

        player2_surf = text_font.render(f"{self.p2}", 1, "white")
        if len(players) == 4:
            player2_rect = player2_surf.get_rect(center = (W - 100, 10)) 
        else:
            player2_rect = player2_surf.get_rect(center = (W - 100, H - player2_surf.get_height()))
        screen.blit(player2_surf, player2_rect)

        if len(players) == 4:
            player3_surf = text_font.render(f"{self.p3}", 1, "white")
            player3_rect = player3_surf.get_rect(center=(W - 100, H - player3_surf.get_height()))
            screen.blit(player3_surf, player3_rect)

            player4_surf = text_font.render(f"{self.p4}", 1, "white")
            player4_rect = player4_surf.get_rect(center=(100, H - player4_surf.get_height()))
            screen.blit(player4_surf, player4_rect)

        pygame.display.update()

    def DrawBackground(self):
        """Drawing function
        """
        screen.blit(BG, (0, 0))
        pygame.display.update()

    def run(self):
        """Main function
        """
        run = True
        clock = pygame.time.Clock()
        
        while run:
            clock.tick(const.FPS)
            if game_active:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and button1.top_rect.collidepoint(event.pos):
                        self.DrawBackground()
                        dice = roll_dice()
                        self.drawPlayersName()
                        button1 = Button(screen, f"{dice}", 100, 40, (W/2.5, H - 50))
                        button1.draw()
                        # time.sleep(1/5)

                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            else:
                screen.fill("white")
                pygame.time.delay(4000)
                run = False
                break
            pygame.display.update()

if __name__ == "__main__":
    players = []
    
    # while not (player.isdigit() and (int(player) == 2 or int(player) == 4)):
    #     player = input("Enter number of players (2 or 4) : ")

    player = 4

    for i in range(player):
        name = f"Player {i + 1}"
        players.append(name)

    game = Game(players)
    game.run()
