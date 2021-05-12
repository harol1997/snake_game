from config import config
from food import Food
from os import system
from screen import Screen
from snake import Snake
from time import sleep
from player import Player
from colorama import Fore
from threading import Thread

class Game:
    """
    snake game
    """

    def __init__(self, player:Player):
        """[Game constructor]

        Args:
            player (Player): [player]
        """
        self.__player = player
        self.snake = Snake(line_start=config.configurations["SNAKE_LINE_START"], 
                            column_start=config.configurations["SNAKE_COLUMN_START"], 
                            direction=config.configurations["DIRECTION_START"].encode(),
                            size=config.configurations["SIZE"],
                            min_speed=config.configurations["MIN_SPEED"],
                            max_speed=config.configurations["MAX_SPEED"])
        self.screen = Screen()  # game screen
        self.cycle = True  # game cycle
        self.food = None
        
    def start(self):
        """[start game]
        """
        self.screen.show_screen()
        Snake.show_body(self.snake)
        
        lost = False
        score = 0
        control_generate_food = True  # allow execute only one time call_generate_food() if is necesary

        while self.cycle:
            key = self.__player.typing()

            if key == b'\x1b':
                self.stop()
            else:
                self.snake.move(key)
            
            #food
            if not self.food and control_generate_food:
                Thread(target=self.__call_generate_food).start()
                control_generate_food = False
            elif self.food:
                if self.snake.eat(self.food):  
                    score += 1
                    self.food = None
                    self.snake.speed -= 0.005
                    control_generate_food = True
            #food

            if self.screen.is_limit(self.snake.get_position()) or self.snake.auto_lost():
                lost = True
                self.stop()

            sleep(self.snake.speed)
        print(Fore.WHITE)

        if lost:
            sleep(0.5)
            print("I'm sorry . You lost\n")    
        
        self.__player.score = score
        print("Player:", self.__player.name)
        print("Total Score:", self.__player.score)

        Player.register(self.__player)
    
    def __call_generate_food(self):
        self.food:Food = Food.generate_food(self.snake.body, self.screen.get_limitx(), self.screen.get_limity())
        Food.show_food(self.food)

    def stop(self):
        """[stop game]
        """
        self.cycle = False
        system("cls")
