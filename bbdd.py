from json import dump, load
from os import path

class File_B:
    """[class to acces a player database]
    """
    def __init__(self, name_file:str):
        """[File_B constructor]

        Args:
            name_file ([str]): [file name]
        """
        self.__name_file = name_file+".json"

    @property
    def name(self):
        """[get name]

        Returns:
            [str]: [file name]
        """
        return self.__name_file

    def read_file(self) -> dict:
        """[get data of file]

        Returns:
            dict: [players datas]
        """
        with open (self.__name_file,"r") as f:
            
            return load(f) 

    def write_file(self, data):
        """[save players]

        Args:
            data ([dict]): [players datas]
        """
        last_data = self.read_file()
        
        last_data.update(data)
        with open(self.__name_file,"w") as f:
            dump(last_data, f)

    @staticmethod
    def create_if_not_exist(f:"File_B"):
        """[create a new player database in o.s
            It will create a file in the same path
            of main script]

        Args:
            f (File_B): [object File_B]
        """
        if  not path.exists(f.name):
            with open(f.name,"w") as fi:
                dump({},fi)
