from pygame.locals import  *

GAME_WIDTH_SIZE = 800
GAME_HEIGHT_SIZE = 600

SPRITE_SIZE_W = 32
SPRITE_SIZE_H = 32

DIR = (
    (-1,0), # UP
    (0,1),  # RIGHT
    (1,0),  # DOWN
    (0,-1), # LEFT
)

DIR_KEY = (K_UP, K_RIGHT, K_DOWN, K_LEFT) 

class SpriteType:
    FLOOR = '.'
    WALL = '#'
    BOX = 'o'
    GOAL = 'O'
    PLAYER = 'I'
    
SPRITE_RES = {
    SpriteType.FLOOR: 'res/floor.png',
    SpriteType.WALL: 'res/wall.png',
    SpriteType.BOX: 'res/box.png',
    SpriteType.GOAL: 'res/goal.png',
    SpriteType.PLAYER: 'res/player.png'
}

class ControlType:
    REN = 0
    JI = 1