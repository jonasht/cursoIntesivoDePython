import pygame
from settings import  Settings
from nave import  Nave



def run_game():
    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode((settings.tela_larguraX, settings.tela_alturaY))


    naveX_change = 0
    naveY_change = 0

    nave = Nave(screen)
    run = True
    while run:
        screen.fill((settings.bg_color))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:  # 1-quando a tecla estah sendo apartada
                if event.key == pygame.K_UP:
                    naveY_change = -settings.velocidade

                if event.key == pygame.K_DOWN:
                    naveY_change = settings.velocidade

                if event.key == pygame.K_LEFT:
                    naveX_change = -settings.velocidade
                if event.key == pygame.K_RIGHT:
                    naveX_change = settings.velocidade
                
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    naveY_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    naveX_change = 0

        settings.naveY += naveY_change
        settings.naveX += naveX_change

        if settings.naveX <= 0:
            settings.naveX = 0
        elif settings.naveX >= 736:
            settings.naveX = 736

        if settings.naveY <= 0:
            settings.naveY = 0
        elif settings.naveY >= 535:
            settings.naveY = 535
            
        nave.colocar(settings.naveX, settings.naveY)
        pygame.display.update()

run_game()