from operator import truediv
from variables import *
import pygame

#---------------------Draws Texts-----------------------------#


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_text2(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))
#------------------------------------------------------------#


#--------------------------------------Main Menu---------------------------#


def MainMenu():
    pygame.mixer.music.load(main_music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1)

    while True:

        screen.fill((0, 0, 0))
        draw_text('Project F', font, white, screen, 190, 75)

        # menu button logic
        if start_button.draw() == True:
            Game()
        if options_button.draw() == True:
            OptionsMenu()
        if quit_button.draw() == True:
            pygame.quit()
            sys.exit()
            quit()

        # Window exit logic
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)
#--------------------------------------------------------------------------#

#--------------------------Options Menu----------------------#


def OptionsMenu():
    running = True
    while running:

        screen.fill((0, 0, 0))
        draw_text('Options', font, white, screen, 250, 75)

        if contorls_button.draw() == True:
            controls()
        if back_button.draw() == True:
            running = False
            


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)
#------------------------------------------------------------#

#-----------------------------Controls-----------------------------------#


def controls():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text('Controls', font, white, screen, 250, 75)

        screen.blit(control_img, (0, 0))
        draw_text2('<-- Quit', font3, white, 290, 185)
        draw_text2('<-- Move Player', font3, white, 330, 270)
        draw_text2('<-- Use mouse to select', font3, white, 320, 400)

        if back_button.draw() == True:
            running = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

#----------------------Main Game---------------------------#


def Game():
    # movement variables to check if player is moving
    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False
    moving = False
   


    player_location = [50, 50]

    p = pygame.transform.scale(
        player_img, (player_img.get_width() * 5, player_img.get_height() * 5))

    player_rect = pygame.Rect(
        50, 50, player_img.get_width(), player_img.get_height())

    running = True
    while running:

        # sets up the encounter rate for battles
        chance = random.randint(0, 30)

        screen.fill((34, 139, 34))

        #draw_text('omg game', font, white, screen, 20, 20)

        screen.blit(p, player_location)
        #canvas.blit(test_rect, (60, 60))

        # basic movement
        if moving_right == True:
            player_location[0] += 4
        if moving_left == True:
            player_location[0] -= 4
        if moving_up == True:
            player_location[1] -= 4
        if moving_down == True:
            player_location[1] += 4

        player_rect.x = player_location[0]
        player_rect.y = player_location[1]

        if moving == True:
            if (chance % 16) == 0:
                encounter = True
                print('Encounter!')
                Battle()
            else:
                print('Not an Encounter')
                pass
        elif moving == False:
            chance = 0
            encounter = False
            pass
        

        # movement controls
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    paused = True
                    print("Paused")
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                    moving = True
                if event.key == K_LEFT:
                    moving_left = True
                    moving = True
                if event.key == K_UP:
                    moving_up = True
                    moving = True
                if event.key == K_DOWN:
                    moving_down = True
                    moving = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                    moving = False
                if event.key == K_LEFT:
                    moving_left = False
                    moving = False
                if event.key == K_UP:
                    moving_up = False
                    moving = False
                if event.key == K_DOWN:
                    moving_down = False
                    moving = False
            

        # helps with scaling images to the screen

        pygame.display.update()
        mainClock.tick(60)
#----------------------------------------------------------#

#--------------------Battle Sequence-------------------------#


def Battle():

    current_fighter = 1
    total_fighters = 2
    action_cooldown = 0
    action_wait_time = 45

    attack = False
    target = None
    potion = False
    potion_effect = 15
    game_over = 0

    #music
    pygame.mixer.music.load(battle_music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    encounter = True
    while encounter:
        screen.fill(magenta)

        battle_panel = pygame.Rect(0, 400, 800, 500)
        pygame.draw.rect(screen, black, battle_panel)
        seperator = pygame.Rect(450, 400, 1, 500)
        pygame.draw.rect(screen, white, seperator)

        draw_text2(f'{enemy.name} HP: {enemy.hp}',
                   font3, white, 500, 425)

        draw_text2(f'{player.name} HP: {player.hp}',
                   font3, white, 200, 425)

        attack = False
        target = None
        potion = False
        if fight_button.draw() == True:
            attack = True
            target = enemy

        if items_button.draw() == True:
            potion = True

        #fight_button.draw()
        damage_text_group.update()
        damage_text_group.draw(screen)

        if special_atk_button.draw() == True:
            attack = True


        player_health_bar.draw(player.hp)
        enemy_health_bar.draw(enemy.hp)

        player.draw()
        enemy.draw()

        # control player actions
        # reset action variables

        if game_over == 0:
            #player action
            if player.alive == True:
                if current_fighter == 1:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #attack
                        if attack == True and target != None:
                            player.attack(enemy)
                            print("Hit")
                            current_fighter += 1
                            action_cooldown = 0
                        if potion == True:
                            if player.potions > 0:
                                if player.max_hp - player.hp > potion_effect:
                                    heal_amount = potion_effect
                                else:
                                    heal_amount = player.max_hp - player.hp
                                player.hp += heal_amount
                                player.potions -= 1
                                damage_text = DamageText(
                                    player.rect.centerx, player.rect.y, str(heal_amount), green)
                                damage_text_group.add(damage_text)
                                current_fighter += 1
                                action_cooldown = 0
            else:
                game_over = -1

            if current_fighter == 2:
                if enemy.alive == True:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        enemy.attack(player)
                        print("Enemy hit you")
                        current_fighter += 1
                        action_cooldown = 0
                else:
                    current_fighter += 1

            if current_fighter > total_fighters:
                current_fighter = 1

            if enemy.hp <= 0:
                enemy.alive = False
            
            if player.hp <= 0:
                player.alive = False

        #alive_enemies = 0
        if enemy.alive == False:
            game_over = 1

        if game_over != 0:
            if game_over == 1:
                victory_screen()
            if game_over == -1:
                defeat_screen()
            # if back_button.draw():
            #     running = False
            
        else:
            pass

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        pygame.display.update()
        mainClock.tick(60)
#------------------------------------------------------------#

#--------------------- victory screen------------------#
def victory_screen():

    screen.blit(victory_img, (0, 0))
    pygame.mixer.music.load(victory_music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    win = True
    while win:
        

        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        running = False
        pygame.display.update()
        mainClock.tick(60)
#----------------------Pause menu-----------------------#

# -------------------Defeat screen--------------------#
def defeat_screen():
    screen.blit(defeat_img, (0, 0))
    pygame.mixer.music.load(defeat_music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    lose =True
    while lose:
    
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    quit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        MainMenu()
        pygame.display.update()
        mainClock.tick(60)

def pause_menu():
    pause = True

    while pause:
        #pause_panel = pygame.Rect(50, 250, 800, 500)
        screen.fill((0, 0, 0))
        #screen.blit(pause_img, (550, 60))
        #draw_text('Paused', font, white, screen, 250, 75)

        if save_button.draw() == True:
            print("this will save your game!")
        if options2_button.draw() == True:
            print("Options menu")
            OptionsMenu()
            #p_options_menu()
            
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = False
                    print("Resumed")
        pygame.display.update()
        mainClock.tick(60)

#--------------------Pause Options Menu----------------#
def p_options_menu():
    options = True
    while options:
        #screen.fill((0, 0, 0))
        draw_text('Options', font, white, screen, 250, 75)

        if contorls_button.draw() == True:
            controls()
        if back_button.draw() == True:
            options = False
            


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def volume_opt():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        draw_text('Volume', font, white, screen, 250, 75)

        if back_button.draw() == True:
            running = False
        


        pygame.display.update()
        mainClock.tick(60)



