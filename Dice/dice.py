import random

class Dice:

    def __init__(self): 
        self.__values__ = []

    def tirar(self):    

        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        self.__values__ = [dado1, dado2]
    
    def obtener_valores(self): 
        return self.__values__
    
    def resetear(self):  # elimina todos los valores disponibles (usado al final del turno)
        self.__values__ = []

    def sin_valores(self):  # saber si quedan valores disponibles
        return len(self.__values__) == 0