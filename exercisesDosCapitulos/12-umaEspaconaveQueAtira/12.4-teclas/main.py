import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    run = True
    while run:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                print(f'apertado:{event.key} ')
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    run = False

        pygame.display.update()


run_game()
