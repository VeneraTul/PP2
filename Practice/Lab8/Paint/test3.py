import pygame

colorBLACK = (0, 0, 0)
colorGRAY = (200, 200, 200)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

def getRectangle(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_radius(x1, y1, x2, y2):
    return int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)

def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius, 10)

    
pygame.init()
screen = pygame.display.set_mode((960, 640))
another_layer = pygame.Surface((960, 640))


done = False
clock = pygame.time.Clock()

x1 = 10
y1 = 10
x2 = 10
y2 = 10

color = colorBLUE
isMouseDown = False
LMBpressed = False
screen.fill((0, 0, 0))
image=pygame.image.load("delet.png")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                    color = colorYELLOW
            elif event.key == pygame.K_r:
                    color = colorRED
            elif event.key == pygame.K_g:
                    color = colorGREEN
            elif event.key == pygame.K_b:
                 color = colorBLUE
            
        

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # левая кнопка мыши
                x1 = event.pos[0]
                y1 = event.pos[1]
                isMouseDown = True
            elif event.button == 3: # правая кнопка мыши
                x1 = event.pos[0]
                y1 = event.pos[1]
                LMBpressed = True


        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # левая кнопка мыши
                isMouseDown = False
                another_layer.blit(screen, (0, 0))
            elif event.button == 3: # правая кнопка мыши
                LMBpressed = False
                another_layer.blit(screen, (0, 0))
                draw_circle(screen, color, (x1, y1), calculate_radius(x1, y1, x2, y2))
                screen.blit(another_layer, (0, 0)) # Очищаем второй круг после отпускания правой кнопки

        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:
                x2 = event.pos[0]
                y2 = event.pos[1]
                screen.blit(another_layer, (0, 0))
                pygame.draw.rect(screen, color, pygame.Rect(getRectangle(x1, y1, x2, y2)), 10)
            elif LMBpressed:
                screen.blit(another_layer, (0, 0))
                radius = calculate_radius(x1, y1, event.pos[0], event.pos[1])
                draw_circle(screen, color, (x1, y1), radius)
        
    pygame.display.flip()
    clock.tick(60)

    

pygame.quit()
