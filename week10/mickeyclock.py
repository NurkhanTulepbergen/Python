import pygame as p
import datetime

WIDTH = 800
HIGH = 700
WIDTH1 = WIDTH - 350
HIGH1 = HIGH - 500
IMAGES = {}
MAX_FPS = 15
def loadImages():
    pieces = ['lefth', 'righth']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("imagess/" + piece + ".png"),(WIDTH1,HIGH1))
        IMAGES['clock'] = p.transform.scale(p.image.load('imagess/clock.png'),(WIDTH,HIGH))

def rot_center(surf, image, topleft, angle):
    rotated_image = p.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit( rotated_image, new_rect)

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HIGH))
    p.display.set_caption('MickeyClock')
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    loadImages()
    done = False
    while not done:
        for event in p.event.get():
            if event.type == p.QUIT:
                done = True
        screen.blit(IMAGES['clock'],(0, 0))
        time = datetime.datetime.now()
        minute = time.minute
        second = time.second
        clock.tick(MAX_FPS)
        rot_center(screen,IMAGES['lefth'],(170,250), ((second % 60)/60) * -360)
        rot_center(screen,IMAGES['righth'],(170,250), ((minute % 60)/60) * -(360 - 40))
        p.display.flip()

if __name__ == "__main__":
    main()
