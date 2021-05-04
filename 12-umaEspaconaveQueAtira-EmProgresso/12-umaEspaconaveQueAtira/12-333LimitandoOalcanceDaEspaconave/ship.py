import pygame
from  settings import Settings


class Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # carregando imagem de ship/nave
        self.image = pygame.image.load('images/ship.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # inicia cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # armazena um valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

        # flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # atualizar a posicao da nava de acordo com as flags de movimento

        # mover para direita
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor

        # movimentar para esquerda
        if self.moving_left and self.rect.left < self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

        # atualiza o objeto rect de acordo com self.center
        self.rect.centerx = self.center

    def blitme(self):
        # desene a espaçonava em sua posicao atual
        self.screen.blit(self.image, self.rect)
