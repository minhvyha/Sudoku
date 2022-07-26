import pygame
from board import Board


# initialize pygame library
pygame.init() 

# Window set up
WIDTH = 700
HEIGHT = 700
BOARD_WIDTH = 500
BOARD_HEIGHT = 500



WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')

# GLOBAL VARIABLE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60

# Set up the board
BOARD = Board(WIN, BOARD_WIDTH, BOARD_HEIGHT, WIDTH - BOARD_WIDTH)




def main():
    isRun = True
    # Loop forever to draw up the window every second
    while isRun:
        
        # Get any event from user such as mouse click, key pressed

        # pygame.event.get() = [click (50, 100)]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRun = False
                break
            keys = pygame.key.get_pressed()
            if BOARD.curr != None and keys:
                assign(keys)
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if x < BOARD_WIDTH - 5 and y > WIDTH - BOARD_WIDTH:
                    BOARD.click(x, y)
        draw()
    pygame.quit()



def assign(keys):
    if keys[pygame.K_1]:
        BOARD.assign(1)
    elif keys[pygame.K_2]:
        BOARD.assign(2)
    elif keys[pygame.K_3]:
        BOARD.assign(3)
    elif keys[pygame.K_4]:
        BOARD.assign(4)
    elif keys[pygame.K_5]:
        BOARD.assign(5)
    elif keys[pygame.K_6]:
        BOARD.assign(6)
    elif keys[pygame.K_7]:
        BOARD.assign(7)
    elif keys[pygame.K_8]:
        BOARD.assign(8)
    elif keys[pygame.K_9]:
        BOARD.assign(9)
    


#Function to draw the window
def draw():

    # Make changes to the window
    WIN.fill((WHITE))
    BOARD.draw()

    # Update and display all the changes
    pygame.display.update()



# Execute all the code
if __name__ == '__main__':
    main()
    