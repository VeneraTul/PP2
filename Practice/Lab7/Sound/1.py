import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
image=pygame.image.load("image1.jpg")

white = (255, 255, 255)
black = (0, 0, 0)

songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
song_index = 0
pygame.mixer.music.load(songs[song_index])

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play()
                elif event.key == pygame.K_RIGHT:
                    song_index = (song_index + 1) % len(songs)
                    pygame.mixer.music.load(songs[song_index])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_LEFT:
                    song_index = (song_index - 1) % len(songs)
                    pygame.mixer.music.load(songs[song_index])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_s:
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_v:
                    pygame.mixer.music.unpause()
   
    screen.fill(white)

    screen.blit(image, (50, 30))

    
    
    pygame.display.flip()

pygame.quit()
