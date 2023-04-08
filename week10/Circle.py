import pygame as p
import sys
WIDTH = 500
HIGH = 400
def main():
    p.init()
    x = WIDTH // 2
    y = HIGH // 2
    screen = p.display.set_mode((WIDTH, HIGH))
    p.display.set_caption('Circle')
    screen.fill(p.Color("white"))
    color = (255,0,0)
    clock = p.time.Clock()
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
        pressed = p.key.get_pressed()
        if x >= 25 and y >= 25 and x <= 475 and y <= 375:
            if pressed[p.K_DOWN]: y += 10
            if pressed[p.K_UP]: y -= 10
            if pressed[p.K_LEFT]: x -= 10
            if pressed[p.K_RIGHT]: x += 10
        elif x < 25:
            x += 2
        elif y < 25:
            y += 2
        elif y > 375:
            y -= 2
        elif x > 475:
            x -= 2
        screen.fill((255,255,255))
        p.draw.circle(screen, color, (int(x), int(y)), 25)
        p.display.flip()
        clock.tick(40)

if __name__ == "__main__":
    main()