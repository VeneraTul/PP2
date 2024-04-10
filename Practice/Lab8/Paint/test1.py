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

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            pygame.draw.rect(screen, colorYELLOW, calculate_rect(prevX, prevY, currX, currY), 2)
            base_layer.blit(screen, (0, 0))

    if LMBpressed:
        screen.blit(base_layer, (0, 0))
        pygame.draw.rect(screen, colorYELLOW, calculate_rect(prevX, prevY, currX, currY), 2)

    pygame.display.flip()