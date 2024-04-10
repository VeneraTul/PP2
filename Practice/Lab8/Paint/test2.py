import pygame
import sys

pygame.init()

WIDTH = 960
HEIGHT = 640


colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorYELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

done = False

LMBpressed = False

prevX = 0
prevY = 0

currX = 0
currY = 0 

def calculate_radius(x1, y1, x2, y2):
    return int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            LMBpressed = False
            radius = calculate_radius(prevX, prevY, currX, currY)
            pygame.draw.circle(screen, colorYELLOW, (prevX, prevY), radius,10)
            base_layer.blit(screen, (0, 0))

    if LMBpressed:
        screen.blit(base_layer, (0, 0))
        radius = calculate_radius(prevX, prevY, currX, currY)
        pygame.draw.circle(screen, colorYELLOW, (prevX, prevY), radius,10)

    pygame.display.flip()
