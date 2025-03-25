#!/usr/bin/python
# -*- coding: utf-8 -*-import pygame

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode(size=(WIN_WIDTH , WIN_HEIGHT ))

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)


        while True:


            menu = Menu(self.window)
            menu.run()
            pass







