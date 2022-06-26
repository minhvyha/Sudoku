import pygame


class Board:
    def __init__(self, WIN) -> None:
        # 9 x 9 sudoku board
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        # Get the reference for the window
        self.WIN = WIN

    # Draw the board into the window
    def draw(self) -> None:
        pass