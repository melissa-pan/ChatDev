'''
GUI class handles the graphical user interface using Pygame.
'''
import pygame
import sys
class GUI:
    def __init__(self, board_size):
        pygame.init()
        self.board_size = board_size
        self.cell_size = 40
        self.width = self.height = self.board_size * self.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Gomoku')
    def draw_board(self, board):
        self.screen.fill((255, 255, 255))
        for x in range(self.board_size):
            for y in range(self.board_size):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)
    def draw_pieces(self, board):
        for y in range(self.board_size):
            for x in range(self.board_size):
                if board.grid[y][x] != '':
                    center = (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2)
                    if board.grid[y][x] == 'X':
                        pygame.draw.line(self.screen, (0, 0, 0), (center[0] - 10, center[1] - 10), (center[0] + 10, center[1] + 10), 2)
                        pygame.draw.line(self.screen, (0, 0, 0), (center[0] - 10, center[1] + 10), (center[0] + 10, center[1] - 10), 2)
                    elif board.grid[y][x] == 'O':
                        pygame.draw.circle(self.screen, (0, 0, 0), center, 10, 2)
    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= self.cell_size
                y //= self.cell_size
                game.make_move(x, y)
        pygame.display.flip()