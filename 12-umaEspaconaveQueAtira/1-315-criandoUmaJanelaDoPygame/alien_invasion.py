# criando uma janela do pygame e respondendo as entradas do usuario.

import sys
import pygame

def run_game():
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('alien invasion')

    # para iniciar o jogo precisa do laço while
    while True:
        
        # para ver os eventos do teclado e do mouse
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()
        
        # deixar a tela mais recente visivel 
        pygame.display.flip()

run_game()