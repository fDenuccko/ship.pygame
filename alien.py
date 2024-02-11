import pygame
import.random
 
class Alien():
    def __init__(self, SW):
        self.screen = SW.screen     
        self.image = pygame.image.load("images/тушкан.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect =  SW.screen.get_rect()
        self.alian_speed = 0.5

        self.y = float(self.recet.y)
    def update_alian(self):
        if self.rect.bottom < self.screen_rect.bottom:
            self.y += self.alian_speed
        if self.rect.bottom == self.screen_rect.bottom:
        self.rect.y = self.y
    def blit_alian(self):
        self.screen.blit(self.image, (random.randint(0, self.screen_rect.bottom.right)0) self.recet)
