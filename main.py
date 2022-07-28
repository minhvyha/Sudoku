import pygame
from board import Board
import time

# initialize pygame library
pygame.init() 

# Window set up
WIDTH = 700
HEIGHT = 700
BOARD_WIDTH = 500
BOARD_HEIGHT = 500

FONT = pygame.font.SysFont('comicsans', 30)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')

# GLOBAL VARIABLE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60

# Set up the board
BOARD = Board(WIN, BOARD_WIDTH, BOARD_HEIGHT, WIDTH - BOARD_WIDTH)

ERROR = 0

def main():
    isRun = True
    clock = pygame.time.Clock()
    # Loop forever to draw up the window every second
    while isRun:
        
        # Get any event from user such as mouse click, key pressed
        clock.tick(FPS)
        # pygame.event.get() = [click (50, 100)]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRun = False
                break
            
            keys = pygame.key.get_pressed()

            if (BOARD.curr != None) and (keys):
                assign(keys)

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if x < BOARD_WIDTH - 5 and y > WIDTH - BOARD_WIDTH:
                    BOARD.select(x, y)
        draw()
        if pygame.mouse.get_pressed()[0] or keys:
            time.sleep(0.2)
    pygame.quit()


# keys = [1]
def assign(keys):
    global ERROR
    if keys[pygame.K_1]:
        ERROR += BOARD.assign(1)
    elif keys[pygame.K_2]:
        ERROR += BOARD.assign(2) 
    elif keys[pygame.K_3]:
        ERROR += BOARD.assign(3)
    elif keys[pygame.K_4]:
        ERROR += BOARD.assign(4)
    elif keys[pygame.K_5]:
        ERROR += BOARD.assign(5)
    elif keys[pygame.K_6]:
        ERROR += BOARD.assign(6)
    elif keys[pygame.K_7]:
        ERROR += BOARD.assign(7)
    elif keys[pygame.K_8]:
        ERROR += BOARD.assign(8)
    elif keys[pygame.K_9]:
        ERROR += BOARD.assign(9)


#Function to draw the window
def draw():
      
    
    # Make changes to the window
    WIN.fill((WHITE))


    if BOARD.curr:
        row, col = BOARD.curr
        ver = pygame.Surface((500,500 // 9))
        hor = pygame.Surface((500 // 9,500))

        hor.set_alpha(75)
        hor.fill((197,226,255))   
        
        ver.set_alpha(75)
        ver.fill((197,226,255)) 

        WIN.blit(hor, (BOARD_WIDTH // 9 * col, WIDTH - BOARD_WIDTH))
        WIN.blit(ver, (0, BOARD_WIDTH // 9 * row + WIDTH - BOARD_WIDTH))
    BOARD.draw()
    error = FONT.render(f'Error: {ERROR}', 1, BLACK)
    WIN.blit(error, (10, 10))


    


    # Update and display all the changes
    pygame.display.update()



# Execute all the code
if __name__ == '__main__':
    main()
    