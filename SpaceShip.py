import pygame


class SpaceShip():
    def __init__(self, x, y, energy, image):
        self.x = x
        self.y = y
        self.energy = energy
        self.image = image
        """
        If it is True , the pixel in the corresponding image belongs to the colored sprite. 
        If False , the pixel in the corresponding image belongs to the background.
        """
        self.mask = pygame.mask.from_surface(self.image)
        self.max_health = energy

    def draw_space_ship(self, screen):
        DEFAULT_IMAGE_SIZE = (64, 64)
        spaceship_img = pygame.transform.scale(
            self.image, DEFAULT_IMAGE_SIZE)
        screen.blit(spaceship_img, (self.x, self.y))
