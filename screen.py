from math import factorial
from os import system
from console import Console
from time import sleep

class Screen:

    def __init__(self, rows=30, columns=150):
        self.__rows = rows  # y
        self.__columns = columns  # x
    
    def is_limit(self, position):
        for line in range(self.__rows):  # y
            for column in range(self.__columns):  # x
                if (line==0 or line==self.__rows-1) or (column==0 or column==self.__columns-1):
                    if position.line == line and position.column == column:
                        return True
        return False

    def get_limitx(self):
        return (0, self.__rows-1)
    
    def get_limity(self):
        return (0, self.__columns-1)

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__columns

    def show_screen(self):
        command = f"mode con: cols={self.__columns} lines={self.__rows}"
        system(command)
        system("cls")

        for axi_x in range(self.__rows):
            for axi_y in range(self.__columns):
                if (axi_x==0 or axi_x==self.__rows-1) and (axi_y!=0 and axi_y!=self.__columns-1):
                    Console.show(axi_x, axi_y, "═")
                elif (axi_y==0 or axi_y==self.__columns-1) and (axi_x!=0 and axi_x!=self.__rows-1):
                    Console.show(axi_x, axi_y, "║")
                elif (axi_x==0 and axi_y == 0):
                    Console.show(axi_x, axi_y, "╔")
                elif (axi_x==0 and axi_y == self.__columns-1):
                    Console.show(axi_x, axi_y, "╗")
                elif (axi_x==self.__rows-1 and axi_y==0):
                    Console.show(axi_x, axi_y, "╚")
                elif (axi_x==self.__rows-1 and axi_y==self.__columns-1):
                    Console.show(axi_x, axi_y, "╝")
