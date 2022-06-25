import pygame
import block

pygame.init()

# Window set up
WIDTH = 700
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')

#GLOBAL VARIABLE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60


def main():
    
    # Loop forever to draw up the window every second
    while True:
        # Get any event from user such as mouse click, key pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
        draw()


#Function to draw the window
def draw():
    # Make changes to the window
    WIN.fill(WHITE)

    # Update and display all the changes

    pygame.display.update()


# Execute all the code
if __name__ == '__main__':
    main()