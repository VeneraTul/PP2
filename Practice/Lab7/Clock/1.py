import pygame
import datetime


pygame.init()
screen = pygame.display.set_mode((800,600))

clock=pygame.time.Clock()

white=(255,255,255)


image=pygame.image.load("mainclock(700,525).png")
imageL=pygame.image.load("leftarm1.png")
imageR=pygame.image.load("rightarm1.png")

done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill(white)

        screen.blit(image, (50, 30))

        curr_date=datetime.datetime.now()
        curr_min=curr_date.minute
        curr_sec=curr_date.second
        minute_angle = (curr_min+0.2 / 60) * (-360)  
        second_angle = (curr_sec/ 60) * (-360)  

        rotated_Rhand=pygame.transform.rotate(imageR,minute_angle)
        Rhand_move=rotated_Rhand.get_rect(center=(400, 300))
        screen.blit(rotated_Rhand, Rhand_move)

        rotated_Lhand = pygame.transform.rotate(imageL, second_angle)
        Lhand_move = rotated_Lhand.get_rect(center=(400, 300))
        screen.blit(rotated_Lhand, Lhand_move)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()
        
