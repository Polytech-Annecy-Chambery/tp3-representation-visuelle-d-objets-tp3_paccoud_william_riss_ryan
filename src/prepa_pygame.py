# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 08:15:49 2021

@author: paccoudw
"""

import pygame


pygame.init()
ecran = pygame.display.set_mode((300, 200))

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()