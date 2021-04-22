import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen

        # carregando imagem de ship/nave
        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # inicia cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # flag de movimento
        self.moving_right = False

    def update(self):

        # mover para direita
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        # desene a espaçonava em sua posicao atual
        self.screen.blit(self.image, self.rect)
