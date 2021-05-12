# system menu

from config import Configure
from system import System
from bbdd import File_B
from os import system

#enable()

system("cls")

bbdd = File_B("scores")
File_B.create_if_not_exist(bbdd)

config = Configure()

system = System(config)
system.run()
