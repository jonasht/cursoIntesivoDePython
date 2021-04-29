import pygame

class Nave():
    def __init__ (self, screen):
        self.screen = screen
        self.imagem = pygame.image.load('img/nave.png')

    def colocar(self, x, y):
        self.screen.blit(self.imagem, (x, y))
