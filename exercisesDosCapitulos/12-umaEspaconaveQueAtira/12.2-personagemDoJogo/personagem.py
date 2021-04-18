import sys
import pygame
from settings import Configs
from homem import Homem


def run_game():
    pygame.init()
    pygame.display.set_caption('personagem')
    
    config = Configs()

    screen = pygame.display.set_mode(
        (config.tela_largura, config.tela_altura)
    )
    homem = Homem(screen)


    while True:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()
        
        screen.fill(config.bg_color)
        homem.blitme()
        pygame.display.flip()

run_game()