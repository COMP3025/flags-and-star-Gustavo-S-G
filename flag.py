import pygame, sys
from pygame.locals import QUIT

pygame.init()

surface = pygame.display.set_mode((400,300))

color = (255,255,255)
pygame.draw.rect(surface, color, pygame.Rect(20, 10, 300, 45))

pygame.draw.rect(surface, color, pygame.Rect(20, 100, 300, 45))

color2 = (255,0,0)
pygame.draw.rect(surface, color2, pygame.Rect(20, 55, 300, 45))

pygame.draw.rect(surface, color2, pygame.Rect(20, 145, 300, 45))

color3 = (0,0,255)
pygame.draw.rect(surface, color3, pygame.Rect(20, 10, 90, 90))

pygame.draw.polygon(surface, color, [[65, 20], [30, 90], [100, 90]], 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
