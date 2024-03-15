import pygame
import random
import math
from parameters import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed, height):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.speed = speed
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH, height))
        self.color_as_function_of_speed()

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

    def color_as_function_of_speed(self):
        # This is just an example of how to change the color of the obstacles
        # based on their speed. You can use this to make the game more visually
        # appealing. I want this to move on the red spectrum - blue spectrum
        # so I'm going to make the red component of the color proportional to
        # the speed of the obstacle, and the blue component inversely proportional
        # to the speed of the obstacle. This will make the obstacles red when they
        # are fast, and blue when they are slow.

        proportion = (self.speed - MINIMUM_OBSTACLE_SPEED)/(MAXIMUM_OBSTACLE_SPEED - MINIMUM_OBSTACLE_SPEED)
        red = proportion*255.0
        green = 0
        blue = (1 - proportion)*255.0
        self.image.fill((red, green, blue))
        print(f"Speed: {self.speed}, Color: {red, green, blue}, Proportion: {proportion}")

def spawn_obstacle(alien_height: int) -> Obstacle:

    # This function spawns a new obstacle with a normal distribution with mean of 
    # the alien height and standard deviation of 10
    height = int(random.gauss(alien_height, 10))
    speed = random.randint(MINIMUM_OBSTACLE_SPEED, MAXIMUM_OBSTACLE_SPEED)
    obstacle = Obstacle(speed, height)
    return obstacle