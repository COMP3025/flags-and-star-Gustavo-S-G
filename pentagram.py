import pygame, sys, math
from pygame.locals import QUIT

pygame.init()

surface = pygame.display.set_mode((900,550))

white = (255, 255, 255)

#function to draw a pentagram at a given position and size
# def draw_star(screen, position, size):
#     points = []
#     for i in range(5):
#         points.append((position[0] + size * math.cos(math.radians(i * 72 - 54)), position[1] + size * math.sin(math.radians(i * 72 - 54))))
#         points.append((position[0] + size / 2 * math.cos(math.radians(i * 72 - 18)), position[1] + size / 2 * math.sin(math.radians(i * 72 - 18))))

#     pygame.draw.polygon(screen, white, points, 2)

#function to draw a pentagram at a given position, size, and angle
# def draw_star(screen, position, size, angle):
#     points = []
#     for i in range(5):
#         points.append((position[0] + size * math.cos(math.radians(i * 72 - 54 + angle)), position[1] + size * math.sin(math.radians(i * 72 - 54 + angle))))
#         points.append((position[0] + size / 2 * math.cos(math.radians(i * 72 - 18 + angle)), position[1] + size / 2 * math.sin(math.radians(i * 72 - 18 + angle))))

#     pygame.draw.polygon(screen, white, points, 2)

#function to draw a pentagram at a given position, size, and angle with lines connecting the points of the center pentagon
def draw_star(screen, position, size, angle):
    points = []
    for i in range(5):
        points.append((position[0] + size * math.cos(math.radians(i * 72 - 53 + angle)), position[1] + size * math.sin(math.radians(i * 72 - 53 + angle))))
        points.append((position[0] + size / 2 * math.cos(math.radians(i * 72 - 17 + angle)), position[1] + size / 2 * math.sin(math.radians(i * 72 - 17 + angle))))
    
    pygame.draw.polygon(screen, white, points, 2)
    for i in range(5):
        pygame.draw.line(screen, white, points[i * 2], points[i * 2 + 1], 2)
        pygame.draw.line(screen, white, points[i * 2 + 1], points[(i * 2 + 3) % 10], 2)

#draw a pentagram at the center of the screen
# draw_star(surface, (450, 275), 200)
draw_star(surface, (450, 275), 200, 35)
          


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()