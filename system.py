from os import system
from player import Player
from game import Game
from instructions import instructions
from config import config
from art import tprint

class System:

    def __init__(self, configure=None):
        pass
        
    def run(self):
        while True:
            tprint("Snake Game........\n")
            print("1. Play")
            print("2. Instructions")
            print("3. Scores")
            print("4. Configuration")
            print("5. Exit\n")
            
            option_number = input("Enter Number Option >> ").strip()
            print()
            
            if option_number == "1":
                name = input("Player name >> ").strip()
                player = Player(name)
                play = Game(player)
                play.start()
                del(player)
                del(play)
                del(name)
            
            elif option_number == "2":
                system("cls")
                print(instructions)

            elif option_number == "3":
                Player.show_players()

            elif option_number == "4":
                while True:
                    system("cls")
                    print("Configuration........\n")
                    print("1. Show Configurations")
                    print("2. Change Configurations")
                    print("3. Back\n")
                    option_configure = input("Enter Number Option >> ")
                    if option_configure == "1":
                        config.show_configurations()

                    elif option_configure == "2":
                        print()
                        item = 1
                        item_menu = dict()

                        for key in config.configurations.keys():
                            item_menu[str(item)] = key
                            item += 1

                        for key, value in item_menu.items():
                            print(f"{key}. {value.lower()}")

                        print()
                        option_item = input("Enter Number Item >> ").strip()
                        if option_item in item_menu:
                            new_value = input("Enter new value >> ")
                            value_type = type(config.configurations[item_menu[option_item]])
                            print(value_type)
                            config.configurations = {item_menu[option_item]:value_type(new_value)}
                            

                        else:
                            print("Option Incorrect")
                        
                        print()

                    elif option_configure == "3":
                        break
                    else:
                        print("Incorrect Option.")
                    
                    input("Press any key to return to configuration menu...")


            elif option_number == "5":
                break

            else:
                print("Incorrect Option.")
        
            print()
            input("Press any key to return to principal menu...")
            system("cls")