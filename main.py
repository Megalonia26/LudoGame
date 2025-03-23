"""Ludo Game made with python

"""
import pygame
import sys, time
from diceRolling import roll_dice
import const

pygame.init()
pygame.font.init()

W = const.WIDTH
H = const.HEIGHT
 
game_active = True

screen = pygame.display.set_mode((W, H))
startBg = pygame.transform.scale(pygame.image.load("img/start.jpg"), (W, H))
screen.blit(startBg, (0, 0))

BG = pygame.transform.scale(pygame.image.load("./img/bg.png"), (W, H))

text_font = pygame.font.SysFont(None, 30)

class Game:
    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]
        self.player3 = players[2]
        self.player4 = players[3]

    def drawPlayersName(self):
        """Drawing Player's name

        """
        player1 = text_font.render(f"{self.player1}", 1, "white")
        player1_rect = player1.get_rect(center=(100, 10))
        screen.blit(player1, player1_rect)
        
        player2 = text_font.render(f"{self.player2}", 1, "white")
        player2_rect = player2.get_rect(center=(W - player2.get_width(), 10))
        screen.blit(player2, player2_rect)
        
        player3 = text_font.render(f"{self.player3}", 1, "white")
        player3_rect = player3.get_rect(center=(W - player3.get_width(), H - player3.get_height()))
        screen.blit(player3, player3_rect)
        
        player4 = text_font.render(f"{self.player4}", 1, "white")
        player4_rect = player4.get_rect(center=(100, H - player4.get_height()))
        screen.blit(player4, player4_rect)

        pygame.display.update()

    def drawDice(self, k, dice):
        """Drawing function

        """
        screen.blit(BG, (0, 0))
        
        dice_text = text_font.render(f"{players[k]}:{dice}", 1, "white")
        dice_surf = dice_text.get_rect(center=(W / 2, H - dice_text.get_height()))
        screen.blit(dice_text, dice_surf)
        pygame.display.update()

    def run(self):
        """Main function

        """
        run = True
        clock = pygame.time.Clock()
        k = 0
        
        while run:
            clock.tick(const.FPS)
            if game_active:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        dice = roll_dice()
                        if k > 3:
                            k = 0
                        self.drawDice(k, dice)
                        k += 1
                        self.drawPlayersName()
                        time.sleep(1/2)

                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            else:
                over = text_font.render("GAME OVER", 3, "black")
                screen.fill("white")
                over_rect = over.get_rect(center=(W / 2, H / 2))
                screen.blit(over, over_rect)
            pygame.display.update()

if __name__ == "__main__":    
    players = ["Charles", "Finoana", "Rakoto", "Narindra"]
    game = Game(players)
    game.run()