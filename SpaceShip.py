import pygame


class SpaceShip():
    def __init__(self, x, y, energy, img):
        self.x = x
        self.y = y
        self.energy = energy
        self.img = img
        """
        If it is True , the pixel in the corresponding image belongs to the colored sprite. 
        If False , the pixel in the corresponding image belongs to the background.
        """
        self.mask = pygame.mask.from_surface(self.img)
        self.max_health = energy
        self.lasers = []

    def draw_space_ship(self, screen):
        DEFAULT_IMAGE_SIZE = (64, 64)
        spaceship_img = pygame.transform.scale(
            self.img, DEFAULT_IMAGE_SIZE)
        screen.blit(spaceship_img, (self.x, self.y))

    def get_height(self):
        return self.img.get_height()

    def get_width(self):
        return self.img.get_width()
