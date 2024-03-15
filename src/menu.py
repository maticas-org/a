import math
import random
import pygame
from parameters import *


def ask_for_number(screen,
                   clock: pygame.time.Clock,
                   question: str,
                   default):
    """
        This function asks for a random number and returns it.
        This can be used for the random seed choice, or for the
        minimum and maximum obstacle speeds.
    """

    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(SCREEN_WIDTH // 3 - 100, SCREEN_HEIGHT // 2 - 20, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active   = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            
            # If the user closes the window, then we're done
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                exit()

            # If the user clicks on the input box, then we're active
            # and we change the color of the input box
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            # If the user types, then we add the character to the text
            # or we remove the last character if the user presses backspace
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # We update the screen
        screen.fill((30, 30, 30))

        # Render the question and the text
        txt_surface = font.render(question, True, (255, 255, 255))
        width = max(150, txt_surface.get_width() + 10)
        input_box.w = width
        
        # We render the text and the input box
        screen.blit(txt_surface, (SCREEN_WIDTH // 2 - width // 2, SCREEN_HEIGHT // 2 - 50))
        txt_surface = font.render(text, True, (255, 255, 255))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # We draw the input box
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(60)

    if text == '':
        return default
    return int(text)

def show_menu(screen, clock) -> int:
    """
    """

    menu_running = True
    title_font = pygame.font.Font(None, 72)
    option_font = pygame.font.Font(None, 36)

    title_text = title_font.render('Alien Jump Game', True, (255, 255, 255))
    play_text = option_font.render('Play', True, (255, 255, 255))
    quit_text = option_font.render('Quit', True, (255, 255, 255))

    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    play_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    while menu_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()
                exit()  # Terminate the program
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_rect.collidepoint(event.pos):
                    menu_running = False  # Will start the game
                    new_random_seed = ask_for_number(screen, clock, "Escribe un número aleatorio (o dale al enter para omitir):", RANDOM_SEED)
                    return new_random_seed

                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        screen.fill((0, 0, 0))  # Fill the screen with a background color
        screen.blit(title_text, title_rect)
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()
        clock.tick(60)
