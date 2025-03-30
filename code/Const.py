import pygame

C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 128)
C_CYAN = (0, 255, 255)

# H
ENTITY_HEALTH = {
    'level1Bg0': 999,
    'level1Bg1': 999,
    'level1Bg2': 999,
    'level1Bg3': 999,
    'level1Bg4': 999,
    'level1Bg5': 999,
    'level1Bg6': 999,
    # Adicione estas linhas abaixo:
    'level2Bg0': 999,
    'level2Bg1': 999,
    'level2Bg2': 999,
    'level2Bg3': 999,
    'level2Bg4': 999,
    'Player1': 6,
    'Player1shot': 1,
    'Player2': 6,
    'Player2shot': 1,
    'Enemy1': 50,
    'Enemy1shot': 1,
    'Enemy2': 60,
    'Enemy2shot': 1,
}


ENTITY_DAMAGE = {
    'level1Bg0': 0,
    'level1Bg1': 0,
    'level1Bg2': 0,
    'level1Bg3': 0,
    'level1Bg4': 0,
    'level1Bg5': 0,
    'level1Bg6': 0,
    'level2Bg0': 0,
    'level2Bg1': 0,
    'level2Bg2': 0,
    'level2Bg3': 0,
    'level2Bg4': 0,
    'Player1': 1,
    'Player1shot': 35,
    'Player2': 1,
    'Player2shot': 20,
    'Enemy1': 1,
    'Enemy1shot': 20,
    'Enemy2': 1,
    'Enemy2shot': 15,
}
# score
ENTITY_SCORE = {
    'level1Bg0': 0,
    'level1Bg1': 0,
    'level1Bg2': 0,
    'level1Bg3': 0,
    'level1Bg4': 0,
    'level1Bg5': 0,
    'level1Bg6': 0,
    'level2Bg0': 0,
    'level2Bg1': 0,
    'level2Bg2': 0,
    'level2Bg3': 0,
    'level2Bg4': 0,
    'Player1': 0,
    'Player1shot': 0,
    'Player2': 0,
    'Player2shot': 0,
    'Enemy1': 100,
    'Enemy1shot': 0,
    'Enemy2': 125,
    'Enemy2shot': 0,
}

# delay
ENTITY_SHOT_DELAY = {
    'Player1': 22,
    'Player2': 16,
    'Enemy1': 30,
    'Enemy2': 40,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}
# s
SPAWN_TIME = 4000


# T
TIMEOUT_STEP = 100 #100ms

TIMEOUT_LEVEL = 20000 #20s
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'level1Bg0': 0,
    'level1Bg1': 1,
    'level1Bg2': 2,
    'level1Bg3': 3,
    'level1Bg4': 4,
    'level1Bg5': 5,
    'level1Bg6': 6,
    'level2Bg0': 0,
    'level2Bg1': 1,
    'level2Bg2': 2,
    'level2Bg3': 3,
    'level2Bg4': 4,
    'Player1': 4,
    'Player1shot': 5,
    'Player2': 4,
    'Player2shot': 2,
    'Enemy1': 1,
    'Enemy1shot': 3,
    'Enemy2': 1,
    'Enemy2shot': 3,
}
# s
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
