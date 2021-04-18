import pygame
import sys

# cores rgb
# Branco    = [255, 255, 255]
# Amarelo   = [255, 255, 0]
# Magenta   = [255, 0, 255]
# Vermelho  = [255, 0, 0]
# Ciano     = [0, 255, 255]
# Verde     = [0, 255, 0]
Azul 	    = [0, 0, 255]
# Preto 	= [0, 0, 0]
# criando uma janela do pygame e respondendo as entradas do usuario.


def run_game():
    pygame.init()

    screen = pygame.display.set_mode((1200, 500))
    pygame.display.set_caption('alien invasion')

    bg_color = (Azul)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()


run_game()
