# ------------- INITIALIZATIONS-------------------

from modules.computer import *
from modules.board import *
import pygame
import sys

pygame.init()  # essential for pygame
pygame.font.init()  # for text

# define display surface
screen = pygame.display.set_mode((800, 60 * 8))
pygame.display.set_caption('Python Chess Game')


# load images
bg = pygame.image.load("assets/chessboard.png").convert()
sidebg = pygame.image.load("assets/woodsidemenu.jpg").convert()
player = 1  # 'AI' for the computer player
myfont = pygame.font.Font("assets/Roboto-Black.ttf", 30)
clippy = pygame.image.load("assets/Clippy.png").convert_alpha()
clippy = pygame.transform.scale(clippy, (320, 240))
playeravatar = None

# board matrix, create instance of board class from modules.board
board = Board()

# allows us to keep track of sprites

all_sprites_list = pygame.sprite.Group()
sprites = [piece for row in board.array for piece in row if piece]
all_sprites_list.add(sprites)

# draw the sprites onto the screen
all_sprites_list.draw(screen)

# necessary for capping the game at 60FPS
clock = pygame.time.Clock()
