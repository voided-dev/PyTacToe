import pygame as p
from pygame.locals import *
import sys

WIN_WIDTH = 302
WIN_HEIGHT = 302
BLACK = (0,0,0)

def tiktaktoeWinner():
    
    winner = [
        ((0,0),(0,1),(0,2)),
        ((1,0),(1,1),(1,2)),
        ((2,0),(2,1),(2,2)),
        ((0,0),(1,0),(2,0)),
        ((0,1),(1,1),(1,2)),
        ((0,2),(1,2),(2,2)),
        ((0,2),(1,1),(2,0)),
        ((0,0),(1,1),(2,2))
    ]

def drawGrid():
    square_size = 100
    for x in range(0, WIN_WIDTH, square_size):
        for y in range(0,WIN_HEIGHT, square_size):
            rect = p.Rect(x,y,square_size, square_size)
            p.draw.rect(SCREEN, BLACK, rect, 1)

def main():
    global SCREEN, CLOCK
    p.init()
    #seting game window and game clock
    p.display.set_caption('Tic Tac Toe')
    SCREEN = p.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    CLOCK = p.time.Clock()
    running = True

    while running:
        #event handler
        for ev in p.event.get():
            if ev.type == p.QUIT:
                running = False
                p.quit()
                sys.exit()
                
            if ev.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                

        #Rendered Game Below
        SCREEN.fill('white')
        drawGrid()
        p.display.flip()

        CLOCK.tick(60) #limits game to 60 FPS

if __name__ == "__main__":
    main()

