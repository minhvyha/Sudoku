import pygame

pygame.init()


RED = (255, 0, 0)
GREEN = (60, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (180, 180, 180)
DGREY = (50, 50, 50)
TURQUOISE = (64, 224, 208)

class Button():
    def __init__(self, WIN, color, text_color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.WIN = WIN
        self.text_color = text_color

    def draw(self,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(self.WIN, outline, (self.x - 2 - self.width // 2, self.y - 2, self.width+4, self.height+4), 0)
            
        pygame.draw.rect(self.WIN, self.color, (self.x - self.width // 2, self.y, self.width, self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (self.text_color))
            self.WIN.blit(text, (self.x + (self.width/2 - text.get_width()/2) - self.width // 2, self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x - self.width // 2 and pos[0] < self.x + self.width - self.width // 2:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


class Pause():
    def __init__(self, WIN, x, y, side) -> None:
        self.x = x
        self.y = y
        self.side = side
        self.WIN = WIN

    def draw(self):
        pygame.draw.rect(self.WIN, BLACK, (self.x - 2 - self.side // 2, self.y - 2, self.side+4, self.side+4), 0)
        pygame.draw.rect(self.WIN, WHITE, (self.x - self.side // 2, self.y, self.side, self.side),0)
        pygame.draw.rect(self.WIN, BLACK, (self.x - self.side // 2 + self.side // 4 - 1, self.y + 8.5 , 8, 35))
        pygame.draw.rect(self.WIN, BLACK, (self.x - self.side // 2 + self.side * 3 // 4 - 7, self.y + 8.5 , 8, 35))
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x - self.side // 2 and pos[0] < self.x + self.side - self.side // 2:
            if pos[1] > self.y and pos[1] < self.y + self.side:
                return True
            
        return False
