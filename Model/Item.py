class Item:

    def __init__(self, nombre:str, vida:int, fuerza:int, coste:int):
        self.Nombre = nombre.title()
        self.Vida = vida
        self.Fuerza = fuerza
        self.Coste = coste

    def GetStats(self):
        return f"Coste: {self.Coste}, Nombre: {self.Nombre}, Fuerza: {self.Fuerza}, Vida: {self.Vida}"


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