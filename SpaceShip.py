import pygame
from Laser import Laser

class SpaceShip():
    COOLDOWN = 30

    def __init__(self, x, y, energy, img):
        self.x = x
        self.y = y
        self.energy = energy
        self.img = img
        self.laser_img = None
        """
        If it is True , the pixel in the corresponding image belongs to the colored sprite. 
        If False , the pixel in the corresponding image belongs to the background.
        """
        self.mask = pygame.mask.from_surface(self.img)
        self.max_health = energy
        self.lasers = []
        self.cool_down_counter = 0

    def draw_space_ship(self, screen):
        DEFAULT_IMAGE_SIZE = (64, 64)
        spaceship_img = pygame.transform.scale(
            self.img, DEFAULT_IMAGE_SIZE)
        screen.blit(spaceship_img, (self.x, self.y))

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    
    def shoot(self, img):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter += 1

    def get_height(self):
        return self.img.get_height()

    def get_width(self):
        return self.img.get_width()
