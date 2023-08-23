import pygame, sys, math
from pygame.locals import QUIT

#initialize pygame
pygame.init()

#create a surface on the screen that has the size of 800 x 400
surface = pygame.display.set_mode((800, 400))

#define some colors
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

#function to draw a star at a given position, size and angle (the star is completely filled in with the given color)
def draw_star(screen, position, size, angle, color):
    points = []
    for i in range(5):
        points.append((position[0] + size * math.cos(math.radians(i * 72 - 54 + angle)), position[1] + size * math.sin(math.radians(i * 72 - 54 + angle))))
        points.append((position[0] + size / 2 * math.cos(math.radians(i * 72 - 18 + angle)), position[1] + size / 2 * math.sin(math.radians(i * 72 - 18 + angle))))
    
    pygame.draw.polygon(screen, color, points)

    

#a function to draw the flag of the Comoros
def drawComorosFlag():
    #draw the yellow background
    pygame.draw.rect(surface, yellow, (0, 0, 550, 100))
    #draw the white background
    pygame.draw.rect(surface, white, (0, 100, 550, 100))
    #draw the red background
    pygame.draw.rect(surface, red, (0, 200, 550, 100))
    #draw the blue background
    pygame.draw.rect(surface, blue, (0, 300, 550, 100))
    #draw the green triangle on the left side of the flag with the top point at (0, 0)
    pygame.draw.polygon(surface, green, ((0, 0), (0, 400), (275, 200)))
    #draw the white circle in the center of the triangle
    pygame.draw.circle(surface, white, (95, 200), 80)
    #draw the green circle in the center of the white circle
    pygame.draw.circle(surface, green, (120, 200), 80)
    #draw the a star in the center of the green circle with a size of 40
    draw_star(surface, (105, 150), 16, 35, white)
    draw_star(surface, (105, 185), 16, 35, white)
    draw_star(surface, (105, 220), 16, 35, white)
    draw_star(surface, (105, 255), 16, 35, white)
    
#call the function to draw the flag of the Comoros
drawComorosFlag()




#loop to keep the program running
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()