import pygame
import sys
import random

pygame.init()

# Color palette
colorBLACK = (0, 0, 0)
colorGRAY = (200, 200, 200)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

WIDTH = 600
HEIGHT = 600
sec = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE")
FPS = 5
clock = pygame.time.Clock()
food_timer = 0
num = random.randint(1,5)

CELL = 30

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))
time_event = pygame.USEREVENT+1
pygame.time.set_timer(time_event, 1000)
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y))
            return True
        return False

    def check_border_collision(self):
        head = self.body[0]
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            return True
        return False

    def speed_increse(self, level):
        return FPS + (level * 2)

class Food:
    def __init__(self):
        self.pos = Point(15, 15)

    def move(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
class GoldFood:
   def __init__(self):
      self.x = int(random.randint(0, WIDTH)/ CELL) * CELL
      self.y = int(random.randint(0, WIDTH)/ CELL) * CELL
      self.rect = pygame.Rect(self.x, self.y, CELL, CELL)
   def update(self):
      pygame.draw.rect(screen, 'yellow', self.rect)
done = False
col = True
snake = Snake()
food = Food()
goldfood = GoldFood()
score = 0
level = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
    if sec > 5:
        rand = int(random.randint(0, 2))
        if rand == 0:
          goldfood = GoldFood()
        else:
          food = Food()
        sec = 0        
    
    draw_grid_chess()

    snake.move()
    if snake.check_border_collision():
        print("Game Over! Hit the wall.")
        pygame.quit()
        sys.exit()
        

    snake.draw()
    food.draw()

    if snake.check_collision(food):
        print("Got food!")
        score += num
        if score % 5 == 0:
            level += 1
            FPS = snake.speed_increse(level)
            print("Level up!")

        food.move()
    
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {score}", True, colorBLACK)
    level_text = font.render(f"Level: {level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))
    

    pygame.display.flip()
    clock.tick(FPS)
