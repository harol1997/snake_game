from msvcrt import kbhit, getch
from bbdd import File_B
from config import config
from prettytable import PrettyTable
from operator import itemgetter

class Player:
    """[player]
    """
    def __init__(self, name:str) -> None:
        """[Player constructor]

        Args:
            name (str): [player name]
        """
        self.__name = "player" if name.strip() == "" else name
        self.__score:int = 0

    @property
    def name(self):
        """[get name]

        Returns:
            [str]: [player name]
        """
        return self.__name

    @property
    def score(self):
        """[get score]

        Returns:
            [int]: [player score]
        """
        return self.__score

    @score.setter
    def score(self, score:int):
        """[set socre]

        Args:
            score (int): [new score]
        """
        self.__score = score
    
    def typing(self):
        """[user type a key]

        Returns:
            [bool or None]: [if user press key return bool else None]
        """
        return getch() if kbhit() else None

    @staticmethod
    def register(player):
        """[save player and player score]

        Args:
            player ([Player]): [player]
        """
        f = File_B(config.configurations["BASE_PLAYER_NAME"])
        f.write_file({player.name:str(player.score)})

    @staticmethod
    def show_players():
        """[print players]
        """
        scores_file = File_B(config.configurations["BASE_PLAYER_NAME"])
        table = PrettyTable()
        table.field_names = ["Item", "Player", "Score"]
        data = scores_file.read_file()
        
        if data:
            item = 1
            data_ordered = dict(sorted(data.items(), key = itemgetter(1), reverse=True))
            for key, value in data_ordered.items():
                table.add_row([item, key, value])
                item += 1                
            print(table.get_string())
        else:
            print("Yet The are not scores")