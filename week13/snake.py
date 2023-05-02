import pygame as p
import sys
import random
import time
import psycopg2
#create limit of our display
WIDTH = 800
HEIGHT = 600
#create size of block
BLOCK_SIZE = 20
global cnt
MAX_LEVEL = 3
global fps, food_timer, now

conn = psycopg2.connect(
    host = "localhost",
    database = "phonebook",
    user = "postgres",
    password = "Nurkhan05"
)
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS snake(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    maxscore VARCHAR(50) NOT NULL,
    maxlevel VARCHAR(50) NOT NULL
)
''')
conn.commit()



print("Enter your username: ")
name = input()
cur.execute("SELECT * FROM snake WHERE name = %s", (name,))
player_data = cur.fetchone()
cur.execute("SELECT COUNT(*) FROM snake WHERE name = %s", (name,))
count = cur.fetchone()[0]
if count != 0:
    print("Name: ", player_data[1])
    print("Max Score: ", player_data[2])
    print("Max Level: ", player_data[3])
else:
    cur.execute("INSERT INTO snake(name,maxscore,maxlevel) VALUES(%s,%s,%s)", (name,0,0))
    print("this is a new player")
conn.commit()

def update_data(name, maxscore=None, maxlevel=None):
    if maxscore:
        cur.execute("UPDATE snake SET maxscore=%s WHERE name=%s", (maxscore, name))
    if maxlevel:
        cur.execute("UPDATE snake SET maxlevel=%s WHERE name=%s", (maxlevel, name))
    conn.commit()

def query_data(name=None):
    cur.execute("SELECT * FROM snake WHERE name = %s", (name,))
    player_data = cur.fetchone()
    if player_data:
        print("Name: ", player_data[1])
        print("Max Score: ", player_data[2])
        print("Max Level: ", player_data[3])


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


#class for group of all food
class Food:
    def __init__(self):
        global fx, fy
        self.cnt = 0
        fx = (random.randint(0, WIDTH // BLOCK_SIZE - 1))
        fy = (random.randint(0, HEIGHT // BLOCK_SIZE - 1))
        self.location = Point(fx, fy)

    def draw(self):#draw food in our map
        point = self.location
        rect = p.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        p.draw.rect(screen, (0,255, 0), rect)

    def randomf(self, wall):#if our food in walls it teleport it to another place
        for i in range(len(wall.body)):
            if self.location.x == wall.allx[i]:
                if self.location.y == wall.ally[i]:
                    self.location.x = (random.randint(0, WIDTH // BLOCK_SIZE - 1))
                    self.location.y = (random.randint(0, HEIGHT // BLOCK_SIZE - 1))


#create the same class for bonus food
class FoodBonus:
    def __init__(self):
        global fx, fy
        self.cnt = 0
        fx = (random.randint(0, WIDTH // BLOCK_SIZE - 1))
        fy = (random.randint(0, HEIGHT // BLOCK_SIZE - 1))
        self.location = Point(fx, fy)

    def draw(self):#draw food in our map
        point = self.location
        rect = p.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        p.draw.rect(screen, (255,255, 255), rect)

    def randomf(self, wall):#if our food in walls it teleport it to another place
        for i in range(len(wall.body)):
            if self.location.x == wall.allx[i]:
                if self.location.y == wall.ally[i]:
                    self.location.x = (random.randint(0, WIDTH // BLOCK_SIZE - 1))
                    self.location.y = (random.randint(0, HEIGHT // BLOCK_SIZE - 1))
    def disappear(self): #function for spawn food in random another place
        self.location.x = (random.randint(0, WIDTH // BLOCK_SIZE - 1))
        self.location.y = (random.randint(0, HEIGHT // BLOCK_SIZE - 1))


#create class walls drawing in the map
class Wall:
    def __init__(self, level,):
        self.body = []
        self.allx = []
        self.ally = []
        f = open("levels/level{}.txt".format(level), "r")

        for y in range(0, HEIGHT // BLOCK_SIZE +1):
            for x in range(0, WIDTH // BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))
                    self.allx.append(x)
                    self.ally.append(y)
    def draw(self):
        for point in self.body:
            rect = p.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            p.draw.rect(screen, p.Color("blue"), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10,11)]
        self.dx = 0
        self.dy = 0
        self.level = 0
    
    def move(self):#for moving
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy
        
        if self.body[0].x * BLOCK_SIZE > WIDTH:
            query_data(name=name)
            time.sleep(2)
            sys.exit()
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            query_data(name=name)
            time.sleep(2)
            sys.exit()
        if self.body[0].x < 0:
            query_data(name=name)
            time.sleep(2)
            sys.exit()
        if self.body[0].y < 0:
            query_data(name=name)
            time.sleep(2)
            sys.exit()

    def draw(self):#draw our snake which is contain rectangles
        point = self.body[0]
        rect = p.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        p.draw.rect(screen, p.Color("green"), rect)

        for point in self.body[1:]:
            rect = p.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            p.draw.rect(screen, p.Color("red"), rect)
    
    def collision(self):#if snake touch his body
        if self.body[0] in self.body[1:]:
            p.quit()
            sys.exit()
        
    def check_collision(self,food, foodbonus):#for random appearing food after has eaten by snake
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                food.cnt += 1
                food.location.x = (random.randint(0, WIDTH // BLOCK_SIZE - 1))
                food.location.y = (random.randint(0, HEIGHT // BLOCK_SIZE - 1))
        if self.body[0].x == foodbonus.location.x: #add some code for new bonus food
            if self.body[0].y == foodbonus.location.y:
                food.cnt += 2
                self.body.append(Point(foodbonus.location.x, foodbonus.location.y))
                self.body.append(Point(foodbonus.location.x, foodbonus.location.y))
                foodbonus.location.x = (random.randint(0, WIDTH // BLOCK_SIZE - 1))
                foodbonus.location.y = (random.randint(0, HEIGHT // BLOCK_SIZE - 1))
    def check_walls(self,wall):#if snake smash walls game end
        for i in range(len(wall.body)):
            if self.body[0].x == wall.allx[i]:
                if self.body[0].y == wall.ally[i]:
                    query_data(name=name)
                    p.quit()
                    sys.exit()



def main():
    global screen, clock 
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("black"))
    font= p.font.SysFont("Verdana", 30)
    snake = Snake()
    p.display.set_caption("Snake")
    food = Food()
    wall = Wall(snake.level)
    foodbonus = FoodBonus()
    cnt = 0
    fps = 8
    food_timer = p.time.get_ticks() + 5000#time after starting our code + 5 second
    while True:
        now = p.time.get_ticks()
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_RIGHT:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == p.K_LEFT:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == p.K_UP:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == p.K_DOWN:
                    snake.dx = 0
                    snake.dy = 1
        FOODS = font.render(str(food.cnt), True, p.Color("yellow"))
        snake.move()
        if p.time.get_ticks() >= food_timer: #if time bigger than we give in the start food is spawn in another place
            foodbonus.disappear()
            food_timer = p.time.get_ticks() + 5000
        food.randomf(wall)
        foodbonus.randomf(wall)#check that food not in walls
        snake.check_collision(food, foodbonus)
        snake.collision()
        snake.check_walls(wall)
        #for changing levels
        if len(snake.body) > 10:
            newlevel = (snake.level + 1) % MAX_LEVEL
            fps += 3
            snake = Snake()
            snake.level = newlevel
            wall = Wall(snake.level)
        screen.fill(p.Color("black"))
        update_data(name, maxscore=food.cnt, maxlevel=snake.level+1)
        wall.draw()
        snake.draw()
        food.draw()
        foodbonus.draw()
        screen.blit(FOODS, (10, 10))
        #drawGrid()
        p.display.update()
        clock.tick(fps)
    query_data(name=name)
    

def drawGrid():#grid for myself
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = p.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            p.draw.rect(screen, p.Color("white"), rect, 1)

if __name__ == "__main__":
    main()
    
