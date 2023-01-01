import pygame
import time
import random

# Initialising font
pygame.font.init()

# Initialize the pygame
pygame.init()

# Game Constants
WIDTH = 800
HEIGHT = 600
VELOCITY = 4
SIZE_X = 64
SIZE_Y = 64

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
BACKGROUND = pygame.transform.scale(pygame.image.load(
    'assets/imgs/bg/bg_black.png'), (WIDTH, HEIGHT))


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
    level = 1
    lives = 5
    # main_font = pygame.font.SysFont("comicsans", 30)
    # Use this for custom font
    main_font = pygame.font.Font(
        "/usr/share/fonts/JetBrainsMono-2.242/fonts/ttf/JetBrainsMono-Medium.ttf", 24)
    player = SpaceShip(WIDTH//2 - SIZE_X//2, HEIGHT -
                       100, 100, PLAYER_SPACE_SHIP)
    clock = pygame.time.Clock()

    # Function to redraw window
    def redraw_window():
        screen.blit(BACKGROUND, (0, 0))
        # Drawing Text Labels
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        player.draw_space_ship()
        screen.blit(level_label, (10, 10))
        screen.blit(lives_label, (WIDTH - lives_label.get_width() - 10, 10))
        pygame.display.update()

    while running:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - VELOCITY > 0:
            player.x -= VELOCITY
        if keys[pygame.K_RIGHT] and player.x + VELOCITY + SIZE_X < WIDTH:
            player.x += VELOCITY
        if keys[pygame.K_UP] and player.y - VELOCITY > HEIGHT-300:
            player.y -= VELOCITY
        if keys[pygame.K_DOWN] and player.y + VELOCITY + SIZE_Y < HEIGHT:
            player.y += VELOCITY


if __name__ == "__main__":
    main()
