import pygame, psycopg2
import random
from config import config
import sys

def delete_by_name(name):
    sql = f"DELETE FROM snake WHERE name = '{name}'"
    insert(sql)


'''def create_table():
    SQL = (
        """CREATE TABLE IF NOT EXISTS snake (
        name VARCHAR(256) NOT NULL,
        score INTEGER NOT NULL,
        level INTEGER NOT NULL
        )
          """
    )
    
    try:
        config = psycopg2.connect(**config())
        query = config.cursor()
        query.execute(SQL)
        query.close()
        config.commit()

    except Exception as Error:
        print(str(Error))

 
create_table()'''

def insert(sql):
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def check(name):
    sql = f"SELECT name FROM snake WHERE name = '{name}'"
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    if result == None:
        return False
    else:
        return True

print("Enter your name:")
name = input()
if check(name) == False:
    sql = f"INSERT INTO snake (name, score) VALUES ('{name}', 0)"
    insert(sql)


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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE")
FPS = 5
clock = pygame.time.Clock()

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
        return FPS + level

class Food:
    def __init__(self):
        self.pos = Point(15, 15)

    def move(self):
        self.pos = Point(random.randint(0, WIDTH // CELL - 1), random.randint(0, HEIGHT // CELL - 1))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

done = False
snake = Snake()
food = Food()
score = 0
level = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
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

    draw_grid_chess()

    snake.move()
    if snake.check_border_collision():
        saved_score = score
        sql = f"UPDATE snake SET score = {saved_score} WHERE name = '{name}'"
        insert(sql)
        pygame.quit()
        sys.exit()

        

    snake.draw()
    food.draw()

    if snake.check_collision(food):
        score += 1
        if score % 5 == 0:
            level += 1
            saved_level = level
            sql = f"UPDATE snake SET level = {saved_level} WHERE name = '{name}'"
            insert(sql)
            FPS = snake.speed_increse(level)

        food.move()
    
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {score}", True, colorBLACK)
    level_text = font.render(f"Level: {level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))
    

    pygame.display.flip()
    clock.tick(FPS)
    
