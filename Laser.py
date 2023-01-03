import pygame

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return self.y <= height and self.y >= 0
    
    # TODO: refactor the collision method, so that it's not just restricted to
    # Lasers, but can also be used to detect collision between any two objects. 
    def collision(self, obj):
        offset_x = obj.x - self.x
        offset_y = obj.y - self.y
        return self.mask.overlap(obj.mask, (offset_x, offset_y))