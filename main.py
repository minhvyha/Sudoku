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
        draw()
    pygame.quit()


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