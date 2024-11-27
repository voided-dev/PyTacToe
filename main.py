import pygame
from pygame.locals import *
import sys

### Global Scope Variables ###
pygame.init()    # initalize the pygame library
WIN_WIDTH = 300
WIN_HEIGHT = 300
GRID_SIZE = 100
BLACK = (0,0,0)
# provide the initial state of the grid, since no moves have been played there is no value associated to any of the grid squares, 
# thus a value of None in each position of the grid
grid_state = [
                [None, None, None],
                [None, None, None],
                [None, None, None]
            ]

def tiktaktoeWinner():
    
    winning_combos = [
        ((0,0),(0,1),(0,2)), # across row 1
        ((1,0),(1,1),(1,2)), # across row 2
        ((2,0),(2,1),(2,2)), # across row 3
        ((0,0),(1,0),(2,0)), # down col 1
        ((0,1),(1,1),(1,2)), # down col 2
        ((0,2),(1,2),(2,2)), # down col 3
        ((0,2),(1,1),(2,0)), # diagonal from top right to bottom left
        ((0,0),(1,1),(2,2))  # diagonal from top left to bottom right   
    ]

    # check to see if any of the winning states are all "X" or all "0"
    for row in winning_combos:
        pass


def displayGrid():
    for x in range(0, WIN_WIDTH, GRID_SIZE): #  start the loop at 0, end at max width of the screen, moving/stepping the length of the grid size
        for y in range(0, WIN_WIDTH, GRID_SIZE):    # see comment above
            grid_rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE) # display the grid square at position XY, width and height equal to grid size, store the generated rect to var grid_rect
            pygame.draw.rect(SCREEN, BLACK, grid_rect, 1) # draws/displays the current grid square to the main window

def displaySymbol():
    #initialize the font
    symbol_font = pygame.font.SysFont('Times New Roman', 75)
    
    #render out the 'X' and 'O'
    valX = symbol_font.render('X', True, BLACK)
    valO = symbol_font.render('O', True, BLACK)

    # create a rect around the render text
    valX_rect = valX.get_rect()
    valO_rect = valO.get_rect()

    for i in range(int(WIN_WIDTH / GRID_SIZE)):
        for j in range(int(WIN_HEIGHT / GRID_SIZE)):

            pos_x = i * GRID_SIZE # get the posistion to blit the text index * 100 (grid_size)
            pos_y = j * GRID_SIZE # get the posistion to blit the text index * 100 (grid_size)

            if grid_state[i][j] == 'X':
                # center the text rect
                valX_rect.center = (pos_x + GRID_SIZE // 2, pos_y + GRID_SIZE // 2)
                SCREEN.blit(valX, valX_rect)
            if grid_state[i][j] == 'O':
                valO_rect.center = (pos_x + GRID_SIZE // 2, pos_y + GRID_SIZE // 2)
                SCREEN.blit(valO, valO_rect)
def main():
    ### poll display settings ###
    global SCREEN, CLOCK  # declared globally for use in creating functions
    pygame.display.set_caption('TIC TAC TOE')
    SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    CLOCK = pygame.time.Clock()
    running = True  # created variable to switch state to determine if the game is running or not
    player_state = True # created variable to decipher if it is player1 'X' or player2 'O' playing
    

    while running:
        ### Event Handler ###
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
                pygame.quit() # suspend the pygame module
                sys.exit()  # exits python interpreteur
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # find which grid square we are currently in
                pos = pygame.mouse.get_pos() # returns the coords of where we click
                
                grid_x = pos[0] // GRID_SIZE # take the x pos of the mouse click and implement floor division to return the x grid index of the local square
                grid_y = pos[1] // GRID_SIZE # take the y pos of the mouse click and implement floor division to return the x grid index of the local square

                if grid_state[grid_x][grid_y] is None:
                    if player_state == True:    # checks if box has not been played and player_state is true(player1), returns 'X'
                        grid_state[grid_x][grid_y] = 'X'
                    elif player_state == False:   # checks if box has been played and player_state is false(player2), returns 'O'
                        grid_state[grid_x][grid_y] = 'O'

                    print((grid_x, grid_y), grid_state[grid_x][grid_y], player_state)
                    player_state = not player_state
                else:
                    print(tiktaktoeWinner())
 #once one of the above conditions is met change the state of player_state so that it becomes the other players turn

        ### Rendered Game Code ###
        #   set a colour so the window displays
        SCREEN.fill('white')
        displayGrid()
        displaySymbol()
        pygame.display.update()
        
        CLOCK.tick(60) #limit 60 FPS, deltatime (dt) not needed for this program since we need no frame-independant physics


if __name__ == "__main__":
    main()

