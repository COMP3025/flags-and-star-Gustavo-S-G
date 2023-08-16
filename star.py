import pygame, sys, math

from pygame.locals import QUIT
pygame.init()

surface = pygame.display.set_mode((800,700))

white = (255,255,255)

#function to draw a pentagram with a given position, size and angle conecting the points of the star with lines
def draw_star(screen, position, size, angle):
    points = []
    for i in range(5):
        points.append((position[0] + size * math.cos(angle + i * 4 * math.pi / 5),
                       position[1] + size * math.sin(angle + i * 4 * math.pi / 5)))
        
    pygame.draw.polygon(screen, white, points, 2)
    pygame.draw.lines(screen, white, True, points, 2)

draw_star(surface, (400, 350), 100, 60)




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()