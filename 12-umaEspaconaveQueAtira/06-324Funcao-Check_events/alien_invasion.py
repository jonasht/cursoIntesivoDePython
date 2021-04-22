
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption('alien invasion')

    # criar uma espaçonave
    ship = Ship(screen)

    # definir a cor bg do jogo - em formato RGB
    bg_color = (230, 230, 230)

    # para iniciar o jogo precisa do laço while
    while True:
        # ver os eventos do teclado e do mouse
        gf.check_events()

        screen.fill(ai_settings.bg_color)
        ship.blitme()               

        # deixar a tela mais recente visivel
        pygame.display.flip()


run_game()
