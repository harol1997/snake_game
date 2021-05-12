class Position():
    def __init__(self, line, column):
        self.__line = line
        self.__column = column

    def __eq__(self, position) -> bool:
        return self.__line == position.line and self.__column == position.column

    @property
    def line(self):
        return self.__line

    @property
    def column(self):
        return self.__column
