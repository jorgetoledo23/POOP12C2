class Item:

    def __init__(self, nombre:str, vida:int, fuerza:int, coste:int):
        self.__Nombre = nombre.title()
        self.__Vida = vida
        self.__Fuerza = fuerza
        self.__Coste = coste

    def GetStats(self):
        return f"Coste: {self.__Coste}, Nombre: {self.__Nombre}, Fuerza: {self.__Fuerza}, Vida: {self.__Vida}"

    def GetCoste(self):
        return self.__Coste

    def GetVida(self):
        return self.__Vida

    def GetFuerza(self):
        return self.__Fuerza

    def GetNombre(self):
        return self.__Nombre


Item1 = Item("Espada", 0, 100, 300)
Item2 = Item("Armadura", 200, 20, 400)
Item3 = Item("Daga", 0 , 30, 50)
Item4 = Item("Pocion de Ataque", 0 , 50, 100)
Item5 = Item("Pocion de Defenza", 50, 0 ,100)
Item6 = Item("Escudo", 80, 0, 100)

ListadoItems = []
ListadoItems.append(Item1)
ListadoItems.append(Item2)
ListadoItems.append(Item3)
ListadoItems.append(Item4)
ListadoItems.append(Item5)
ListadoItems.append(Item6)