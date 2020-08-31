import pygame
import sys
import functions

from monster import Monster
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from game import Game

def run_game():
    pygame.init()
    screen_wid=1200
    screen_hei=800
    screen = pygame.display.set_mode((screen_wid,screen_hei))#屏幕大小
    pygame.display.set_caption("my first game")#标题

    ship=Ship(screen)
   

    bullets=Group()
    monsters=Group()

    functions.creat_monsters(screen,ship,monsters,screen_wid,screen_hei)

    stats=Game()

    while True:
        functions.event_get(screen,ship,bullets)

        if stats.active:    
            ship.update()
            functions.update_monsters(bullets,screen,ship,monsters,screen_wid,screen_hei,stats)
            functions.update_buttles(bullets,screen,ship,monsters,screen_wid,screen_hei,stats)
       
        '''update_screen'''
        functions.update_buttles(bullets,screen,ship,monsters,screen_wid,screen_hei,stats)
        screen.fill((230,230,230))
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        monsters.draw(screen)

        pygame.display.flip()


run_game()
