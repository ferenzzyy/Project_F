import pygame  # imports pygame
from menu import *  # imports everything from the menu.py file
#from play_area import *
import sys
from pygame.locals import *  # import pygame modules

clock = pygame.time.Clock()


class Game():
    def __init__(self):
        pygame.init()  # initializes pygame
        # This sets up the states for the menu and game.
        self.running, self.playing = True, False
        # This is used to set up the contorls
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        # This is used to set up the window's height and width
        self.window_size = (self.DISPLAY_W, self.DISPLAY_H)
        # This is used to create the windows
        self.window = pygame.display.set_mode(self.window_size, 0, 32)
        # This is used to create the display with pygame
        self.display = pygame.Surface(self.window_size)
        self.font_name = '8-BIT WONDER.TTF'  # THe font used in the game
        self.BLACK, self.WHITE, self.GREEN = (
            0, 0, 0), (255, 255, 255), (86, 125, 70)  # The colours used in the menu
        # Class called from menu.py (Sets up the main menu properties)
        self.main_menu = MainMenu(self)
        # Class called from menu.py (Sets up the options menu properties)
        self.options = OptionsMenu(self)
        # Class called from menu.py (Sets up the Credits properties
        self.credits = CreditsMenu(self)
        # THis is used so that when the game is opened the main menu is always the first menu to appear on screen
        self.curr_menu = self.main_menu

    icon_image = pygame.image.load('F.png')
    pygame.display.set_caption('Project F')
    pygame.display.set_icon(icon_image)

    #main Game loop

    def game_loop(self):

        #player_image = pygame.image.load('player.png').convert()

        tree_image = pygame.image.load('tree.png')
        tree_image.set_colorkey((255, 255, 255))
        TILE_SIZE = tree_image.get_width()

        #dirt_image = pygame.image.load('dirt.png')

        game_map = [['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
                    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

        while self.playing:  # THe while loop used for the game's main loop
            # This is called to see what the current menu is or what state the game is in.

            self.check_events()
            if self.START_KEY:  # This checks if the key assaigned to
                self.playing = False

            self.display = pygame.Surface((300,210))
            self.display.fill(self.GREEN)

            tile_rects = []
            y = 0
            for row in game_map:
                x = 0
                for tile in row:
                    if tile == '1':
                        self.display.blit(
                            tree_image, (x * TILE_SIZE, y * TILE_SIZE))
                    if tile != '0':
                        tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    x += 1
                y += 1

            surf = pygame.transform.scale(self.display, self.window_size)
            self.window.blit(surf, (0, 0))
            # This updates the display for when a key is pressed or chages state
            pygame.display.update()
            #self.window.blit(self.display, (0,0))#This is used to copy contents from the sruface to the window

            self.reset_keys()  # Reset the contorls to not being pressed

    #This is used to check if the buttons are being pressed

    def check_events(self):
        for event in pygame.event.get():  # A for loop that checks the state of the window or
            # if the any of the keys are pressed
            if event.type == pygame.QUIT:  # To check if the window is closed and shutsdown the game
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            # To check the keys that are being pressed such as:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # The enter key
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:  # The backspace key
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:  # The down key
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:  # And the up key
                    self.UP_KEY = True

    #This is used to reset the keys after being pressed or when the game states change
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    #this is used to render the text on the screeen
    def draw_text(self, text, size, x, y):
        # Sets the font for pygame to use
        font = pygame.font.Font(self.font_name, size)
        # Sets the rendering options for the text
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()  # Adds a hit box for each text
        text_rect.center = (x, y)  # sets the centre of each hitbox
        # applies the text with its hitbox
        self.display.blit(text_surface, text_rect)
