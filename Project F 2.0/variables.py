from pygame.locals import *
import pygame
import sys
import random
import button
import time


# Variables for the main window
mainClock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
window_size = (800, 600)
screen = pygame.display.set_mode((window_size), 0, 32)
pygame.display.set_caption('Project F')
state = "MainMenu"

# Music & Sounds
b_click = pygame.mixer.Sound('music/click.mp3')
heal = pygame.mixer.Sound('music/heal.mp3')
hit = pygame.mixer.Sound('music/hit.mp3')
main_music = 'music/minecraft.mp3'
battle_music = 'music/battle.mp3'
victory_music = 'music/victory.mp3'
defeat_music = 'music/defeat.mp3'




# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
magenta = (138, 43, 226)

# screen images
victory_img = pygame.image.load('assets/screens/victory_screen.png')
defeat_img = pygame.image.load('assets/screens/defeat_screen.png')
control_img = pygame.image.load('assets/screens/controls_screen.png')
control_img.set_colorkey(white)
pause_img = pygame.image.load('assets/screens/pause_back.png')

# fonts
font = pygame.font.Font('assets/fonts/8-BIT WONDER.TTF', 50)
font2 = pygame.font.Font('assets/fonts/INVASION2000.TTF', 10)
font3 = pygame.font.Font('assets/fonts/INVASION2000.TTF', 26)
# player images
player_img = pygame.image.load('assets/sprites/player.png').convert()
player_img.set_colorkey(white)

# button images
start_img = pygame.image.load('assets/buttons/Start_button.png')
options_img = pygame.image.load('assets/buttons/Options_button.png')
quit_img = pygame.image.load('assets/buttons/Quit_button.png')
controls_img = pygame.image.load('assets/buttons/Controls_button.png')
back_img = pygame.image.load('assets/buttons/Back_button.png')
save_img = pygame.image.load('assets/buttons/save_button.png') 


# Battle buttons images
fight_img = pygame.image.load('assets/buttons/Fight_button.png')
items_img = pygame.image.load('assets/buttons/Items_button.png')
special_atk_img = pygame.image.load('assets/buttons/Sp_atk_button.png')

# The main menu buttons intanceses
start_button = button.Button(screen, 250, 250, start_img, 250, 50)
options_button = button.Button(screen, 250, 320, options_img, 250, 50)
quit_button = button.Button(screen, 250, 400, quit_img, 250, 50)
contorls_button = button.Button(screen, 250, 250, controls_img, 250, 50)
back_button = button.Button(screen, 590, 525, back_img, 200, 50)
options2_button = button.Button(screen, 580, 150, options_img, 190, 40)
save_button = button.Button(screen, 580, 100, save_img, 190, 40)

# Option Menu button instances


# battle menu button intanceses
fight_button = button.Button(screen, 1, 425, fight_img, 200, 50)
items_button = button.Button(screen, 1, 475, items_img, 200, 50)
special_atk_button = button.Button(screen, 5, 525, special_atk_img, 200, 50)



class Fighter():
    def __init__(self, x, y, name, max_hp, atk_dmg, magic_dmg, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.potions = potions
        self.start_potions = potions
        self.atk_dmg = atk_dmg
        self.magic_dmg = magic_dmg
        self.alive = True
        img = pygame.image.load(f'assets/sprites/{self.name}.png').convert()
        self.image = pygame.transform.scale(
            img, (img.get_width() * 5, img.get_height() * 5))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def attack(self, target):
        #deal damgae to emnemy
        rand = random.randint(-5, 5)
        damage = self.atk_dmg + rand
        target.hp -= damage
        damage_text = DamageText(
            target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)

    def draw(self):
        self.image.set_colorkey((255, 255, 255))
        screen.blit(self.image, self.rect)


class HealthBar():
	def __init__(self, x, y, hp, max_hp):
		self.x = x
		self.y = y
		self.hp = hp
		self.max_hp = max_hp

	def draw(self, hp):
		#update with new health
		self.hp = hp
		#calculate health ratio
		ratio = self.hp / self.max_hp
		pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
		pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font3.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        # move damage text up
        self.rect.y -= 1
        # delete after a few seconds
        self.counter += 1
        if self.counter > 30:
            self.kill()


damage_text_group = pygame.sprite.Group()


# Player & enemy with their healthbar instances
player = Fighter(150, 260, 'player', 30, 8, 10, 3)

enemy = Fighter(600, 210, 'dragon', 30, 8, 10, 3)

enemy_health_bar = HealthBar(525, 475, enemy.hp, enemy.max_hp)
player_health_bar = HealthBar(220, 475, player.hp, player.max_hp)
