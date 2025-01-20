'''
Constants module defines game constants like colors, shapes, and board dimensions.
'''
# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
# Grid dimensions
ROWS = 20
COLS = 10
BLOCK_SIZE = 30
# Frames per second
FPS = 60
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]]
]