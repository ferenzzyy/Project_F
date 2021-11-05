from game import Game  #Imports  the Game class from game.py

g = Game() #Makes the class the into a variable for an easier use

while g.running: #Main loop for the game itself by calling the variables from the Game class
    g.curr_menu.display_menu()
    g.game_loop()
