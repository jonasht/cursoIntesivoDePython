import sys

import pygame

def check_events():
    # responder events/eventos quando eh pressionado as teclas e o mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            