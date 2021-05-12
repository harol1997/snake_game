from bbdd import File_B
from prettytable import PrettyTable 

class Configure:  # configurator

    def __init__(self):
        self.f = File_B("config")
        #self.__configurations = self.configurations
    
    @property
    def configurations(self):
        self.f.create_if_not_exist(self.f)
        configure = self.f.read_file()

        if "BASE_PLAYER_NAME"not in configure:
            configure["BASE_PLAYER_NAME"] = "scores"
            self.f.write_file(configure)
            
        if "MAX_SPEED" not in configure:
            configure["MAX_SPEED"] = 0.5
            self.f.write_file(configure)

        if "MIN_SPEED" not in configure:
            configure["MIN_SPEED"] = 0.2
            self.f.write_file(configure)

        if "SNAKE_LINE_START" not in configure:
            configure["SNAKE_LINE_START"] = 10
            self.f.write_file(configure)

        if "SNAKE_COLUMN_START" not in configure:
            configure["SNAKE_COLUMN_START"] = 60
            self.f.write_file(configure)

        if "DIRECTION_START" not in configure:
            configure["DIRECTION_START"] = "d"
            self.f.write_file(configure)
        
        if "SIZE" not in configure:
            configure["SIZE"] = 3
            self.f.write_file(configure)
        
        return configure

    @configurations.setter
    def configurations(self, configure:dict):
        self.f.create_if_not_exist(self.f)
        print(configure)
        self.f.write_file(configure)
    
    def show_configurations(self):
        print()
        table = PrettyTable()
        table.field_names = ["Item", "Option", "Value"]
        item = 1
        
        for key, value in self.configurations.items():
            table.add_row([item, key, value])
            item += 1
        print(table.get_string(),'\n')


config = Configure()
