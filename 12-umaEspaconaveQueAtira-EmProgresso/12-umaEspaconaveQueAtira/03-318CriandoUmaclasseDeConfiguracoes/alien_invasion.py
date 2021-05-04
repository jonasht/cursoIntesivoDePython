
import sys
import pygame
from settings import Settings

def run_game():
    pygame.init()
    
    ai_settings = Settings() 

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    
    pygame.display.set_caption('alien invasion')

    # definir a cor bg do jogo - em formato RGB
    bg_color = (230, 230, 230)

    # para iniciar o jogo precisa do laço while
    while True:
        
        # para ver os eventos do teclado e do mouse
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()
        
        screen.fill(ai_settings.bg_color)

        # deixar a tela mais recente visivel 
        pygame.display.flip()

run_game()