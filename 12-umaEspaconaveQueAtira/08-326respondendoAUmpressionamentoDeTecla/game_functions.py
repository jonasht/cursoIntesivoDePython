import sys

import pygame

def check_events(ship):
    # responder events/eventos quando eh pressionado as teclas e o mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
def update_screen(ai_settings, screen, ship):
    """atualiza as imagens na tela para nova tela"""        
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # deixar a tela mais receente visivel 
    pygame.display.flip()
    
    