import pygame

# Initialize the pygame
pygame.init()

# Game Screen
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/spaceships/logo.png')
pygame.display.set_icon(icon)


class SpaceShip():
    def __init__(self, x, y, energy, imagepath):
        self.x = x
        self.y = y
        self.energy = energy
        self.imagepath = imagepath

    def draw_space_ship(self):
        DEFAULT_IMAGE_SIZE = (64, 64)
        spaceship_img = pygame.image.load(self.imagepath)
        spaceship_img = pygame.transform.scale(
            spaceship_img, DEFAULT_IMAGE_SIZE)
        screen.blit(spaceship_img, (self.x, self.y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player = SpaceShip(370, 480, 100, 'assets/spaceships/spaceship2.png')
    player.draw_space_ship()
    pygame.display.update()
