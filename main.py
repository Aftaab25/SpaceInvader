import pygame

# Initialize the pygame
pygame.init()

# Game Constants
WIDTH = 800
HEIGHT = 600

# Game Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('assets/imgs/icon/logo.png')
pygame.display.set_icon(icon)

# Load Images
PLAYER_SPACE_SHIP = pygame.image.load('assets/imgs/spaceships/spaceship2.png')
ENEMY_SPACE_SHIP = pygame.image.load('assets/imgs/spaceships/enemy.png')
LASER = pygame.image.load('assets/imgs/laser/laser_32.png')
BACKGROUND = pygame.image.load('assets/imgs/bg/bg_black.png')


class SpaceShip():
    def __init__(self, x, y, energy, image):
        self.x = x
        self.y = y
        self.energy = energy
        self.image = image

    def draw_space_ship(self):
        DEFAULT_IMAGE_SIZE = (64, 64)
        spaceship_img = pygame.transform.scale(
            self.image, DEFAULT_IMAGE_SIZE)
        screen.blit(spaceship_img, (self.x, self.y))


# Game Loop
def main():
    running = True
    FPS = 60
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
