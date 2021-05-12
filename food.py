from random import randint
from position import Position
from console import Console
from colorama import Fore


class Food:
    """[class to generate snake food]
    """
    def __init__(self, position):
        """[Food constructor]

        Args:
            position ([Position]): [object Position]
        """
        self.__position = position

    @property
    def position(self):
        """[get position]

        Returns:
            [Position]: [object Position]
        """
        return self.__position

    @staticmethod
    def generate_food(positions:list, limitsx:tuple, limitsy:tuple):
        """[generate snake food]

        Args:
            positions (list): [snake body]
            limitsx (tuple): [limits line of screen]
            limitsy (tuple): [limits columns of screen]

        Returns:
            [Food]: [snake Food]
        """
        
        while True:
            
            line = randint(limitsx[0]+2, limitsx[1]-2)
            column = randint(limitsy[0]+2, limitsy[1]-2)
            
            position_food = Position(line, column)
            
            result = list(map(lambda pos: pos == position_food, positions))

            if len(set(result)) == 1 and not result[0]:
                return Food(position_food)
    
    @staticmethod
    def show_food(food):
        """[print food]

        Args:
            food ([Food]): [snake food]
        """
        Console.show(food.position.line,food.position.column, f"{Fore.WHITE}▄")
