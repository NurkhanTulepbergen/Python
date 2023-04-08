import pygame as p

WIDTH = 800
HIGH = 700
IMAGES = {}
global a
global cnt
def loadImages():
    pieces = ["SmackThat", "Superman", "DieForYou", "Tom'sDiner", "WorkOut"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Music/" + piece + ".jpg"), (WIDTH, HIGH))

def main():
    a = 0
    cnt = 0
    loadImages()
    MUSICS = [("Music/SmackThat.mp3",IMAGES["SmackThat"]), ("Music/Superman.mp3",IMAGES["Superman"]), ("Music/DieForYou.mp3",IMAGES["DieForYou"]), ("Music/Tom'sDiner.mp3",IMAGES["Tom'sDiner"]), ("Music/WorkOut.mp3",IMAGES["WorkOut"] )]
    lenM= len(MUSICS)
    p.init()
    p.mixer.init()
    screen = p.display.set_mode((WIDTH, HIGH))
    p.display.set_caption('MusicPlayer')
    screen.fill(p.Color("black"))
  
    run = False
    while not run:
        for event in p.event.get():
            if event.type == p.QUIT:
                run = True

            if event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    p.mixer.music.load(MUSICS[a][0]) 
                    p.mixer.music.play(0)

                elif event.key == p.K_RIGHT:
                    a += 1
                    p.mixer.music.load(MUSICS[a][0]) 
                    p.mixer.music.play(0)
                    if a == (lenM - 1):
                        a = -1
                    
                elif event.key == p.K_LEFT:
                    if a < 0:
                        a = lenM - 1 
                    a -= 1
                    p.mixer.music.load(MUSICS[a][0]) 
                    p.mixer.music.play(0)

                elif event.key == p.K_SPACE:
                    cnt += 1
                    if cnt % 2 != 0:
                        p.mixer.music.pause()
                    else:
                        p.mixer.music.unpause()
            screen.blit(MUSICS[a][1],(0, 0))
        p.display.flip()
                    
if __name__ == "__main__":
    main()