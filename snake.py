from position import Position
from console import Console
from colorama import Fore


class  Snake:

    def __init__(self, direction, line_start, column_start, size, min_speed, max_speed):
        """[Snake init]

        Args:
            direction ([str]): [direction for first time]
            line_start (int, optional): [row in terminal]. Defaults to 10.
            column_start (int, optional): [column in terminal]. Defaults to 10.
            size (int, optional): [snake length]. Defaults to 3.
        """
        self.__body = [Position(line_start, column_start+i) for i in range(size)]
        self.__speed = max_speed
        self.__direction = direction
        self.__MIN_SPEED = min_speed  # it works with sleep in main.py

    @property
    def speed(self):
        """[getter method]

        Returns:
            [float]: [snake speed]
        """
        return self.__speed
    
    @speed.setter
    def speed(self, new_speed:int):
        """[set snake speed]

        Args:
            new_speed (int): [new snake speed]
        """
        self.__speed = self.__MIN_SPEED if new_speed < self.__MIN_SPEED else new_speed

    @classmethod
    def show_body(cls, snake):
        """[print body]

        Args:
            snake ([Snake]): [object Snake]
        """
        for position in snake.body[:-1]:
            Console.show(position.line, position.column, f"{Fore.WHITE}*")
        Console.show(snake.body[-1].line, snake.body[-1].column, f"{Fore.RED}*")
        

    def __change_position(self,position):
        """[private method to update snake body]

        Args:
            position ([Position]): [object Position]
        """
        Console.show(self.__body[0].line, self.__body[0].column, " ")
        self.__body.pop(0)
        self.__body.append(position)
        self.show_body(self)

    def get_position(self):
        """[get the last position of snake body(head)]

        Returns:
            [Position]: [object Position]
        """
        return self.__body[-1]

    @property
    def body(self):
        """[method getter]

        Returns:
            [list]: [snake body]
        """
        return self.__body

    def move(self, key):
        """[move snake]

        Args:
            key ([byte]): [user key]
        """
        if not key: key = self.__direction

        if key == b'w' and self.__direction != b's':
            self.__up()
            self.__direction = key
        elif key == b's' and self.__direction != b'w':
            self.__down()
            self.__direction = key
        elif key == b'a' and self.__direction != b'd':
            self.__left()
            self.__direction = key
        elif key == b'd' and self.__direction != b'a':
            self.__right()
            self.__direction = key

    def  __up(self):
        self.__change_position(Position(self.__body[-1].line-1, self.__body[-1].column))

    def  __down(self):
        self.__change_position(Position(self.__body[-1].line+1, self.__body[-1].column))

    def  __left(self):
        self.__change_position(Position(self.__body[-1].line, self.__body[-1].column-1))

    def  __right(self):
        self.__change_position(Position(self.__body[-1].line, self.__body[-1].column+1))

    def  eat(self, food):
        """"[summary]

        Args:
            food ([Food]): [object generated in game.py]

        Returns:
            [bool]: [If ate -> True else False]
        """
        if self.__body[-1] == food.position:
        
            position = self.__body[0]  # last position
            if self.__direction == b'w':            
                self.__body.insert(0, Position(position.line-1, position.column))

            elif self.__direction == b's':
                self.__body.insert(0, Position(position.line+1, position.column))
            
            elif self.__direction == b'a':
                self.__body.insert(0, Position(position.line, position.column-1))
            
            else:
                self.__body.insert(0, Position(position.line, position.column+1))
            return True
        return False

    def auto_lost(self):
        """[detect if snake ate yourself]

        Returns:
            [bool]: [True if lost. False else]
        """
        for position in self.__body[:-1]:
            if position == self.__body[-1]:
                return True
        return False 
