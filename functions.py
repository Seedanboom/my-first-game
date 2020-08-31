import pygame
import sys
from bullet import Bullet
from monster import Monster
from time import sleep

def event_get(screen,ship,bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:#响应按键
                
                if event.key==pygame.K_RIGHT: #右键
                    ship.moving_right=True
                elif event.key == pygame.K_LEFT:#左键
                    ship.moving_left=True
                elif event.key == pygame.K_m:#m键
                    if len(bullets)<ship.allowed:
                        new_bullet=Bullet(screen,ship)
                        bullets.add(new_bullet)
                elif event.key == pygame.K_ESCAPE:
                    pygame.QUIT
            
            elif event.type == pygame.KEYUP:#响应松开
                
                if event.key==pygame.K_RIGHT: 
                    ship.moving_right=False    
                elif event.key == pygame.K_LEFT:
                    ship.moving_left=False

def ship_hit(bullets,screen,ship,monsters,screen_wid,screen_hei,stats):
    if stats.ship_left>0:
        stats.ship_left-=1

        monsters.empty()
        bullets.empty()

        creat_monsters(screen,ship,monsters,screen_wid,screen_hei)
        update_monsters(bullets,screen,ship,monsters,screen_wid,screen_hei,stats)

        sleep(0.5)
    else:
        stats.active=False

    
def update_buttles(bullets,screen,ship,monsters,screen_wid,screen_hei,stats):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,monsters,True,True)
    if len(monsters)<=1:
        bullets.empty()
        creat_monsters(screen,ship,monsters,screen_wid,screen_hei)
        update_monsters(bullets,screen,ship,monsters,screen_wid,screen_hei,stats)

def update_monsters(bullets,screen,ship,monsters,screen_wid,screen_hei,stats):
    for monster in monsters.sprites():
        check_monsters_edges(monster)
        monsters.update()
        if pygame.sprite.spritecollideany(ship,monsters):
            ship_hit(bullets,screen,ship,monsters,screen_wid,screen_hei,stats)
    

def creat_monster(screen,monsters,monster_wid,monster_number,number_row):
    monster=Monster(screen)

    monster.x=monster_wid+2*monster_wid*monster_number
    monster.rect.x=monster.x
    monster.rect.y=monster.rect.height+2*monster.rect.height*number_row
    monsters.add(monster)
    

def creat_monsters(screen,ship,monsters,screen_wid,screen_hei):
    monster=Monster(screen)
    monster_wid=monster.rect.width
    monster_hei=monster.rect.height
    ship_hei=ship.rect.height

    available_space_x=screen_wid- 2*monster_wid
    number_monster_x=int(available_space_x/(2*monster_wid))

    available_space_y=(screen_hei-(2*monster_hei)-ship_hei)
    number_rows=int(available_space_y/(2*monster_hei))

    for number_row in range(number_rows):
        for monster_number in range(number_monster_x):
            creat_monster(screen,monsters,monster_wid,monster_number,number_row)

def check_monsters_edges(monster):
    '''当monster碰到边缘时'''
    if monster.check_edges():
        chang_monsters_direction(monster)#改变位置

def chang_monsters_direction(monster):
    monster.rect.y += 10
    monster.direction *= -1
   
