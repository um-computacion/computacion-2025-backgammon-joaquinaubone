class Ficha:
    def __init__(self, color):
        self.__color__ = color

    def obtener_color(self):
        return self.__color__