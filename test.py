# Simple pygame program
# Import and initialize the pygame library

import pygame
import pygame_menu
import StartGame

pygame.init()

# Set up the drawing window

screen = pygame.display.set_mode([500, 500])


# Run until the user asks to quit

running = True


def set_difficulty(value, difficulty):
    # Do the job here !
    pass





while running:

    # Did the user click the window close button?

    # for event in pygame.event.get():
    #
    #     if event.type == pygame.QUIT:
    #         running = False

    menu = pygame_menu.Menu('Welcome', 400, 300,
                            theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name :', default='John Doe')
    menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
    menu.add.button('Play', StartGame.start_the_game())
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)
    pygame.display.flip()
