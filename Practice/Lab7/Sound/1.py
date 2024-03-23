import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
image=pygame.image.load("image1.jpg")

white = (255, 255, 255)
black = (0, 0, 0)

songs = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song_index = 0
pygame.mixer.music.load(songs[current_song_index])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play()
                elif event.key == pygame.K_RIGHT:
                    current_song_index = (current_song_index + 1) % len(songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_LEFT:
                    current_song_index = (current_song_index - 1) % len(songs)
                    pygame.mixer.music.load(songs[current_song_index])
                    pygame.mixer.music.play()
                elif event.key == pygame.K_s:
                    pygame.mixer.music.stop()
   
    screen.fill(white)

    screen.blit(image, (50, 30))

    
    
    pygame.display.flip()

pygame.quit()
