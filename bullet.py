import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
   
    def __init__(self, screen,ship):
        self.speed=1#速度
        self.color=255,255,255#子弹颜色
        
        super(Bullet, self).__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0, 10, 10)#x，y，宽，高
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        self.y=float(self.rect.y)
    
    def update(self):
        self.y -= self.speed
        self.rect.y=self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)