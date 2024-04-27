import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

clock = pygame.time.Clock()

x=30
y=30

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
color = red
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                color = blue
                      
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
            x+=20
    if keys[pygame.K_LEFT]:
            x-=20
    if keys[pygame.K_UP]:
            y-=20
    if keys[pygame.K_DOWN]:
            y+=20

    screen.fill(white)

    pygame.draw.circle(screen,color,(x,y),25)
    pygame.display.flip()
    clock.tick(60)
    



            

