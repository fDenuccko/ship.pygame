import pygame



class Ship:
    def __init__(self, SW):
        self.screen = SW.screen
        self.screen_recet = SW.screen.get_rect()
        self.image = pygame.image.load("images/1945907.png")
        self.recet = self.image.get_rect()
        self.recet.midbottom = self.screen_recet.midbottom
    def blit_ship(self):
        self.screen.blit(self.image, self.recet)
