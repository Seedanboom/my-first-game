import pygame
from pygame.sprite import Sprite

class Monster(Sprite):

    def __init__(self,screen):
        super(Monster,self).__init__()
        self.screen=screen
        self.speed=1
        self.direction=1
        self.image = pygame.image.load('images/monster.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect) 
    
    def update(self):
        self.x+=(self.speed*self.direction)
        self.rect.x=self.x

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
    
    
    