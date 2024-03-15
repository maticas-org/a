import pygame
import random
import math
import menu

from parameters import *
from alien import Alien, draw_lives
from obstacles import Obstacle, spawn_obstacle

# Initialize PyGame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alien Jump")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
alien = Alien()
obstacles = pygame.sprite.Group()
collided_obstacles = set()

# Show the menu
RANDOM_SEED = menu.show_menu(screen, clock)
random.seed(RANDOM_SEED)

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                alien.jump()

    # Spawn a new obstacle randomly
    if random.randint(0, 60) == 0:  # Adjust timing for gameplay

        # Get the alien position
        alien_position = alien.rect.y
        obstacle = spawn_obstacle(alien_position)
        obstacles.add(obstacle)

    # Update
    alien.update()
    obstacles.update()

    # Collision detection
    if pygame.sprite.spritecollide(alien, obstacles, False):
        
        # Add the collided obstacles to a new group
        for obstacle in pygame.sprite.spritecollide(alien, obstacles, False):
            collided_obstacles.add(obstacle)

        # Update the lives of the alien
        if not alien.update_lives(collided_obstacles):
            # Game over and reset the game
            RANDOM_SEED = menu.show_menu(screen, clock)
            alien.lives = MAX_LIVES
            collided_obstacles = set()

    # Draw everything
    screen.blit(alien.image, alien.rect)
    for obstacle in obstacles:
        screen.blit(obstacle.image, obstacle.rect)

    draw_lives(screen, 100, 20, alien.lives)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()