import pygame
import random
import math
from parameters import *

# per collision losses one life and the game is over when the lives are over
# only has MAX_LIVES lives

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT - 50))
        self.jump_speed = -20  # Negative because PyGame's y-axis is inverted
        self.velocity = 0
        self.lives = MAX_LIVES

    def jump(self):
        self.velocity = self.jump_speed

    def update(self):
        self.velocity += GRAVITY * 0.1  # Adjust gravity's effect based on your game's needs
        self.rect.y += self.velocity
        # Prevent the alien from falling below the ground
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0

        # Allow the alien to cicle from the top to the bottom of the screen
        if self.rect.top < 0:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity = 0

    def update_lives(self, collided_obstacles):
        self.lives = MAX_LIVES - len(collided_obstacles)
        if self.lives == 0:
            return False
        return True
        

def draw_lives(surface, x, y, lives, radius=10, spacing=5, color=(255, 0, 0)):
    """
    Draws the life bar with red circles representing lives.
    :param surface: PyGame surface to draw on
    :param x: X coordinate of the first circle's center
    :param y: Y coordinate of the circles' center
    :param lives: Number of lives to draw
    :param radius: Radius of each circle
    :param spacing: Spacing between circles
    :param color: Color of the circles
    """
    lives_str = 'Lives: ' + str(lives)
    font = pygame.font.Font(None, 24)
    lives_surf = font.render(lives_str, True, color)  # Render the text to a new surface
    lives_rect = lives_surf.get_rect(center=(x - 50, y))

    # Draw the lives text
    surface.blit(lives_surf, lives_rect)

    # We draw the lives
    for i in range(lives):
        pygame.draw.circle(surface, color, (x + i * (radius * 2 + spacing), y), radius)