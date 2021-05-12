from ctypes import byref, c_char_p, windll, Structure, c_short, c_int
from os import system
from time import sleep

class CONSOLE_CURSOR_INFO(Structure):
    _fields_ = [('dwSize', c_int),
                ('bVisible', c_int)]

class Console(Structure):

    STD_OUTPUT_HANDLE = -11

    _fields_ = [("X", c_short), ("Y", c_short)]

    @classmethod
    def show(cls, x:int, y:int , out:str):
        """[show str in line:x and column:y]

        Args:
            x (int): [terminal line]
            y (int): [terminal column]
            out (str): [data to print]
        """
        h = windll.kernel32.GetStdHandle(cls.STD_OUTPUT_HANDLE)
        
        info_cursor = CONSOLE_CURSOR_INFO()
        info_cursor.dwSize = 1
        info_cursor.bvVisible = 0

        windll.kernel32.SetConsoleCursorInfo(h,byref(info_cursor))

        windll.kernel32.SetConsoleCursorPosition(h,Console(y,x))
        try:
            mssg = out.encode("windows-1252")
        except UnicodeEncodeError:
            mssg = out.encode("cp437")

        windll.kernel32.WriteConsoleA(h, c_char_p(mssg), len(mssg), None, None)
        
if __name__ == '__main__':
    system("cls")
    Console.show(10,30,'*')
    sleep(0.3)
    Console.show(28,140,'*')
    