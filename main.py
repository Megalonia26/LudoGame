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
pygame.display.set_caption("Ludo")
startBg = pygame.transform.scale(pygame.image.load("img/start.jpg"), (W, H))
screen.blit(startBg, (0, 0))

BG = pygame.transform.scale(pygame.image.load("./img/bg.png"), (W, H))

text_font = pygame.font.SysFont(None, 30)
dice_font = pygame.font.SysFont(None, 50)

class Game:
    """
    Game class
    """
    def __init__(self, players):
        """Game initialisation
        @param players: number of players
        """
        self.player1 = players[0]
        self.player2 = players[1]
        if len(players) == 4:
            self.player3 = players[2]
            self.player4 = players[3]

    def drawPlayersName(self):
        """Drawing Player's name

        """
        player1_surf = text_font.render(f"{self.player1}", 1, "white")
        player1_rect = player1_surf.get_rect(center=(100, 10))
        screen.blit(player1_surf, player1_rect)

        player2_surf = text_font.render(f"{self.player2}", 1, "white")
        player2_rect = player2_surf.get_rect(center = (W - player2_surf.get_width() - 10, 10)) if len(players) == 4 else player2_surf.get_rect(center = (W - player2_surf.get_width() - 10, H - player2_surf.get_height()))
        screen.blit(player2_surf, player2_rect)

        if len(players) == 4:
            player3_surf = text_font.render(f"{self.player3}", 1, "white")
            player3_rect = player3_surf.get_rect(center=(W - player3_surf.get_width() - 10, H - player3_surf.get_height()))
            screen.blit(player3_surf, player3_rect)

            player4_surf = text_font.render(f"{self.player4}", 1, "white")
            player4_rect = player4_surf.get_rect(center=(100, H - player4_surf.get_height()))
            screen.blit(player4_surf, player4_rect)

        pygame.display.update()

    def drawDice(self, player, dice):
        """Drawing function

        """
        screen.blit(BG, (0, 0))

        dice_text = dice_font.render(f"{players[player]} : {dice}", 1, "white")
        dice_surf = dice_text.get_rect(center=(W / 2, H - dice_text.get_height()))
        screen.blit(dice_text, dice_surf)
        pygame.display.update()

    def run(self):
        """Main function

        """
        run = True
        clock = pygame.time.Clock()
        player = 0

        while run:
            clock.tick(const.FPS)
            if game_active:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        dice = roll_dice()
                        self.drawDice(player, dice)
                        player += 1
                        if player > len(players) - 1:
                            player = 0
                        self.drawPlayersName()
                        time.sleep(1/2)
                    
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        print(event.pos)

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
    # player = ""
    players = []

    # while not (player.isdigit() and (int(player) == 2 or int(player) == 4)):
    #     player = input("Enter number of players (2 or 4) : ")
    player = 4

    for i in range(player):
        name = f"Player {i + 1}"
        players.append(name)

    game = Game(players)
    game.run()
