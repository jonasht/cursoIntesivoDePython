import sys
from ship import Ship
import pygame


def check_keydown_events(event, ship):
    """ responde a pressionamentos de tecla """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """ responde a solturas das teclas """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.KEY_LEFT:
        ship.moving_left = False


def check_events(ship):
    # responder events/eventos quando eh pressionado as teclas e o mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """atualiza as imagens na tela para nova tela"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # deixar a tela mais receente visivel
    pygame.display.flip()
